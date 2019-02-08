# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num1 = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num1+ 1):
       factorial = factorial*i
   print()
