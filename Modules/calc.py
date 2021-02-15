# calc
import addition
import subtract

x = int(input("Num1:"))
y = int(input("Num2:"))

res1 = addition.add(x,y)
print(res1,__name__)
res2 = subtract.sub(x,y)
print(res2)

if __name__ == "__main__":
    print(f"__name__ is {__name__}")