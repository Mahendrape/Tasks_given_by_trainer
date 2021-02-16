# Write a 'while' loop that prints integers from zero to 5.
i = 0
while i < 10:
    print('Integers from Zero to five are {} '.format(i))
    if i == 5:
        break
    i += 1

# Write a 'while' loop that starts at the last character in the string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
string = input('Enter the string ')
while string:
    x = string[::-1]
    print('Last to first characters are {}'.format(x))
    for chr in string:
        print('Letters on a separate line are {}'.format(chr))
    break

import math
# Write a program that asks the user to enter a number and prints out all the divisors of that number.
n = int(input('Enter a number '))
for i in range(n):
    x = len([i for i in range(1, n + 1) if not n % i])
print(x)

from functools import reduce
# Write a program to calculate factorial of any given number.
Factorial = eval(input('Enter a number '))
print(' Factorial of the given number is {} '.format(math.factorial(Factorial)))

# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
x = eval(input("enter the value of x "))
y = eval(input("enter the value of y "))
print(math.gcd(x, y))

# Write a program to take integer inputs from user until he/she presses q and print the average and product of all those numbers.
# x = eval(input('Enter the value '))
# if ('The user presses the q ') !==q:


# Write a program to print whether the given number is a palindrome or not.
alpnum = input('Enter the number or string ')
if alpnum == alpnum[::-1]:
    print('It is a Palindrome')
else:
    print('It is not a palindrome ')
# Another Method
print('It is a palindrome ' if alpnum == alpnum[::-1] else 'It is not a palindrome ')
