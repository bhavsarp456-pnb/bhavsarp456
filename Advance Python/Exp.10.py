#Calculate the result of multiplying all the integers starting from 1 up to and including 10 using
# the reduce() function.
from functools import reduce

my_list = list(range(1,11))
Prod = reduce(lambda x,y: x*y, my_list)
print(Prod)
