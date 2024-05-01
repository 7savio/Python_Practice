username = "Savio Fernando"

def func():
    username = "Savio"
    print(username)

print(username)
func()







x = 99

def func2(y):
    z = x + y
    return z

result = func2(101)
print(result)









def func3():
    global x
    x = 15
    print(x)
print(x)
func3()






def f1():
    #x = 56
    def f2():
        print(x)
    f2()
f1()        






#CLOSURE

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(4))
print(g(2))