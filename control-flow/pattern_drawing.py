size = int(input("Enter the size of the pattern: "))

if size < 0:
    print("Please input a positive integer")
else:
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("*" ,end="")
            j+=1
        i+=1
        print()