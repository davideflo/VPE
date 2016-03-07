## Code for fault prediction Machine Learning - UCI dataset

# useful libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# import of the data
data = pd.read_table("faults.txt", sep = "\t", header = 0)

# 
headers = data.dtypes.index

# plot a histogram for each variable
#plt.ion()
for col in headers:
	plt.figure()
	plt.hist(data[col], bins = 50, normed=True)
	plt.show()
	_ = input("press [enter] to continue")
	plt.close()


# code for Figure 1
fig, ax = plt.subplots(2, 2, sharex=False, sharey=False)
fig.subplots_adjust(hspace=0.25, wspace=0.25)
fig.suptitle('Histograms')
ax[0,0].hist(data['Minimum_of_Luminosity '], bins = 50, normed=True, color='blue')
ax[1,0].hist(data['Maximum_of_Luminosity '], bins = 50, normed=True, color='blue')
ax[0,1].hist(data['Log_X_Index '], bins = 50, normed=True, color='blue')
ax[1,1].hist(data['Steel_Plate_Thickness '], bins = 50, normed=True, color='blue')
plt.show()

# defining the fault types
fault_types = headers[27:34]

# computing how many observations in each fault class
numerosity = []
for ft in fault_types:
	ixft = data.ix[data[ft] > 0]
	C = ixft[ft].count()
	numerosity.append(C)
	print(ft)
	print(C)

# function to separate each class from the others
def get_fault_types(df, fault):
	data_f = df.ix[df[fault] > 0]
	data_f = data_f.reset_index(drop=True)
	return(data_f)

# separating each fault type
pastry = get_fault_types(data, 'Pastry ')
z_scratch = get_fault_types(data, 'Z_Scratch ')
k_scratch = get_fault_types(data, 'K_Scatch ')
stains = get_fault_types(data, 'Stains ')
dirtiness = get_fault_types(data, 'Dirtiness ')
bumps = get_fault_types(data, 'Bumps ')
other = get_fault_types(data, 'Other_Faults ')

# code for scatterplots.
# defining the colours for each fault class
# defining a function that given the name of two vatiables
# plots the associate scatterplot
faultcolors = [fault_types[i].replace('Pastry ','b').replace('Z_Scratch ','g').replace('K_Scatch ','r').replace('Stains ','c').replace('Dirtiness ','m').replace('Bumps ','y').replace('Other_Faults ','k') for i in range(len(fault_types))]

def scatterplot(variable1, variable2):
	plt.figure()
	plt.scatter(data[variable1], data[variable2], c=faultcolors)
	pr = plt.Rectangle((0, 0), 1, 1, fc='r')
	pg = plt.Rectangle((0, 0), 1, 1, fc='g')
	pb = plt.Rectangle((0, 0), 1, 1, c='b')
	pc = plt.Rectangle((0, 0), 1, 1, fc='c')
	py = plt.Rectangle((0, 0), 1, 1, fc='y')
	pm = plt.Rectangle((0, 0), 1, 1, fc='m')
	pk = plt.Rectangle((0, 0), 1, 1, fc='k')
	plt.legend([pr, pg, pb,pc,py,pm,pk], ['k_scratch', 'Z_Scratch', 'Pastry','Stains', 'Bumps','Dirtiness','Other_Faults'])
	plt.show()

# BEGIN: DO NOT RUN
# scatterplot for each pair of consecutive variables
#for i in range(26):
#	scatterplot(headers[i], headers[i+1])
#	_ = input("press [enter] to continue")
#	plt.close()
# END: DO NOT RUN

# computing the covariance matrix for each class
for ft in fault_types:
	ixft = data.ix[data[ft] > 0]
	var_vect = ixft.var().sort_values(inplace=False)
	print(ft)
	print(var_vect)

# PCA for each class
from sklearn.decomposition import PCA

pca_pastry = PCA()
pca_pastry = pca_pastry.fit(pastry)

pca_pastry.explained_variance_ratio_
pca_pastry.components_

pca_z = PCA()
pca_z = pca_pastry.fit(z_scratch)

pca_k = PCA()
pca_k = pca_pastry.fit(k_scratch)

pca_stains = PCA()
pca_stains = pca_pastry.fit(stains)

pca_dirtiness = PCA()
pca_dirtiness = pca_pastry.fit(dirtiness)

pca_bumps = PCA()
pca_bumps = pca_pastry.fit(bumps)

pca_other = PCA()
pca_other = pca_pastry.fit(other)

###############################################
########### DATA MODELLING ####################
###############################################

from sklearn.metrics import mean_squared_error, confusion_matrix, precision_recall_curve
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.ensemble.partial_dependence import plot_partial_dependence
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint as sp_randint
from operator import itemgetter

# definition of parameters and grids for grid search in RF and GB
def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
              score.mean_validation_score,
              np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")

param_dist_RF = {"max_depth": [4, None],
        "max_features": sp_randint(1,2),
        "min_samples_split": sp_randint(1,2),
        "min_samples_leaf": sp_randint(1,2),
        "bootstrap": [True, False],
        "criterion": ["gini", "entropy"]}

