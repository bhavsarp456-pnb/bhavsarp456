#Write a lambda function that takes a dictionary as a parameter and returns the keys of that
# dictionary in a list, sorted in reverse order (descending). 

mylamb = (lambda **kwargs: sorted(kwargs.values(), reverse=True))
print(mylamb(one=1, two=2, three=3))