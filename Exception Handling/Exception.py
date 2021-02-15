#exception Handling

try:
    i = 0
    while i < 4:
        def add(a,b):
            return a + b

        def sub(a,b):
            return a - b

        def mul(a,b):
            return a * b

        def div(a,b):
            return a / b

        num1 = int(input("num1:"))
        num2 = int(input("num2:"))
        choice = int(input("Please Enter your choice:"))

        if choice == 1:
            print(add(num1,num2))
            i += 1
        if choice == 2:
            print(sub(num1,num2))
            i += 1
        if choice == 3:
            print(mul(num1,num2))
            i += 1
        if choice == 4:
            print(div(num1,num2))
            i += 1
except ValueError:
    print("You have Entered Wrong Value.")
except ZeroDivisionError:
    print("Zero division is not possible, Please Check")
except:
    print("Something went wrong! Please try again.")
else:
    if choice == 1:
        print(add(num1,num2))
        i += 1
    if choice == 2:
        print(sub(num1,num2))
        i += 1
    if choice == 3:
        print(mul(num1,num2))
        i += 1
    if choice == 4:
        print(div(num1,num2))
        i += 1
finally:
    print("Program will run any how.")