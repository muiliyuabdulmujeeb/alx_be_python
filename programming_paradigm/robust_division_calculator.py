def safe_divide(numerator, denominator):
    try:
        numerator= float(numerator)
        denominator= float(denominator)
    except ValueError:
        raise print("Error: Please enter numeric values only.")
    
    if numerator and denominator:
        try:
            result = numerator/denominator
        except ZeroDivisionError:
            raise print("Error: Cannot divide by zero.")
        print(f"The result of the division is {result}")