#. Write a lambda function that takes three strings as parameters and concatenates them,
# inserting a space character between each word. 

my_lam = (lambda *list1: " ".join(list1))
print(my_lam("Python", "Network", "Programming"))
#print(f"{my_lam("Python", "Network", "Programming")}")