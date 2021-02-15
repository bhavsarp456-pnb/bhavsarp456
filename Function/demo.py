def fun(name, surname, age):
    print(f"name is {name}, surname:{surname}, age:{age}, ")

def show_info(a,b,*args,role="moderator", **kwargs):
	return [a, b, args, role, kwargs]
print(show_info(1,2,3,first_name="Piyush",last_name="Bhavsar"))

def func(a,b,*args,role="moderator",**kwargs):
    return [a, b, args, role, kwargs]
print(func(1,2,3,first_name="Piyush",last_name="Bhavsar"))

names = ["John", "Jack", "Babloo", "Alice", "Piyush", "Aditi", "Abhilash"]
print(list(map(lambda name: f"The one who wins is {name}",filter(lambda value: len(value)<5,names))))

