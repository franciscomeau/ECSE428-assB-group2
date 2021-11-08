from flask import Flask, render_template, request

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""
    length = request.form['Length']
    width = request.form['Width']
    weigth = request.form['Weight']
    linearUnit = request.form['LinearUnit']
    weightUnit = request.form['WeightUnit']

    #Convert values to floats

    calLength = float(length)
    calWidth = float(width)
    calWeight = float(weigth)


    return (render_template('index.html', 
    calLength = calLength, 
    calWidth = calWidth, 
    calWeight = calWeight, 
    linearUnit = linearUnit, 
    weightUnit = weightUnit))    

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
