# Funktionen
for num in [1,2,3,4,5]:
    print(num * 2)
    
for num in [1,2,3,4,5]:
    print(num * 3)
    
for num in [1,2,3,4,5]:
    print(num * 4)


len([1,2,3])

def say_hi():
    print("hi")
    
def say_hi2(name):
    print("Hi " + name)


def say_hi3(name = "Max"):
    print("Hi " + name)
    
    
def add(x):
    return x + x

# *args and **kwargs

def add2(*args):
    return sum(args)

add2(2,3,5,6)


def sayhi4(**kwargs):
    if "name" in kwargs:
        print(f'Hi {kwargs["name"]}')
    else:
        print("Hi Unbekannter")

# Scope

x = 20

def func():
    x = 10
    print(x)

func()
print(x)


def func2():
    global x
    x = 10
    print(x)
    
func2()
