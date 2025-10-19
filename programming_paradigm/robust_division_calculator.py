def safe_divide(numerator, denominator):
    try:
        numerator= float(numerator)
        denominator= float(denominator)
        result = numerator/denominator
    except ValueError:
        raise "Error: Please enter numeric values only."
    except ZeroDivisionError:
        raise "Error: Cannot divide by zero."
    except Exception:
        raise "Error performing operation"
    return f"The result of the division is {result}"