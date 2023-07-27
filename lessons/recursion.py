#recursion
print("Recursion")
def factorial(n):
    
    if n == 1: return 1
    return n * (n-1)

print(factorial(7))

#decorators
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("After")
        return val
    return wrapper

@logtime
def hello():
    print("hello")
    
hello()