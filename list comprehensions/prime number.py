num = int(input("num:"))

print([num for num in range(2,num) if all(num % y != 0 for y in range(2,num))])
