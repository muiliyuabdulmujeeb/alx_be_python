def safe_divide(numerator, denominator):
    try:
        numerator= float(numerator)
        denominator= float(denominator)
    except ValueError:
        raise Exception("Error: Please enter numeric values only.")
    

    try:
        result = numerator/denominator
    except ZeroDivisionError:
        raise Exception("Error: Cannot divide by zero.")
    return f"The result of the division is {result}"