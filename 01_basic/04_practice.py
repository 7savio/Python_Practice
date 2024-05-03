# Decorators
#1) Timing Function Execution
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)    





#2) Debugging Function Calls

def debug(func):
    def wrapper_1(*args,**kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwarg_value = ', '.join(f"{k}={v}" for k , v in kwargs.items())
        print(f"calling : {func.__name__} with args {arg_value} and kwargs {kwarg_value}")
        return func(*args,**kwargs)
    return wrapper_1

@debug
def greet(name,greeting = "Hello"):
    print(f"{greeting},{name}")

greet("Savio")    






#3) Casche Return Values

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper_3(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper_3


@cache
def long_running_function(a,b):
    time.sleep(3)
    return a + b
    

print(long_running_function(2,3))    
print(long_running_function(3,4))
print(long_running_function(4,5))        