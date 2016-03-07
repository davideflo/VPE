## Fault - BigML

def predict_fault(data={}):
    """ Predictor for Fault from model/56d595a43bbd2125ce00317f

        A dataset of steel plates’ faults, classified into 7 different types. The goal was to train machine learning for automatic pattern recognition.
        ** Source **
        Steel Plates Faults Data Set[*] at UCI[*] Machine Learning Repository[*]
        [*]Steel Plates Faults Data Set: http://archive.ics.uci.edu/ml/datasets/Steel+Plates+Faults
        [*]UCI: http://cml.ics.uci.edu/
        [*]Machine Learning Repository: http://archive.ics.uci.edu/ml/index.html
    """
    if (data.get('log_x_index') is None):
        return u'Other_Faults'
    if (data['log_x_index'] <= 2.02965):
        if (data.get('typeofsteel_a4falsefalse') is None):
            return u'Other_Faults'
        if (data['typeofsteel_a4falsefalse'] == 'True'):
            if (data.get('logofareas') is None):
                return u'Other_Faults'
            if (data['logofareas'] <= 1.49081):
                if (data.get('sum_of_luminosity') is None):
                    return u'Stains'
                if (data['sum_of_luminosity'] > 486):
                    if (data['logofareas'] <= 1.3613):
                        return u'Stains'
                    if (data['logofareas'] > 1.3613):
                        if (data.get('edges_index') is None):
                            return u'Stains'
                        if (data['edges_index'] > 0.51205):
                            if (data['edges_index'] <= 0.85195):
                                return u'Other_Faults'
                            if (data['edges_index'] > 0.85195):
                                return u'Stains'
                        if (data['edges_index'] <= 0.51205):
                            return u'Stains'
                if (data['sum_of_luminosity'] <= 486):
                    return u'K_Scatch'
            if (data['logofareas'] > 1.49081):
                if (data.get('orientation_index') is None):
                    return u'Other_Faults'
                if (data['orientation_index'] > 0.48215):
                    if (data.get('length_of_conveyer') is None):
                        return u'Other_Faults'
                    if (data['length_of_conveyer'] <= 1371):
                        if (data.get('y_maximum') is None):
                            return u'Other_Faults'
                        if (data['y_maximum'] > 1535080):
                            if (data['y_maximum'] <= 3167875):
                                if (data.get('minimum_of_luminosity') is None):
                                    return u'Dirtiness'
                                if (data['minimum_of_luminosity'] > 91):
                                    if (data.get('x_minimum') is None):
                                        return u'Dirtiness'
                                    if (data['x_minimum'] <= 317):
                                        return u'Bumps'
                                    if (data['x_minimum'] > 317):
                                        if (data.get('x_perimeter') is None):
                                            return u'Dirtiness'
                                        if (data['x_perimeter'] > 12):
                                            if (data.get('empty_index') is None):
                                                return u'Dirtiness'
                                            if (data['empty_index'] <= 0.27815):
                                                if (data['logofareas'] > 2.1687):
                                                    return u'Other_Faults'
                                                if (data['logofareas'] <= 2.1687):
                                                    return u'Dirtiness'
                                            if (data['empty_index'] > 0.27815):
                                                return u'Dirtiness'
                                        if (data['x_perimeter'] <= 12):
                                            return u'Bumps'
                                if (data['minimum_of_luminosity'] <= 91):
                                    if (data['length_of_conveyer'] <= 1360):
                                        return u'Pastry'
                                    if (data['length_of_conveyer'] > 1360):
                                        if (data['logofareas'] > 3.36905):
                                            return u'K_Scatch'
                                        if (data['logofareas'] <= 3.36905):
                                            return u'Bumps'
                            if (data['y_maximum'] > 3167875):
                                if (data.get('minimum_of_luminosity') is None):
                                    return u'Pastry'
                                if (data['minimum_of_luminosity'] > 84):
                                    if (data.get('empty_index') is None):
                                        return u'Other_Faults'
                                    if (data['empty_index'] <= 0.2948):
                                        return u'Pastry'
                                    if (data['empty_index'] > 0.2948):
                                        return u'Other_Faults'
                                if (data['minimum_of_luminosity'] <= 84):
                                    return u'Pastry'
                        if (data['y_maximum'] <= 1535080):
                            if (data.get('edges_index') is None):
                                return u'Other_Faults'
                            if (data['edges_index'] <= 0.08872):
                                if (data['y_maximum'] > 154569):
                                    if (data.get('minimum_of_luminosity') is None):
                                        return u'Other_Faults'
                                    if (data['minimum_of_luminosity'] <= 63):
                                        if (data.get('empty_index') is None):
                                            return u'Other_Faults'
                                        if (data['empty_index'] > 0.46915):
                                            return u'Other_Faults'
                                        if (data['empty_index'] <= 0.46915):
                                            if (data.get('square_index') is None):
                                                return u'Pastry'
                                            if (data['square_index'] <= 0.05995):
                                                return u'Other_Faults'
                                            if (data['square_index'] > 0.05995):
                                                return u'Pastry'
                                    if (data['minimum_of_luminosity'] > 63):
                                        return u'Other_Faults'
                                if (data['y_maximum'] <= 154569):
                                    if (data.get('x_minimum') is None):
                                        return u'Dirtiness'
                                    if (data['x_minimum'] <= 42):
                                        if (data['edges_index'] > 0.0492):
                                            return u'Pastry'
                                        if (data['edges_index'] <= 0.0492):
                                            if (data['edges_index'] <= 0.01255):
                                                return u'Dirtiness'
                                            if (data['edges_index'] > 0.01255):
                                                return u'Other_Faults'
                                    if (data['x_minimum'] > 42):
                                        return u'Dirtiness'
                            if (data['edges_index'] > 0.08872):
                                if (data.get('edges_y_index') is None):
                                    return u'Other_Faults'
                                if (data['edges_y_index'] > 0.97555):
                                    if (data.get('edges_x_index') is None):
                                        return u'Other_Faults'
                                    if (data['edges_x_index'] <= 0.2973):
                                        if (data.get('minimum_of_luminosity') is None):
                                            return u'Pastry'
                                        if (data['minimum_of_luminosity'] > 77):
                                            if (data['edges_index'] <= 0.3313):
                                                return u'Z_Scratch'
                                            if (data['edges_index'] > 0.3313):
                                                return u'Other_Faults'
                                        if (data['minimum_of_luminosity'] <= 77):
                                            return u'Pastry'
                                    if (data['edges_x_index'] > 0.2973):
                                        if (data.get('x_maximum') is None):
                                            return u'Other_Faults'
                                        if (data['x_maximum'] > 1255):
                                            if (data.get('square_index') is None):
                                                return u'Pastry'
                                            if (data['square_index'] <= 0.3926):
                                                return u'Pastry'
                                            if (data['square_index'] > 0.3926):
                                                return u'Other_Faults'
                                        if (data['x_maximum'] <= 1255):
                                            if (data['edges_x_index'] <= 0.68335):
                                                if (data['y_maximum'] > 419400):
                                                    if (data['length_of_conveyer'] <= 1337):
                                                        return u'Bumps'
                                                    if (data['length_of_conveyer'] > 1337):
                                                        return u'Other_Faults'
                                                if (data['y_maximum'] <= 419400):
                                                    if (data.get('empty_index') is None):
                                                        return u'Other_Faults'
                                                    if (data['empty_index'] <= 0.3346):
                                                        return u'Other_Faults'
                                                    if (data['empty_index'] > 0.3346):
                                                        return u'Pastry'
                                            if (data['edges_x_index'] > 0.68335):
                                                return u'Bumps'
                                if (data['edges_y_index'] <= 0.97555):
                                    if (data['y_maximum'] <= 682685):
                                        if (data['edges_index'] > 0.7602):
                                            return u'Bumps'
                                        if (data['edges_index'] <= 0.7602):
                                            if (data['y_maximum'] <= 31313):
                                                return u'Z_Scratch'
                                            if (data['y_maximum'] > 31313):
                                                return u'Other_Faults'
                                    if (data['y_maximum'] > 682685):
                                        if (data['edges_index'] > 0.16015):
                                            return u'Z_Scratch'
                                        if (data['edges_index'] <= 0.16015):
                                            return u'Other_Faults'
                    if (data['length_of_conveyer'] > 1371):
                        if (data.get('empty_index') is None):
                            return u'Other_Faults'
                        if (data['empty_index'] > 0.4351):
                            if (data['orientation_index'] <= 0.77285):
                                if (data.get('luminosity_index') is None):
                                    return u'Other_Faults'
                                if (data['luminosity_index'] > -0.0123):
                                    if (data.get('sigmoidofareas') is None):
                                        return u'Other_Faults'
                                    if (data['sigmoidofareas'] <= 0.9612):
                                        return u'Other_Faults'
                                    if (data['sigmoidofareas'] > 0.9612):
                                        return u'K_Scatch'
                                if (data['luminosity_index'] <= -0.0123):
                                    return u'Other_Faults'
                            if (data['orientation_index'] > 0.77285):
                                if (data['length_of_conveyer'] > 1531):
                                    if (data.get('edges_index') is None):
                                        return u'Pastry'
                                    if (data['edges_index'] <= 0.0947):
                                        return u'Other_Faults'
                                    if (data['edges_index'] > 0.0947):
                                        return u'Pastry'
                                if (data['length_of_conveyer'] <= 1531):
                                    if (data.get('maximum_of_luminosity') is None):
                                        return u'Other_Faults'
                                    if (data['maximum_of_luminosity'] <= 217):
                                        return u'Other_Faults'
                                    if (data['maximum_of_luminosity'] > 217):
                                        return u'K_Scatch'
                        if (data['empty_index'] <= 0.4351):
                            if (data.get('x_minimum') is None):
                                return u'Pastry'
                            if (data['x_minimum'] <= 1399):
                                if (data.get('edges_index') is None):
                                    return u'Pastry'
                                if (data['edges_index'] > 0.034):
                                    if (data.get('edges_x_index') is None):
                                        return u'Pastry'
                                    if (data['edges_x_index'] <= 0.5359):
                                        if (data['orientation_index'] > 0.8096):
                                            if (data['edges_index'] <= 0.95235):
                                                return u'Pastry'
                                            if (data['edges_index'] > 0.95235):
                                                return u'Dirtiness'
                                        if (data['orientation_index'] <= 0.8096):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] <= 124):
                                                return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] > 124):
                                                if (data['empty_index'] > 0.32585):
                                                    if (data.get('outside_x_index') is None):
                                                        return u'Other_Faults'
                                                    if (data['outside_x_index'] <= 0.0048):
                                                        return u'Pastry'
                                                    if (data['outside_x_index'] > 0.0048):
                                                        return u'Other_Faults'
                                                if (data['empty_index'] <= 0.32585):
                                                    if (data.get('steel_plate_thickness') is None):
                                                        return u'Pastry'
                                                    if (data['steel_plate_thickness'] <= 50):
                                                        return u'Bumps'
                                                    if (data['steel_plate_thickness'] > 50):
                                                        return u'Pastry'
                                    if (data['edges_x_index'] > 0.5359):
                                        if (data['edges_x_index'] > 0.90455):
                                            if (data['edges_index'] <= 0.3711):
                                                return u'Pastry'
                                            if (data['edges_index'] > 0.3711):
                                                return u'Other_Faults'
                                        if (data['edges_x_index'] <= 0.90455):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Pastry'
                                            if (data['maximum_of_luminosity'] <= 118):
                                                if (data.get('edges_y_index') is None):
                                                    return u'Bumps'
                                                if (data['edges_y_index'] > 0.97915):
                                                    return u'K_Scatch'
                                                if (data['edges_y_index'] <= 0.97915):
                                                    return u'Bumps'
                                            if (data['maximum_of_luminosity'] > 118):
                                                if (data.get('log_y_index') is None):
                                                    return u'Pastry'
                                                if (data['log_y_index'] > 1.1751):
                                                    if (data['edges_x_index'] <= 0.79655):
                                                        return u'Pastry'
                                                    if (data['edges_x_index'] > 0.79655):
                                                        return u'Pastry'
                                                if (data['log_y_index'] <= 1.1751):
                                                    return u'K_Scatch'
                                if (data['edges_index'] <= 0.034):
                                    if (data.get('x_perimeter') is None):
                                        return u'Other_Faults'
                                    if (data['x_perimeter'] <= 18):
                                        if (data['empty_index'] > 0.27705):
                                            return u'Other_Faults'
                                        if (data['empty_index'] <= 0.27705):
                                            if (data.get('sigmoidofareas') is None):
                                                return u'Other_Faults'
                                            if (data['sigmoidofareas'] <= 0.62515):
                                                if (data.get('luminosity_index') is None):
                                                    return u'Pastry'
                                                if (data['luminosity_index'] > -0.1025):
                                                    return u'Other_Faults'
                                                if (data['luminosity_index'] <= -0.1025):
                                                    return u'Pastry'
                                            if (data['sigmoidofareas'] > 0.62515):
                                                return u'Other_Faults'
                                    if (data['x_perimeter'] > 18):
                                        return u'Pastry'
                            if (data['x_minimum'] > 1399):
                                return u'Pastry'
                if (data['orientation_index'] <= 0.48215):
                    if (data.get('luminosity_index') is None):
                        return u'Other_Faults'
                    if (data['luminosity_index'] <= -0.04986):
                        if (data.get('edges_y_index') is None):
                            return u'Other_Faults'
                        if (data['edges_y_index'] > 0.93028):
                            if (data.get('length_of_conveyer') is None):
                                return u'Bumps'
                            if (data['length_of_conveyer'] <= 1369):
                                if (data['luminosity_index'] > -0.2009):
                                    if (data.get('minimum_of_luminosity') is None):
                                        return u'Bumps'
                                    if (data['minimum_of_luminosity'] <= 88):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'Bumps'
                                        if (data['maximum_of_luminosity'] > 133):
                                            if (data.get('square_index') is None):
                                                return u'Pastry'
                                            if (data['square_index'] <= 0.6905):
                                                return u'K_Scatch'
                                            if (data['square_index'] > 0.6905):
                                                return u'Pastry'
                                        if (data['maximum_of_luminosity'] <= 133):
                                            if (data.get('empty_index') is None):
                                                return u'Bumps'
                                            if (data['empty_index'] <= 0.24175):
                                                if (data.get('square_index') is None):
                                                    return u'Bumps'
                                                if (data['square_index'] > 0.7402):
                                                    return u'Bumps'
                                                if (data['square_index'] <= 0.7402):
                                                    return u'Other_Faults'
                                            if (data['empty_index'] > 0.24175):
                                                return u'Bumps'
                                    if (data['minimum_of_luminosity'] > 88):
                                        if (data.get('steel_plate_thickness') is None):
                                            return u'Bumps'
                                        if (data['steel_plate_thickness'] > 75):
                                            if (data.get('empty_index') is None):
                                                return u'Other_Faults'
                                            if (data['empty_index'] <= 0.36645):
                                                if (data['luminosity_index'] > -0.07205):
                                                    return u'Bumps'
                                                if (data['luminosity_index'] <= -0.07205):
                                                    return u'Other_Faults'
                                            if (data['empty_index'] > 0.36645):
                                                if (data['empty_index'] > 0.4691):
                                                    return u'Z_Scratch'
                                                if (data['empty_index'] <= 0.4691):
                                                    return u'Dirtiness'
                                        if (data['steel_plate_thickness'] <= 75):
                                            if (data.get('y_maximum') is None):
                                                return u'Bumps'
                                            if (data['y_maximum'] <= 10531480):
                                                if (data['luminosity_index'] > -0.145):
                                                    if (data.get('sigmoidofareas') is None):
                                                        return u'Bumps'
                                                    if (data['sigmoidofareas'] <= 0.29075):
                                                        return u'Bumps'
                                                    if (data['sigmoidofareas'] > 0.29075):
                                                        return u'Bumps'
                                                if (data['luminosity_index'] <= -0.145):
                                                    if (data.get('log_y_index') is None):
                                                        return u'Other_Faults'
                                                    if (data['log_y_index'] <= 1.07305):
                                                        return u'Bumps'
                                                    if (data['log_y_index'] > 1.07305):
                                                        return u'Other_Faults'
                                            if (data['y_maximum'] > 10531480):
                                                return u'Other_Faults'
                                if (data['luminosity_index'] <= -0.2009):
                                    if (data.get('sum_of_luminosity') is None):
                                        return u'Other_Faults'
                                    if (data['sum_of_luminosity'] <= 18073):
                                        if (data.get('edges_x_index') is None):
                                            return u'Pastry'
                                        if (data['edges_x_index'] > 0.72475):
                                            if (data.get('sigmoidofareas') is None):
                                                return u'Other_Faults'
                                            if (data['sigmoidofareas'] <= 0.172):
                                                return u'Pastry'
                                            if (data['sigmoidofareas'] > 0.172):
                                                return u'Other_Faults'
                                        if (data['edges_x_index'] <= 0.72475):
                                            if (data['luminosity_index'] <= -0.27755):
                                                if (data['edges_x_index'] > 0.6548):
                                                    return u'Pastry'
                                                if (data['edges_x_index'] <= 0.6548):
                                                    return u'Other_Faults'
                                            if (data['luminosity_index'] > -0.27755):
                                                if (data.get('square_index') is None):
                                                    return u'Bumps'
                                                if (data['square_index'] > 0.5397):
                                                    return u'Bumps'
                                                if (data['square_index'] <= 0.5397):
                                                    return u'Pastry'
                                    if (data['sum_of_luminosity'] > 18073):
                                        return u'Other_Faults'
                            if (data['length_of_conveyer'] > 1369):
                                if (data.get('y_maximum') is None):
                                    return u'Other_Faults'
                                if (data['y_maximum'] > 66406):
                                    if (data.get('edges_index') is None):
                                        return u'Other_Faults'
                                    if (data['edges_index'] <= 0.384):
                                        if (data.get('edges_x_index') is None):
                                            return u'Other_Faults'
                                        if (data['edges_x_index'] > 0.6066):
                                            return u'Other_Faults'
                                        if (data['edges_x_index'] <= 0.6066):
                                            if (data.get('empty_index') is None):
                                                return u'Pastry'
                                            if (data['empty_index'] <= 0.34585):
                                                return u'Pastry'
                                            if (data['empty_index'] > 0.34585):
                                                return u'Other_Faults'
                                    if (data['edges_index'] > 0.384):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] > 134):
                                            if (data.get('square_index') is None):
                                                return u'Pastry'
                                            if (data['square_index'] <= 0.68055):
                                                return u'Pastry'
                                            if (data['square_index'] > 0.68055):
                                                return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] <= 134):
                                            if (data['y_maximum'] <= 3301627):
                                                if (data.get('x_maximum') is None):
                                                    return u'Other_Faults'
                                                if (data['x_maximum'] > 442):
                                                    if (data.get('edges_x_index') is None):
                                                        return u'Other_Faults'
                                                    if (data['edges_x_index'] <= 0.9129):
                                                        return u'Other_Faults'
                                                    if (data['edges_x_index'] > 0.9129):
                                                        return u'Bumps'
                                                if (data['x_maximum'] <= 442):
                                                    return u'Bumps'
                                            if (data['y_maximum'] > 3301627):
                                                return u'Bumps'
                                if (data['y_maximum'] <= 66406):
                                    if (data.get('empty_index') is None):
                                        return u'K_Scatch'
                                    if (data['empty_index'] <= 0.34835):
                                        return u'K_Scatch'
                                    if (data['empty_index'] > 0.34835):
                                        return u'Other_Faults'
                        if (data['edges_y_index'] <= 0.93028):
                            if (data.get('edges_index') is None):
                                return u'Other_Faults'
                            if (data['edges_index'] <= 0.829):
                                if (data['logofareas'] > 3.2728):
                                    return u'K_Scatch'
                                if (data['logofareas'] <= 3.2728):
                                    if (data.get('x_minimum') is None):
                                        return u'Other_Faults'
                                    if (data['x_minimum'] <= 286):
                                        if (data['luminosity_index'] > -0.054):
                                            return u'K_Scatch'
                                        if (data['luminosity_index'] <= -0.054):
                                            return u'Other_Faults'
                                    if (data['x_minimum'] > 286):
                                        if (data.get('square_index') is None):
                                            return u'Other_Faults'
                                        if (data['square_index'] > 0.9773):
                                            return u'Bumps'
                                        if (data['square_index'] <= 0.9773):
                                            if (data.get('y_maximum') is None):
                                                return u'Other_Faults'
                                            if (data['y_maximum'] <= 424411):
                                                return u'Other_Faults'
                                            if (data['y_maximum'] > 424411):
                                                if (data.get('steel_plate_thickness') is None):
                                                    return u'Other_Faults'
                                                if (data['steel_plate_thickness'] > 85):
                                                    return u'Bumps'
                                                if (data['steel_plate_thickness'] <= 85):
                                                    if (data.get('sigmoidofareas') is None):
                                                        return u'Other_Faults'
                                                    if (data['sigmoidofareas'] <= 0.9989):
                                                        return u'Other_Faults'
                                                    if (data['sigmoidofareas'] > 0.9989):
                                                        return u'Bumps'
                            if (data['edges_index'] > 0.829):
                                if (data.get('x_maximum') is None):
                                    return u'Bumps'
                                if (data['x_maximum'] > 661):
                                    if (data.get('sigmoidofareas') is None):
                                        return u'K_Scatch'
                                    if (data['sigmoidofareas'] <= 0.69885):
                                        return u'Stains'
                                    if (data['sigmoidofareas'] > 0.69885):
                                        return u'K_Scatch'
                                if (data['x_maximum'] <= 661):
                                    return u'Bumps'
                    if (data['luminosity_index'] > -0.04986):
                        if (data.get('steel_plate_thickness') is None):
                            return u'Other_Faults'
                        if (data['steel_plate_thickness'] > 55):
                            if (data['steel_plate_thickness'] <= 177):
                                if (data.get('y_maximum') is None):
                                    return u'Bumps'
                                if (data['y_maximum'] > 253695):
                                    if (data.get('edges_index') is None):
                                        return u'Bumps'
                                    if (data['edges_index'] <= 0.55195):
                                        return u'Bumps'
                                    if (data['edges_index'] > 0.55195):
                                        if (data.get('sigmoidofareas') is None):
                                            return u'Other_Faults'
                                        if (data['sigmoidofareas'] > 0.2596):
                                            return u'Other_Faults'
                                        if (data['sigmoidofareas'] <= 0.2596):
                                            return u'Bumps'
                                if (data['y_maximum'] <= 253695):
                                    if (data.get('square_index') is None):
                                        return u'Other_Faults'
                                    if (data['square_index'] <= 0.2374):
                                        return u'Bumps'
                                    if (data['square_index'] > 0.2374):
                                        return u'Other_Faults'
                            if (data['steel_plate_thickness'] > 177):
                                return u'Other_Faults'
                        if (data['steel_plate_thickness'] <= 55):
                            if (data['luminosity_index'] <= 0.13182):
                                if (data.get('x_minimum') is None):
                                    return u'Other_Faults'
                                if (data['x_minimum'] > 152):
                                    if (data.get('x_perimeter') is None):
                                        return u'Other_Faults'
                                    if (data['x_perimeter'] <= 21):
                                        if (data['orientation_index'] > -0.3205):
                                            if (data['logofareas'] <= 1.979):
                                                if (data.get('edges_index') is None):
                                                    return u'Other_Faults'
                                                if (data['edges_index'] > 0.66995):
                                                    return u'Bumps'
                                                if (data['edges_index'] <= 0.66995):
                                                    return u'Other_Faults'
                                            if (data['logofareas'] > 1.979):
                                                return u'Bumps'
                                        if (data['orientation_index'] <= -0.3205):
                                            return u'Stains'
                                    if (data['x_perimeter'] > 21):
                                        if (data['x_minimum'] > 213):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] <= 188):
                                                return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] > 188):
                                                return u'K_Scatch'
                                        if (data['x_minimum'] <= 213):
                                            if (data.get('y_maximum') is None):
                                                return u'Other_Faults'
                                            if (data['y_maximum'] <= 1009772):
                                                return u'Other_Faults'
                                            if (data['y_maximum'] > 1009772):
                                                return u'Z_Scratch'
                                if (data['x_minimum'] <= 152):
                                    if (data.get('empty_index') is None):
                                        return u'K_Scatch'
                                    if (data['empty_index'] <= 0.40005):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] > 137):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] <= 137):
                                            return u'Z_Scratch'
                                    if (data['empty_index'] > 0.40005):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'K_Scatch'
                                        if (data['maximum_of_luminosity'] > 141):
                                            if (data.get('log_y_index') is None):
                                                return u'Other_Faults'
                                            if (data['log_y_index'] <= 1.30265):
                                                return u'Other_Faults'
                                            if (data['log_y_index'] > 1.30265):
                                                return u'Z_Scratch'
                                        if (data['maximum_of_luminosity'] <= 141):
                                            if (data['luminosity_index'] <= -0.02015):
                                                return u'K_Scatch'
                                            if (data['luminosity_index'] > -0.02015):
                                                if (data.get('edges_index') is None):
                                                    return u'K_Scatch'
                                                if (data['edges_index'] > 0.1538):
                                                    if (data['empty_index'] <= 0.4975):
                                                        return u'Z_Scratch'
                                                    if (data['empty_index'] > 0.4975):
                                                        return u'K_Scatch'
                                                if (data['edges_index'] <= 0.1538):
                                                    return u'K_Scatch'
                            if (data['luminosity_index'] > 0.13182):
                                if (data.get('x_perimeter') is None):
                                    return u'K_Scatch'
                                if (data['x_perimeter'] > 19):
                                    return u'Other_Faults'
                                if (data['x_perimeter'] <= 19):
                                    return u'K_Scatch'
        if (data['typeofsteel_a4falsefalse'] == 'False'):
            if (data.get('length_of_conveyer') is None):
                return u'Bumps'
            if (data['length_of_conveyer'] <= 1361):
                if (data.get('steel_plate_thickness') is None):
                    return u'Z_Scratch'
                if (data['steel_plate_thickness'] > 90):
                    if (data.get('outside_x_index') is None):
                        return u'Other_Faults'
                    if (data['outside_x_index'] <= 0.0059):
                        if (data.get('luminosity_index') is None):
                            return u'Pastry'
                        if (data['luminosity_index'] > -0.1282):
                            if (data.get('edges_index') is None):
                                return u'Z_Scratch'
                            if (data['edges_index'] <= 0.10235):
                                return u'Other_Faults'
                            if (data['edges_index'] > 0.10235):
                                return u'Z_Scratch'
                        if (data['luminosity_index'] <= -0.1282):
                            return u'Pastry'
                    if (data['outside_x_index'] > 0.0059):
                        if (data.get('luminosity_index') is None):
                            return u'Other_Faults'
                        if (data['luminosity_index'] > -0.1854):
                            if (data.get('edges_y_index') is None):
                                return u'Bumps'
                            if (data['edges_y_index'] <= 0.92585):
                                if (data.get('empty_index') is None):
                                    return u'Other_Faults'
                                if (data['empty_index'] > 0.539):
                                    if (data.get('square_index') is None):
                                        return u'Bumps'
                                    if (data['square_index'] <= 0.39925):
                                        return u'Stains'
                                    if (data['square_index'] > 0.39925):
                                        return u'Bumps'
                                if (data['empty_index'] <= 0.539):
                                    return u'Other_Faults'
                            if (data['edges_y_index'] > 0.92585):
                                if (data.get('edges_index') is None):
                                    return u'Bumps'
                                if (data['edges_index'] > 0.042):
                                    return u'Bumps'
                                if (data['edges_index'] <= 0.042):
                                    return u'Other_Faults'
                        if (data['luminosity_index'] <= -0.1854):
                            if (data['outside_x_index'] <= 0.0144):
                                return u'Other_Faults'
                            if (data['outside_x_index'] > 0.0144):
                                if (data.get('square_index') is None):
                                    return u'Other_Faults'
                                if (data['square_index'] > 0.4783):
                                    if (data.get('logofareas') is None):
                                        return u'Bumps'
                                    if (data['logofareas'] <= 2.59175):
                                        return u'Other_Faults'
                                    if (data['logofareas'] > 2.59175):
                                        return u'Bumps'
                                if (data['square_index'] <= 0.4783):
                                    return u'Other_Faults'
                if (data['steel_plate_thickness'] <= 90):
                    if (data.get('maximum_of_luminosity') is None):
                        return u'Z_Scratch'
                    if (data['maximum_of_luminosity'] <= 140):
                        if (data.get('x_minimum') is None):
                            return u'Z_Scratch'
                        if (data['x_minimum'] > 527):
                            if (data.get('x_perimeter') is None):
                                return u'Bumps'
                            if (data['x_perimeter'] <= 16):
                                if (data.get('empty_index') is None):
                                    return u'Bumps'
                                if (data['empty_index'] > 0.3356):
                                    if (data.get('edges_index') is None):
                                        return u'Z_Scratch'
                                    if (data['edges_index'] <= 0.8575):
                                        if (data['empty_index'] > 0.39015):
                                            return u'Bumps'
                                        if (data['empty_index'] <= 0.39015):
                                            return u'Other_Faults'
                                    if (data['edges_index'] > 0.8575):
                                        return u'Z_Scratch'
                                if (data['empty_index'] <= 0.3356):
                                    return u'Bumps'
                            if (data['x_perimeter'] > 16):
                                if (data.get('orientation_index') is None):
                                    return u'Other_Faults'
                                if (data['orientation_index'] > -0.08535):
                                    if (data.get('edges_x_index') is None):
                                        return u'Z_Scratch'
                                    if (data['edges_x_index'] <= 0.74535):
                                        return u'Z_Scratch'
                                    if (data['edges_x_index'] > 0.74535):
                                        return u'Other_Faults'
                                if (data['orientation_index'] <= -0.08535):
                                    if (data['orientation_index'] <= -0.7972):
                                        return u'Bumps'
                                    if (data['orientation_index'] > -0.7972):
                                        return u'Other_Faults'
                        if (data['x_minimum'] <= 527):
                            if (data.get('y_maximum') is None):
                                return u'Z_Scratch'
                            if (data['y_maximum'] <= 2184983):
                                if (data.get('empty_index') is None):
                                    return u'Z_Scratch'
                                if (data['empty_index'] > 0.32038):
                                    return u'Z_Scratch'
                                if (data['empty_index'] <= 0.32038):
                                    if (data.get('edges_index') is None):
                                        return u'Z_Scratch'
                                    if (data['edges_index'] <= 0.6168):
                                        return u'Z_Scratch'
                                    if (data['edges_index'] > 0.6168):
                                        return u'Bumps'
                            if (data['y_maximum'] > 2184983):
                                if (data.get('edges_index') is None):
                                    return u'Z_Scratch'
                                if (data['edges_index'] > 0.07885):
                                    return u'Other_Faults'
                                if (data['edges_index'] <= 0.07885):
                                    return u'Z_Scratch'
                    if (data['maximum_of_luminosity'] > 140):
                        if (data.get('edges_y_index') is None):
                            return u'Pastry'
                        if (data['edges_y_index'] > 0.96725):
                            if (data.get('edges_index') is None):
                                return u'Pastry'
                            if (data['edges_index'] <= 0.02135):
                                if (data.get('luminosity_index') is None):
                                    return u'Pastry'
                                if (data['luminosity_index'] > 0.0037):
                                    return u'Pastry'
                                if (data['luminosity_index'] <= 0.0037):
                                    return u'Bumps'
                            if (data['edges_index'] > 0.02135):
                                return u'Pastry'
                        if (data['edges_y_index'] <= 0.96725):
                            return u'Z_Scratch'
            if (data['length_of_conveyer'] > 1361):
                if (data.get('square_index') is None):
                    return u'Bumps'
                if (data['square_index'] > 0.46824):
                    if (data.get('steel_plate_thickness') is None):
                        return u'Bumps'
                    if (data['steel_plate_thickness'] <= 92):
                        if (data['steel_plate_thickness'] > 64):
                            if (data.get('y_maximum') is None):
                                return u'Bumps'
                            if (data['y_maximum'] <= 3079675):
                                if (data.get('sum_of_luminosity') is None):
                                    return u'Bumps'
                                if (data['sum_of_luminosity'] > 9672):
                                    if (data.get('edges_x_index') is None):
                                        return u'Bumps'
                                    if (data['edges_x_index'] <= 0.5873):
                                        if (data.get('x_maximum') is None):
                                            return u'Other_Faults'
                                        if (data['x_maximum'] > 407):
                                            if (data.get('minimum_of_luminosity') is None):
                                                return u'Other_Faults'
                                            if (data['minimum_of_luminosity'] <= 100):
                                                if (data.get('log_y_index') is None):
                                                    return u'Other_Faults'
                                                if (data['log_y_index'] > 1.267):
                                                    if (data['y_maximum'] <= 1073165):
                                                        return u'Bumps'
                                                    if (data['y_maximum'] > 1073165):
                                                        return u'Other_Faults'
                                                if (data['log_y_index'] <= 1.267):
                                                    return u'Bumps'
                                            if (data['minimum_of_luminosity'] > 100):
                                                return u'Other_Faults'
                                        if (data['x_maximum'] <= 407):
                                            return u'Bumps'
                                    if (data['edges_x_index'] > 0.5873):
                                        if (data.get('minimum_of_luminosity') is None):
                                            return u'Bumps'
                                        if (data['minimum_of_luminosity'] > 68):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Bumps'
                                            if (data['maximum_of_luminosity'] <= 123):
                                                if (data['length_of_conveyer'] > 1636):
                                                    return u'Other_Faults'
                                                if (data['length_of_conveyer'] <= 1636):
                                                    if (data['length_of_conveyer'] <= 1363):
                                                        return u'Other_Faults'
                                                    if (data['length_of_conveyer'] > 1363):
                                                        return u'Bumps'
                                            if (data['maximum_of_luminosity'] > 123):
                                                if (data.get('luminosity_index') is None):
                                                    return u'Bumps'
                                                if (data['luminosity_index'] > -0.1552):
                                                    if (data['sum_of_luminosity'] <= 10597):
                                                        return u'Other_Faults'
                                                    if (data['sum_of_luminosity'] > 10597):
                                                        return u'Bumps'
                                                if (data['luminosity_index'] <= -0.1552):
                                                    return u'Bumps'
                                        if (data['minimum_of_luminosity'] <= 68):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Bumps'
                                            if (data['maximum_of_luminosity'] <= 98):
                                                return u'K_Scatch'
                                            if (data['maximum_of_luminosity'] > 98):
                                                return u'Bumps'
                                if (data['sum_of_luminosity'] <= 9672):
                                    if (data.get('outside_x_index') is None):
                                        return u'Other_Faults'
                                    if (data['outside_x_index'] <= 0.0072):
                                        if (data['length_of_conveyer'] > 1638):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] <= 138):
                                                if (data['maximum_of_luminosity'] > 122):
                                                    return u'Other_Faults'
                                                if (data['maximum_of_luminosity'] <= 122):
                                                    if (data.get('orientation_index') is None):
                                                        return u'Other_Faults'
                                                    if (data['orientation_index'] <= 0.3205):
                                                        return u'Bumps'
                                                    if (data['orientation_index'] > 0.3205):
                                                        return u'Other_Faults'
                                            if (data['maximum_of_luminosity'] > 138):
                                                return u'Bumps'
                                        if (data['length_of_conveyer'] <= 1638):
                                            if (data['length_of_conveyer'] <= 1621):
                                                if (data['outside_x_index'] > 0.00625):
                                                    return u'Bumps'
                                                if (data['outside_x_index'] <= 0.00625):
                                                    return u'Other_Faults'
                                            if (data['length_of_conveyer'] > 1621):
                                                return u'Bumps'
                                    if (data['outside_x_index'] > 0.0072):
                                        return u'Other_Faults'
                            if (data['y_maximum'] > 3079675):
                                if (data.get('minimum_of_luminosity') is None):
                                    return u'Bumps'
                                if (data['minimum_of_luminosity'] > 75):
                                    if (data['y_maximum'] <= 5773819):
                                        if (data['length_of_conveyer'] > 1647):
                                            if (data.get('empty_index') is None):
                                                return u'Bumps'
                                            if (data['empty_index'] <= 0.54155):
                                                return u'Bumps'
                                            if (data['empty_index'] > 0.54155):
                                                return u'Other_Faults'
                                        if (data['length_of_conveyer'] <= 1647):
                                            return u'Bumps'
                                    if (data['y_maximum'] > 5773819):
                                        return u'Dirtiness'
                                if (data['minimum_of_luminosity'] <= 75):
                                    if (data.get('x_maximum') is None):
                                        return u'Other_Faults'
                                    if (data['x_maximum'] <= 1587):
                                        return u'Other_Faults'
                                    if (data['x_maximum'] > 1587):
                                        return u'Bumps'
                        if (data['steel_plate_thickness'] <= 64):
                            if (data.get('orientation_index') is None):
                                return u'Bumps'
                            if (data['orientation_index'] <= 0.44155):
                                if (data.get('luminosity_index') is None):
                                    return u'Bumps'
                                if (data['luminosity_index'] > -0.3425):
                                    if (data.get('edges_index') is None):
                                        return u'Bumps'
                                    if (data['edges_index'] <= 0.89415):
                                        return u'Bumps'
                                    if (data['edges_index'] > 0.89415):
                                        if (data['square_index'] > 0.75155):
                                            return u'Bumps'
                                        if (data['square_index'] <= 0.75155):
                                            return u'Pastry'
                                if (data['luminosity_index'] <= -0.3425):
                                    return u'Pastry'
                            if (data['orientation_index'] > 0.44155):
                                if (data.get('edges_index') is None):
                                    return u'Bumps'
                                if (data['edges_index'] > 0.0929):
                                    if (data.get('sum_of_luminosity') is None):
                                        return u'Bumps'
                                    if (data['sum_of_luminosity'] <= 8398):
                                        if (data.get('edges_x_index') is None):
                                            return u'Pastry'
                                        if (data['edges_x_index'] > 0.57735):
                                            return u'Pastry'
                                        if (data['edges_x_index'] <= 0.57735):
                                            if (data['square_index'] <= 0.51665):
                                                return u'Bumps'
                                            if (data['square_index'] > 0.51665):
                                                return u'Other_Faults'
                                    if (data['sum_of_luminosity'] > 8398):
                                        return u'Bumps'
                                if (data['edges_index'] <= 0.0929):
                                    return u'Other_Faults'
                    if (data['steel_plate_thickness'] > 92):
                        if (data.get('sum_of_luminosity') is None):
                            return u'Other_Faults'
                        if (data['sum_of_luminosity'] > 8330):
                            if (data.get('x_maximum') is None):
                                return u'Other_Faults'
                            if (data['x_maximum'] <= 279):
                                if (data.get('logofareas') is None):
                                    return u'Bumps'
                                if (data['logofareas'] > 2.00605):
                                    return u'Bumps'
                                if (data['logofareas'] <= 2.00605):
                                    if (data.get('luminosity_index') is None):
                                        return u'Other_Faults'
                                    if (data['luminosity_index'] <= 0.0626):
                                        return u'Other_Faults'
                                    if (data['luminosity_index'] > 0.0626):
                                        return u'Dirtiness'
                            if (data['x_maximum'] > 279):
                                if (data.get('edges_y_index') is None):
                                    return u'Other_Faults'
                                if (data['edges_y_index'] > 0.87655):
                                    if (data.get('edges_index') is None):
                                        return u'Other_Faults'
                                    if (data['edges_index'] <= 0.6702):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] > 132):
                                            if (data.get('edges_x_index') is None):
                                                return u'Other_Faults'
                                            if (data['edges_x_index'] <= 0.6345):
                                                if (data.get('logofareas') is None):
                                                    return u'Bumps'
                                                if (data['logofareas'] > 2.08245):
                                                    return u'Other_Faults'
                                                if (data['logofareas'] <= 2.08245):
                                                    return u'Bumps'
                                            if (data['edges_x_index'] > 0.6345):
                                                return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] <= 132):
                                            return u'Other_Faults'
                                    if (data['edges_index'] > 0.6702):
                                        if (data['x_maximum'] > 1066):
                                            return u'Other_Faults'
                                        if (data['x_maximum'] <= 1066):
                                            return u'Bumps'
                                if (data['edges_y_index'] <= 0.87655):
                                    return u'Other_Faults'
                        if (data['sum_of_luminosity'] <= 8330):
                            if (data.get('logofareas') is None):
                                return u'Other_Faults'
                            if (data['logofareas'] <= 1.76335):
                                if (data.get('edges_index') is None):
                                    return u'Bumps'
                                if (data['edges_index'] > 0.4431):
                                    if (data.get('x_maximum') is None):
                                        return u'Bumps'
                                    if (data['x_maximum'] <= 921):
                                        if (data['square_index'] > 0.82855):
                                            if (data['edges_index'] <= 0.75335):
                                                return u'Pastry'
                                            if (data['edges_index'] > 0.75335):
                                                return u'Bumps'
                                        if (data['square_index'] <= 0.82855):
                                            return u'Other_Faults'
                                    if (data['x_maximum'] > 921):
                                        return u'Bumps'
                                if (data['edges_index'] <= 0.4431):
                                    if (data.get('y_maximum') is None):
                                        return u'Other_Faults'
                                    if (data['y_maximum'] <= 1530185):
                                        if (data.get('orientation_index') is None):
                                            return u'Other_Faults'
                                        if (data['orientation_index'] > 0.05555):
                                            if (data.get('empty_index') is None):
                                                return u'Bumps'
                                            if (data['empty_index'] <= 0.4979):
                                                return u'Bumps'
                                            if (data['empty_index'] > 0.4979):
                                                return u'Other_Faults'
                                        if (data['orientation_index'] <= 0.05555):
                                            return u'Other_Faults'
                                    if (data['y_maximum'] > 1530185):
                                        return u'Pastry'
                            if (data['logofareas'] > 1.76335):
                                if (data.get('orientation_index') is None):
                                    return u'Other_Faults'
                                if (data['orientation_index'] > 0.1224):
                                    if (data.get('edges_x_index') is None):
                                        return u'Pastry'
                                    if (data['edges_x_index'] <= 0.78175):
                                        if (data['length_of_conveyer'] > 1642):
                                            if (data['sum_of_luminosity'] <= 5894):
                                                return u'Pastry'
                                            if (data['sum_of_luminosity'] > 5894):
                                                return u'Other_Faults'
                                        if (data['length_of_conveyer'] <= 1642):
                                            if (data.get('maximum_of_luminosity') is None):
                                                return u'Pastry'
                                            if (data['maximum_of_luminosity'] <= 117):
                                                return u'Bumps'
                                            if (data['maximum_of_luminosity'] > 117):
                                                return u'Pastry'
                                    if (data['edges_x_index'] > 0.78175):
                                        return u'Pastry'
                                if (data['orientation_index'] <= 0.1224):
                                    return u'Other_Faults'
                if (data['square_index'] <= 0.46824):
                    if (data.get('y_maximum') is None):
                        return u'Other_Faults'
                    if (data['y_maximum'] <= 5698833):
                        if (data.get('outside_x_index') is None):
                            return u'Other_Faults'
                        if (data['outside_x_index'] > 0.0081):
                            if (data.get('sigmoidofareas') is None):
                                return u'Other_Faults'
                            if (data['sigmoidofareas'] <= 0.25005):
                                return u'Other_Faults'
                            if (data['sigmoidofareas'] > 0.25005):
                                if (data.get('minimum_of_luminosity') is None):
                                    return u'Other_Faults'
                                if (data['minimum_of_luminosity'] > 70):
                                    if (data['log_x_index'] <= 1.4548):
                                        if (data.get('maximum_of_luminosity') is None):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] > 131):
                                            return u'Other_Faults'
                                        if (data['maximum_of_luminosity'] <= 131):
                                            if (data.get('empty_index') is None):
                                                return u'Bumps'
                                            if (data['empty_index'] <= 0.456):
                                                return u'Other_Faults'
                                            if (data['empty_index'] > 0.456):
                                                if (data.get('x_maximum') is None):
                                                    return u'Bumps'
                                                if (data['x_maximum'] > 994):
                                                    return u'Bumps'
                                                if (data['x_maximum'] <= 994):
                                                    if (data['square_index'] <= 0.39375):
                                                        return u'Other_Faults'
                                                    if (data['square_index'] > 0.39375):
                                                        return u'Bumps'
                                    if (data['log_x_index'] > 1.4548):
                                        if (data.get('y_perimeter') is None):
                                            return u'Bumps'
                                        if (data['y_perimeter'] > 44):
                                            return u'Other_Faults'
                                        if (data['y_perimeter'] <= 44):
                                            return u'Bumps'
                                if (data['minimum_of_luminosity'] <= 70):
                                    if (data['square_index'] <= 0.04315):
                                        return u'Pastry'
                                    if (data['square_index'] > 0.04315):
                                        return u'Other_Faults'
                        if (data['outside_x_index'] <= 0.0081):
                            if (data.get('steel_plate_thickness') is None):
                                return u'Pastry'
                            if (data['steel_plate_thickness'] <= 69):
                                if (data['y_maximum'] > 2837454):
                                    return u'Pastry'
                                if (data['y_maximum'] <= 2837454):
                                    if (data['square_index'] <= 0.24185):
                                        return u'Pastry'
                                    if (data['square_index'] > 0.24185):
                                        if (data.get('orientation_index') is None):
                                            return u'Bumps'
                                        if (data['orientation_index'] > 0.62535):
                                            return u'Bumps'
                                        if (data['orientation_index'] <= 0.62535):
                                            return u'Pastry'
                            if (data['steel_plate_thickness'] > 69):
                                if (data.get('edges_index') is None):
                                    return u'Other_Faults'
                                if (data['edges_index'] > 0.03925):
                                    if (data['outside_x_index'] <= 0.0057):
                                        if (data.get('luminosity_index') is None):
                                            return u'Pastry'
                                        if (data['luminosity_index'] > -0.20655):
                                            if (data.get('sum_of_luminosity') is None):
                                                return u'Pastry'
                                            if (data['sum_of_luminosity'] <= 12412):
                                                return u'Pastry'
                                            if (data['sum_of_luminosity'] > 12412):
                                                if (data['steel_plate_thickness'] > 121):
                                                    return u'Pastry'
                                                if (data['steel_plate_thickness'] <= 121):
                                                    return u'Other_Faults'
                                        if (data['luminosity_index'] <= -0.20655):
                                            if (data.get('empty_index') is None):
                                                return u'Pastry'
                                            if (data['empty_index'] <= 0.3229):
                                                return u'Pastry'
                                            if (data['empty_index'] > 0.3229):
                                                if (data.get('log_y_index') is None):
                                                    return u'Bumps'
                                                if (data['log_y_index'] > 1.27815):
                                                    return u'Bumps'
                                                if (data['log_y_index'] <= 1.27815):
                                                    return u'Pastry'
                                    if (data['outside_x_index'] > 0.0057):
                                        if (data['outside_x_index'] > 0.0072):
                                            return u'Pastry'
                                        if (data['outside_x_index'] <= 0.0072):
                                            return u'Other_Faults'
                                if (data['edges_index'] <= 0.03925):
                                    return u'Other_Faults'
                    if (data['y_maximum'] > 5698833):
                        if (data.get('x_maximum') is None):
                            return u'Dirtiness'
                        if (data['x_maximum'] > 931):
                            return u'Dirtiness'
                        if (data['x_maximum'] <= 931):
                            if (data.get('outside_x_index') is None):
                                return u'Pastry'
                            if (data['outside_x_index'] <= 0.01375):
                                if (data['square_index'] > 0.27565):
                                    return u'Pastry'
                                if (data['square_index'] <= 0.27565):
                                    return u'Dirtiness'
                            if (data['outside_x_index'] > 0.01375):
                                return u'Bumps'
    if (data['log_x_index'] > 2.02965):
        if (data.get('x_minimum') is None):
            return u'K_Scatch'
        if (data['x_minimum'] > 302):
            return u'Other_Faults'
        if (data['x_minimum'] <= 302):
            if (data.get('typeofsteel_a4falsefalse') is None):
                return u'K_Scatch'
            if (data['typeofsteel_a4falsefalse'] == 'False'):
                if (data.get('empty_index') is None):
                    return u'Z_Scratch'
                if (data['empty_index'] > 0.64175):
                    if (data.get('edges_y_index') is None):
                        return u'Z_Scratch'
                    if (data['edges_y_index'] <= 0.31215):
                        return u'Bumps'
                    if (data['edges_y_index'] > 0.31215):
                        return u'Z_Scratch'
                if (data['empty_index'] <= 0.64175):
                    return u'Other_Faults'
            if (data['typeofsteel_a4falsefalse'] == 'True'):
                if (data.get('edges_index') is None):
                    return u'K_Scatch'
                if (data['edges_index'] > 0.30565):
                    return u'Other_Faults'
                if (data['edges_index'] <= 0.30565):
                    if (data.get('x_maximum') is None):
                        return u'K_Scatch'
                    if (data['x_maximum'] <= 159):
                        return u'Other_Faults'
                    if (data['x_maximum'] > 159):
                        if (data.get('y_maximum') is None):
                            return u'K_Scatch'
                        if (data['y_maximum'] > 2316792):
                            if (data['y_maximum'] <= 2622058):
                                if (data.get('length_of_conveyer') is None):
                                    return u'K_Scatch'
                                if (data['length_of_conveyer'] > 1357):
                                    return u'K_Scatch'
                                if (data['length_of_conveyer'] <= 1357):
                                    if (data.get('square_index') is None):
                                        return u'K_Scatch'
                                    if (data['square_index'] <= 0.39015):
                                        return u'Other_Faults'
                                    if (data['square_index'] > 0.39015):
                                        return u'K_Scatch'
                            if (data['y_maximum'] > 2622058):
                                return u'K_Scatch'
                        if (data['y_maximum'] <= 2316792):
                            return u'K_Scatch'