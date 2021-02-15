numbers = [1,2,3,4,5,6]
print([num for num in numbers if num % 2 == 0])
print([num*2 if num % 2 == 0 else num/2 for num in numbers])