param_dist_GB = {"loss": ["deviance"],
                   "learning_rate": [0.05, 0.1, 0.2],
                   "max_depth": [1,2,3]}

# stratified sampling to build the training set
train_ix = list([])
num = np.array(numerosity).cumsum()
for i in range(len(fault_types)):
	ixft = data.ix[data[fault_types[i]] > 0]
	rows = ixft.shape[0]
	if i <= 0:
		ix = list(np.random.randint(0, num[i]-1, size= np.ceil(rows*0.8)) )
	else:
		ix = list(np.random.randint(num[i-1]-1, num[i]-1, size= np.ceil(rows*0.8)))
	train_ix = train_ix + ix

# the remaining 20% of the data goes into the testing set
test_ix = list(set(range(data.shape[0])).difference(set(train_ix)))
test_ix = np.asarray(test_ix)

train_ix = np.asarray(train_ix)

trainset = data.ix[train_ix]
testset = data.ix[test_ix]

data = data[list(range(27))]
trainset = trainset[list(range(27))]
testset = testset[list(range(27))]

out = np.array([0,1,2,3,4,5,6])
outcome = np.repeat(out, numerosity)

train_outcome = outcome[train_ix]
test_outcome = outcome[test_ix]

# initialize and compute best RF classifier
forest = RandomForestClassifier(n_estimators = 200)
random_search = RandomizedSearchCV(forest, param_distributions=param_dist_RF, n_iter=40)
random_search.fit(trainset, train_outcome)
report(random_search.grid_scores_)
bestmodel = RandomForestClassifier(n_estimators=200, criterion="gini", max_features=1, bootstrap=True, max_depth=None, min_samples_leaf=1, min_samples_split=1)
rfc = bestmodel.fit(trainset, train_outcome)

# feature importance for RF
rfc.feature_importances_
res_rf = rfc.predict(testset)

# MSE and misclassification error:
mse_rf = mean_squared_error(res_rf, test_outcome)
## 3.0264976958525347

confusion_matrix(res_rf, test_outcome)

## empirical misclassification error:
1 - (np.diag(confusion_matrix(res_rf, test_outcome)).sum())/(confusion_matrix(res_rf, test_outcome).sum())
# 0.2375434530706837
#precision_recall_curve(test_outcome, res_rf)

# initialize and compute the best GB classifier
gb = GradientBoostingClassifier(n_estimators=200)
random_search_grad = GridSearchCV(gb, param_dist_GB)
random_search_grad.fit(trainset, train_outcome)
report(random_search_grad.grid_scores_)
grad_fit = GradientBoostingClassifier(n_estimators=200, loss="deviance", learning_rate=0.1, max_depth=3)
gbfit = grad_fit.fit(trainset, train_outcome)

# feature importance for GB
gbfit.feature_importances_
res_gb = gbfit.predict(testset)

# plot of feature importance for the two methods
fig, ax = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)
pos = np.arange(len(gbfit.feature_importances_)) + 1
ax[0].plot(pos, gbfit.feature_importances_, color='blue')
ax[1].plot(pos, rfc.feature_importances_, color='red')
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()

# MSE and misclassification error for GB
mse_gb = mean_squared_error(res_gb,test_outcome)
## 2.7338709677419355

confusion_matrix(res_gb, test_outcome)
#precision_recall_curve(test_outcome, res_gb)
## empirical misclassification error:
1 - (np.diag(confusion_matrix(res_gb, test_outcome)).sum())/(confusion_matrix(res_gb, test_outcome).sum())
# 0.22595596755504055

## misclassification error per class:

drf = np.diag(confusion_matrix(res_rf, test_outcome))
dgb = np.diag(confusion_matrix(res_gb, test_outcome))
crf = confusion_matrix(res_rf, test_outcome).sum(axis=0)
cgb = confusion_matrix(res_gb, test_outcome).sum(axis=0)
errors_rf = np.zeros(7)
errors_gb = np.zeros(7)
for i in range(len(fault_types)):
	errors_rf[i] = 1 - (drf[i])/(crf[i])
	errors_gb[i] = 1 - (dgb[i])/(cgb[i])

#partial dependence plots
features = [1, 10, 14, (10, 14)]
fig, axs = plot_partial_dependence(gbfit, trainset, features,label=gbfit.classes_[0],n_jobs=2, grid_resolution=50)
fig.suptitle('Partial dependence of X_Maximum, Length_of_Conveyer and Edges_Index for Pastry faults')
####### comments #######
# The better mse of the GBM is very likely due to a better recognition
# of the Z_scratch fault. A little contribution due also to Bumps.
# The most mistaken fault types are bumpiness and other faults. 
# In case of other faults, this was quite expected: firstly for the high 
# numerosity of the class, compared to the others. Secondly, because the class 
# 'other' is too broad and not well defined. Therefore it is likely that 
# shares many common features with the remaining fault types. Plot only
# this group to see if there are better clusters.