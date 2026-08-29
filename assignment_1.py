# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:28:00 2026

@author: indig

Ryne McCormick
CIS206 Fall 2026
Assignment 1

"""

"""
1.

Allow a use to enter first name and last name into two separate variables. Then display the values in the order of last name, first name. 
"""

def main():
    
    first = input("Please enter your first name: ").title()
    last = input("Please enter your last name: ").title()
    
    print(last, ",", first, "\n")
    
main()

"""
2.
 
Write a program to compute and display 10 times 100 times 1000 times 10000.
"""

def main():

    a = 10*100*1000*10000
    print("10 * 100 * 1000 * 10000 =", a,"\n")

main()

"""
3.

Create a program that shows the numerical values of the Boolean true and false.
"""

def main():
    
    print("True =", int(True), "False =", int(False))

main()

"""
4.

Allow a use to enter two floating point numerical values. Display the product of the two numbers.
"""

def main():
    
    
    while True:
        num1 = input("\nEnter a decimal number: ")
        try:
            num1 = float(num1)
            break
        except ValueError:
            print("Invalid input, please enter a decimal number")
            
    while True:
        num2 = input("Enter another decimal number: ")
        try:
            num2 = float(num2)
            break
        except ValueError:
            print("Invalid input, please enter another decimal number")
            
    print("\nThe combination of your numbers is ", num1+num2)
    
main()

"""
5.

Use the type function to display the data types of a string, float and integer.
"""

def main():
    
    s = "this is a string"
    f = 3.14159
    i = 42
    
    print("\n", s, "is data type", type(s))
    print(str(f), "is data type", type(f))
    print(str(i), "is data type", type(i))
    
main()