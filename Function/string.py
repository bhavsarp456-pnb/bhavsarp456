def string(x):
    return x.upper()

print(string("Piyush"))
def even_multipy(x):
    evens = [num for num in x if num % 2 == 0]
    print(evens)
    result = 1
    for number in evens:
        result *= number
    return result
print(even_multipy([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))