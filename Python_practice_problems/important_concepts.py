# Decorators

def test1(func):
    def wrapper(*args,**kwargs):
        print("entry")
        print(func(*args,**kwargs))
        print("exit")
        return(func(*args,**kwargs))
    return wrapper

@test1
def hello(a,b):
    return a+b

hello(2,3)

# Output:
# entry
# AB
# exit

#####################################################

# Lambda with function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Output:
# 33

#####################################################

# Iterator 

data=["ineuron","code","india"]

x=iter(data)
type(x) # list iterator

print(next(x))
print(next(x))
print(next(x))

# Output:
# ineuron
# code
# india


# Generator

def square(n):
    for i in range(n):
        yield i**2
        
k=square(3)

type(k)  # generator

print(next(k))
print("#################")
for i in k:
    print(i)
    
# Output:
# 0
# #################
# 1
# 4