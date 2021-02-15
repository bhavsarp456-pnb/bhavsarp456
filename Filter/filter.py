nums = eval(input("Enter the number:"))
even = (filter(lambda x: x % 2 != 0,nums))
print(list(even))
