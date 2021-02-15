#Generator
#custom for loop 


def for_man(iterable_obj):
    iterator = iter(iterable_obj)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
for_man("Hello World!")

def map_func(func,iterable_obj):
    Iterator = iter(iterable_obj)
    while True:
        try:
            i = next(Iterator)
        except StopIteration:
            break
        else:
            func(i)
my_list = []
map_func(lambda x:my_list.append(x**2),[1,2,3,4])
print(my_list)

class Counter:
    def __init__(self, start = None, end = None, step = 1):
        if start == None:
            self.current = 0
            self.end = 0
        elif end == None:
            self.current = start
            self.end = start
        else:
            self.current = start
            self.end = end
        self.step = step
    
    def __iter__(self):
        #so what this return is what the iter() return
        #This need to be an iterator and not something stupid
        #return iter("Hello") #this will work, as it is iterable
        return (self) #wont work without __next__ as it is iterator yet.
    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        else:
            raise StopIteration

c = Counter(10,20)
result = iter(c)
print(f"Counter = {list(result)}")
for x in Counter(0,10 ,2):
    print(x)

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(10)
print([num for num in count_up_to(20)])

def gen_counter(start,end):
    while start < end:
        yield start
        start += 1
c = gen_counter(1,11)
print(list(c))

for num in gen_counter(1,11):
    print(num)


import random
def make_greet_func(person):
    def make_message():
        msg = random.choice(["Hello","Yoo Man","What!","Get Lost!"])
        return f"{msg}.{person}"
    return make_message
greet_abhilash = make_greet_func("Abhilash")

print(greet_abhilash())
print(greet_abhilash())
print(greet_abhilash())
print(greet_abhilash())
print(greet_abhilash())
print(greet_abhilash())
print(greet_abhilash())


def sum(n, func):
    total = 0
    for num in range(1,n+1):
        total += func(num)
    return total

def square(n):
    return n*n

def cube(n):
    return n*n*n
print(sum(3, square))
print(sum(3, cube))

def greet(person):
    def get_mood():
        mood = [
            "Hey",
            "What",
            "What the heck do you want!",
            "Get Lost"
        ]
        msg = random.choice(mood)
        return msg
    
    result = f"{get_mood()} {person}"
    return result

print(greet("John"))