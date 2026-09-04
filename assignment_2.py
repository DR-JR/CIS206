# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:32:45 2026

@author: indig

Ryne McCormick
Assignment 2
CIS206 - Fall 2026

"""

"""
I was more focused on the presentation this time rather than proofing the
inputs for user errors. I could have spent more time with it and added in some
try/except functions but I just wanted to get something that stood on its own
feet first, and once I had the framework for it I added some colors and line
spacing so it was more legible. The colors I learned in the previous class 
for my final project, and I thought it would work nicely here for the BMI Legend.

"""


ORANGE = "\033[38;5;208m"
RED    = "\033[31m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
GREEN  = "\033[32m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

def main():
    
    w = float(input("How much do you weigh in pounds? "))
    
    f = float(input("How tall is your height in feet? "))
    
    f = f * 12
    
    i = float(input("How tall is your height in inches? "))
    
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