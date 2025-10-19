def safe_divide(numerator, denominator):
    try:
        numerator= float(numerator)
        denominator= float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    except TypeError:
        return "Error: Please enter numeric values only."
    if numerator and denominator:
        try:
            result = numerator/denominator
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {result}"