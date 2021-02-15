def make_upper_case(fn):
    def wrapper(*args, **kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper

@make_upper_case
def say_hello(name):
    return f"Hello, {name}"

@make_upper_case
def custom_hello(msg, name):
    return f"{msg} {name}"

@make_upper_case
def add(a,b,c):
    result = a + b + c
    return f"The result of addditing {a},{b},{c} is {result}"

print(add(10,20,25))

from time import time
def speed_test(fn):
    def wrapper(*args, **kwargs):
        print(f"Excecuting {fn.__name__} ")
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f"Total Time elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_gen(value):
    return sum(num for num in range(value))

@speed_test
def sum_list(value):
    return sum([num for num in range(value)])
@speed_test
def greet(name):
    return f"Hello {name}"

print(sum_gen(1000))
print(sum_list(1000))
print(greet("John Doe"))

help(time)

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = (meal_cost/100)*20
    tax_percent = (tax_percent/100)*20
    total_cost = meal_cost + tip_percent + tax_percent
    print(tip_percent)
    print(tax_percent)
    print(round(total_cost))

solve(12,20,8)
