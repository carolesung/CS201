#File: assignment3.py
#Name: Carole (Chia Jung) Sung
#Email: carole07@bu.edu
#Date: Feb 7 2018
#Description: Chapter 4 Question 11, Question 13, Question 14

#Question 11
num = int(input("\nPlease enter a nonnegative integer: "))
#Uses loop to calculate the factorial of a given number
ret = 1
for x in range(2,num+1):
    ret = ret*x
print("The factorial of",num,"is:",ret)

#Question 13
print("\n")
m = 7
for i in range(7):
    for j in range(1):
        print("*"*m)
    m-=1

#Question 14
    
print("\n")
m = 0
for i in range(6):
    for j in range(1):
        print("#"+" "*m+"#")
    m += 1
