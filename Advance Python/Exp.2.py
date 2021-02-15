# Write a list comprehension that interates over [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and multiplies with
# 10 only the elements that are less than or equal to 5.
my_list = [num*10 for num in range(1,11)]
x = []
for i in my_list:
    if i <= 50:
        x.append(i)
print(x)