#Q.1)
def squared(number):
   return number ** 2

result = squared(5)
print(f"Your answer of 5 squared is {result}")












#Q.2)
def Total(num1,num2):
   return num1 + num2

result = Total(5,4)
print(f"Your answer for Sum is {result}")












#Q.3)
def mul(numb1,numb2):
   return numb1 * numb2

result_1 = mul(8,6)
result_2 = mul('A',6)
print(f"Your answer for polymorphism is {result_1}.")
print(f"Your answer for ploymorphism with string character is {result_2}.")











#Q.4)
import math 

def circle_stat(radius):
   area = math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference

a, c  = circle_stat(3)
print(f"Your answer for circle formula for Area: {round(a,2)} and for Circumference: {round(c,2)}")













#Q.5)
def greet(name = "Default User"):
   return "Hello, " + name + ' !'

print(greet("Savio"))
print(greet())
    












#Q.6)

cube = lambda x: x ** 3

print("3","X","3","X","3","=",cube(3))
print(cube(3))




















#Q7)Function with *args ----> Arguments Handler
def sum_all(*args):
   print(*args)
   for i in args:
       print(i * 2)
   return sum(args)
print(sum_all(1,2,3))















#Q.8)Functions with **kkwargs
def print_kwargs(**kwargs):
   for key, value in kwargs.items():
       print(f"{key} : {value}")

print_kwargs(name = "Spiderman", power = "Web")
print_kwargs(Superhero_name = "Savio")
print_kwargs(Superhero_name = "Savio", name = "Spiderman", power = "Web", Enemy = "Venom")

















#Q.9)Generator Function with yield
def even_generator(limit):
   for i in range(2, limit + 1, 2):
       yield i

for num in even_generator(10):
   print(num)        














#Q.10)Recursion Function
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
print(factorial(5))    