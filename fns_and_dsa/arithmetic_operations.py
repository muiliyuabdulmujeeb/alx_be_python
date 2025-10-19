def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "cannot divide by 0"
            elif num1 == 0:
                return "divide a non zero number"
            else:
                return num1/num2
        case _:
            return "please input the correct operation"