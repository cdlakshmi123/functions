def bmi(height,weight):
    bmi2=weight/height**2
    if bmi<=18.5:
        return"underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<=30.0:
        return "overweight"
    elif bmi >30:
        return"obese"


    
        



