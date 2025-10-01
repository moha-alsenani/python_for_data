# First basic function
def greet():
    print("HELO?!!")
greet()

def add(a, b):
    return a + b
print(add(1, 1))

def subtract(c, d):
    return c - d
print(subtract(1, 1))

def power(e, f=2):
    return e ** f
print(power(2))

# overwriting f
print(power(2, 3))

def divide(x, y):
    if y == 0:
        return "Cannot be Divided by 0 !!"
    return x / y

print(divide(1, 2))
print(divide(1,0))
