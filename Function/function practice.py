def sum_all_num(*args):
	Total = 1
	for num in args:
		Total += num
	return Total
print(sum_all_num(1,2,3,4,5,6,7,8,9,10))

def details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key.upper()}-{value}")
details(Username="bhavsarp456@gmail.com",Password="Piyush@7523",Location="Goregaon",Phone_number=7208186114)

def show_info(a,b,*args,role="moderator", **kwargs):
	return [a, b, args, role, kwargs]
print(show_info(1,2,3,4,5,6,7,first_name="Piyush",last_name="Bhavsar"))

def My_Name(first,second):
    print(f"My name is {first} {second}.")
My_Name(first="Piyush",second="Bhavsar")

nums = [1,2,3,4,5,6,7,8,9]
gap = map(lambda x: x*2, nums)
print(tuple(gap))

my_list = [1,2,3,4,5,6]
Evens = list(filter(lambda c: c % 2 == 0,my_list))
print(Evens)
num = [1,2,3,4,5,6,7,8,9,10]
even=(lambda x: x % 2 == 0)
print(even(2))