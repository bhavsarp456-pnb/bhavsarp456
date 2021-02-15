my_string = "a0:12:90:00:80:43"
x = my_string[-11:-6:]
print(x.replace(":"," "))
print(abs(-11))
my_list = ["10","x","20.02","y",30j,"z","10","False"]

my_list.remove(30j)
print(sorted(my_list, reverse=True))