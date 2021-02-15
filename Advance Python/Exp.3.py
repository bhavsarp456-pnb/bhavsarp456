#Write a list comprehension that iterates over both [1, 2, 3, 4, 5] and [10, 11, 12] and
# multiplies each element of the first list with each element of the second list. 
list1 = [1,2,3,4,5]
list2 = [10,11,12]
my_list = [i*j for i in list1 for j in list2]
print(my_list)
#x = []
#for i in list1:
    #for j in list2:
        #x.append(i * j)
#print(x)
