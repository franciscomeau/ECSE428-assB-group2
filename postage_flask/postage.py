from flask import Flask, render_template, request

Flask_App = Flask(__name__) # Creating our Flask Instance

def is_numeric(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

def errorPage():
    """ Displays the index page accessible at '/' """

    return render_template('errorPage.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""
    length = request.form['Length']
    linearUnit = request.form['LinearUnit']
    weight = request.form['Weight']
    weightUnit = request.form['WeightUnit']
    width = request.form['Width']
    widthUnit = request.form['WidthUnit']
    isStandard = False
    postalRate = -1.0
    errorMessage = ""

    # if non-Numeric then error message

    if ( 
    not(is_numeric(length)) or
    not(is_numeric(width)) or
    not(is_numeric(weight))
    ):
        errorMessage = "Error: Non-numeric characters are not allowed for Length, Width, or Weight"
        return (render_template('errorPage.html', 
            errorMessage = errorMessage
        ))

    
   
   # Convert values to floats
    
    calLength = float(length)
    calWeight = float(weight)
    calWidth = float(width) 

    # if negative inputs then error message

    if (
        calLength < 0 or
        calWidth < 0 or
        calWeight < 0
    ):
        errorMessage = "Error: Negative inputs are not allowed"
        return (render_template('errorPage.html', 
            errorMessage = errorMessage
        )) 
    

    #Conversion of inches to mm if necessary
    if linearUnit == "inches":
        calLength = calLength * 25.4

    if weightUnit == "ounces":
        calWeight = calWeight * 28.35  

    if widthUnit == "inches":
        calWidth = calWidth * 25.4

    if calLength >= 140 and  calLength <= 245 and calWidth >= 90 and calWidth <= 156 and calWeight >= 3 and calWeight <= 50:    
        isStandard = True

    if isStandard and calWeight <= 30:
        postalRate = 0.49

    if isStandard and calWeight > 30 and calWeight <= 50:
        postalRate = 0.80

    if not(isStandard) and calWeight <= 100:
        postalRate = 0.98

    if not(isStandard) and calWeight > 100 and calWeight <= 500:
        postalRate = 2.40

    # if weight over 500g then error message

    if calWeight > 500:
        errorMessage = "Error: Weight cannot be over 500g"
        return (render_template('errorPage.html', 
            errorMessage = errorMessage
        ))

    # if weight under 3g then error message

    if calWeight < 3:
        errorMessage = "Error: Weight cannot be under 3g"
        return (render_template('errorPage.html', 
            errorMessage = errorMessage
        ))  

    return (render_template('resultPage.html', 
    calLength = calLength,
    linearUnit = linearUnit,
    calWeight = calWeight,
    weightUnit = weightUnit,
    calWidth = calWidth,
    isStandard = isStandard,
    postalRate = postalRate,
    errorMessage = errorMessage
    ))    

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
