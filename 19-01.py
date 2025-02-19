#print first 10 natural numbers using while loop?
#natural numbers-1,2,3,4,5.....
#syn for while lopp
#while condition:
     # Code to execute while the condition is True.
i = 1
while i <= 10:
    print(i)
    i+= 1
#This code sets an initial value of number to 1 and then enters a while loop.
#Inside the loop, it checks if number is less than or equal to 10.
# If that condition is true, it prints the value of number and then increments it by 1 using number += 1.
# The loop continues until number becomes greater than 10, at which point it exits.    


#.....calculate sum of all numbers from 1 t0 a given number?
#sum=n(n+1)\2--->formula 
def sum_of_numbers(n):
    return n * (n + 1) // 2  # Using the formula
#n=10
#sum=10(10+1)\2
# 10(11)/2
# 110/2
# 55
#The sum of numbers from 1 to 1 is 1
#The sum of numbers from 1 to 2 is 3
#The sum of numbers from 1 to 3 is 6
#The sum of numbers from 1 to 4 is 10
#The sum of numbers from 1 to 5 is 15
#The sum of numbers from 1 to 6 is 21
#The sum of numbers from 1 to 7 is 28
#The sum of numbers from 1 to 8 is 36
#The sum of numbers from 1 to 9 is 45
#The sum of numbers from 1 t0 10 is 55
# Calculate sum from 1 to 10
given_number =10
result = sum_of_numbers(given_number)
print(f"The sum of numbers from 1 to {given_number} is {result}")
