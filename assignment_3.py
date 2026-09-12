# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:32:45 2026

@author: indig

Ryne McCormick
Assignment 2
CIS206 - Fall 2026

"""

"""
This is my program from the last week's exercise but modified to meet the parameters of the new assignment.
I didn't have to change much here, just added some deeper validation checks and exception handling for the input variables.
It was fun to come up with a way for data validation, and I wonder if it can be even easier or take less space.
I am thinking python probably has some advanced built-in functions that I don't know fully yet, but am excited to
see what comes next.

"""


ORANGE = "\033[38;5;208m"
RED    = "\033[31m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
GREEN  = "\033[32m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

def main():
    
    while True: #added a while True condition to keep looping to the start until the input is correct
        try: #attempts the following sections until one of the conditions is reached, allowing for branching paths or error catching, and very useful in input validation
            w = float(input("How much do you weigh in pounds? ")) #assigning the weight variable
            if w > 0: #added a nested if condition to ensure weight is a non-negative number less than 1000
                if w < 1000: #continues if the input is between 0 and 1000. Constraint validation
                    break #this path ends successfully and the next while section begins
                else: #anything other than the if condition produces this result
                    print("Please enter a weight less than 1000 lbs.")
            else: #anything other than the if condition produces this result. Data type validation
                print("Please enter a positive integer.")
        except ValueError: #this is a catch-all for any code breaking input errors, like letters as integers. Exception handling
            print("Please enter your weight in pounds, as an integer.")
            
    while True: #same template as the section above but for a different variable
        try:
            f = float(input("How tall is your height in feet? "))
            if f > 0:
                if f < 8:
                    break
                else:
                    print("Please enter your actual height in feet.")
            else:
                print("Please enter a positive whole integer.")
        except ValueError:
            print("Please enter your height in feet as a whole integer.")
    
    f = f * 12
    
    while True:
        try:
            i = float(input("How tall is your height in inches? "))
            if i >= 0:
                if i < 12:
                    break
                else:
                    print("Please enter your height in inches (0-11)")
            else:
                print("Please enter a positive whole integer.")
        except ValueError:
            print("Please enter your height in inches as a whole integer.")
            
    h = f + i
    
    bmi = w / (h*h) * 703
    
    bmi = round(bmi, 1)
    
    print("\nYour BMI is:", bmi)
    
    if bmi < 18.5:
        print(f"{RESET}\nYou are {YELLOW}Underweight{RESET} according to the WHO.")
    elif bmi > 18.5 and bmi < 25.0:
        print(f"{RESET}\nYou are in the {GREEN}Normal Range{RESET} according to the WHO.")
    elif bmi >= 25.00:
        print(f"{RESET}\nYou are {RED}Overweight{RESET} according to the WHO.")
        
    print(f"{RESET}\n~~::{ORANGE}BMI Values Legend{RESET}::~~")
    print(f"{RESET}\n{YELLOW}Underweight{RESET}: < 18.5")
    print(f"{RESET}{GREEN}Normal Range{RESET}: 18.5 - 24.99")
    print(f"{RESET}{RED}Overweight{RESET}: >= 25.00")
    print(f"{RESET}\n{WHITE}Source{RESET}: Adapted from WHO, 1995, WHO, 2000 and WHO, 2004")

    

main()