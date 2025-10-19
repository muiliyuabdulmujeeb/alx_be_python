FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit: float):
    celcius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius: float):
    fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


to_convert= float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

match unit:
    case "c":
        print(f"Converting {to_convert} from Celcius to Fahrenheit")
        result = convert_to_fahrenheit(to_convert)
        print(f"{to_convert}°C is {result}°F")
    case "f":
        print(f"Converting {to_convert} from Farenheit to Celcius")
        result = convert_to_celcius(to_convert)
        print(f"{to_convert}°F is {result}°C")
    case _:
        print("Please input the correct unit (C or F)")