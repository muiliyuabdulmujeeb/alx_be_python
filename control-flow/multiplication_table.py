number = int(input("Enter a number to see its multiplication table: "))


for value in range(1,11):
    result = number * value
    print(f"{number} * {value} = {result}")