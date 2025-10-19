def safe_divide(numerator, denominator):
    try:
        num= float(numerator)
        den= float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    except TypeError:
        return "Error: Please enter numeric values only."
    if num and den:
        try:
            result = num/den
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {result}"