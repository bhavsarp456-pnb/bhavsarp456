def for_man(iterable_obj):
    iterator = iter(iterable_obj)

    while True:
        try:
            i = next(iterator)
            i = i ** 2
        except StopIteration:
            break
        yield i

print(list(for_man([1,2,3,4,5])))

def map_func(func, iterable_obj):
    iterator = iter(iterable_obj)

    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)
    

my_list = []
map_func(lambda x:my_list.append(x**2),[1,2,3,4,5])
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
        return (self)

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        else:
            raise StopIteration
    
counter = Counter(10,21)
result = iter(counter)
print(f"Counter:{list(result)}")


def gen_counter(start, end ,step = 1):
    while start < end:
        yield start
        start += step
Range = gen_counter(1,11)
print(tuple(Range))

for num in gen_counter(1,21):
    print(num,end=" ")

import random
def make_greet_func(person):
    def make_message():
        msg = random.choice(["Hello","Yoo Man","What are you doing, Man!", "Welcome to RST Forum!"])
        return f"{person} {msg}"
    return make_message
greet_Piyush = make_greet_func("Piyush")
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())
print(greet_Piyush())