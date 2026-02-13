"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:

"""

""" Task1"""
number1 = input("Enter the first number: ")
number2 = input("Enter the Second number: ")

Addition = int(number1) + int(number2)

number3 = input("Addition :  ")
print(Addition)

Subtraction = int(number1) - int(number2)
number4 =input("Subtraction:  ")
print(Subtraction)

Multiplication = int(number1) * int(number2)
number5 = input("Multiplication :  ")
print(Multiplication)

Division = int(number1) /int(number2)
number6 =input("Division:  ")
print(Division)