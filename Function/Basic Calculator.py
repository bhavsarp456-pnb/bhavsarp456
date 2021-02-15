print("....Basic Calculator.....")
print("...Addition...")
print("...Subtraction...")
print("...Multiplication...")
print("...Divison...")
i = 0
while i < 4:    
    num1 = eval(input("num1:"))
    num2 = eval(input("num2:"))
    choice = int(input("Please Enter your choice:"))

    if choice == 1:
        print(f"Add:{num1 + num2}")
        i += 1
    elif choice == 2:
        print(f"Sub:{num1 - num2}")
        i += 1
    elif choice == 3:
        print(f"Mul:{num1 * num2}")
        i += 1
    elif choice == 4:
        print(f"Div:{num1 / num2}")
        i += 1
    else:
        print(f"Invalid choice")