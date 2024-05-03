#Loops
#Q.1)
numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
postive_count = 0
for num in numbers:
   if num > 0:
       postive_count += 1
print(f"Final Count of Postive Count: {postive_count}")        





#Q.2)
#1)
numbers_1 = 10
sum = 0
for num in range(1,numbers_1+1):
   if num % 2 == 0:
       sum +=1 
print(f"Even Numbers are {sum}")   



#2)
for i in range(1,11):
   if i % 2 == 0:
       print(i)

    




    
#Q.3)
#1)
n = 3

for a in range(1,11):
   if a == 5:
       continue
   print(n,'X',a,'=',n*a)


#2)
mul = 5
for m in range(1,11):
   if m == 5:
       continue
   mm = mul * m
   print(mm)





#Q.4)
character = input("Enter a Name to reverse: ")
reversed_char = " "
for char in character:
   reversed_char = char + reversed_char
print(f"Your Name has reversed {reversed_char}")    







#Q.5)
repeated = input("Enter a Character name: ")

for b in repeated:
   print(b)
   if repeated.count(b) == 1:
       print(f"Character is {b}")
       break    










#Q.6)
number = 5
factorial =1 

while number > 0:
   factorial = factorial * number
   number = number - 1
print(f"Factorial value of Number is {factorial}")









#Q.7)
while True:
   number = int(input("Enter a number between 1 to 10: "))

   if 1 <= number <= 10:
       print("Thanks")
       break
   else:
       print("Invalid Number, Please Try again.")











#Q.8)
number_1 = int(input("Enter a number: "))
is_prime = True

if number_1 > 1:
   for v in range(2,number_1):
       if (number_1 % v) == 0:
           is_prime = False
           break

print(is_prime)
















#Q.9)
items = ["Apple","Banana","Orange","Apple","Mango"]
unique_item = set()

for item in items:
   if item in unique_item:
       print(f"Duplicate is {item}")
       break
   unique_item.add(item)












#Q.10)
import time

wait_time = 1
attempts = 0
max_retries = 5

while attempts < max_retries:
   print("attempts",attempts + 1,"- wait time",wait_time)
   time.sleep(wait_time)
   wait_time *= 2
   attempts += 1

