# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:32:45 2026

@author: indig

Ryne McCormick
Assignment 4
CIS206 - Fall 2026

"""

"""
This is the new version of the BMI program, with some sections removed in favor of newer data/input validation methods.
Gone are the catch-all try/except paths, instead replaced by some while and if loops, with an exit built in at any time.
Building the BMI table was challenging and required me to go over some of my old programs from the spring on iterating tables
with for loops and ranges, so it's good to dust off the cobwebs. I enjoyed this week's excercise and look forward to the next
challenge!

"""

import sys # this adds the sys module to allow an easy exit code to be used

ORANGE = "\033[38;5;208m"
RED    = "\033[31m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
GREEN  = "\033[32m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

def bmi_table(): # a separate function for creating the bmi table so to make some of the code neater
    
    height_list = list(range(58, 77, 2))    # populates a list with the range of heights we want
    weight_list = list(range(100, 251, 10)) # populates a list with the range of weights we want
    
    print(f"{'Wt\\Ht':<8}", end="") # formats the output to 8 spaces to keep everything neat, overrides the default print() command to create a new line and instead keep going with end=()
    for h in height_list:   # iterates as many times as there are variables in the list
        print(f"{h:<8}", end="")    # prints the current height, formatted to 8 spaces, and keeps the line going
    print() # new line for formatting
    
    for dash in range(len(height_list) +1): # counts the number of variables in the height list, and adds 1 since python starts at 0 and we want this to cover all the columns
        print("-" * 8, end="")  # prints a dash 8 times for each variable in the height list + 1, because our outputs are formatted to 8 spaces this covers each column neatly
    print() # new line for formatting
    
    for w in weight_list:   # iterates a number of times equal to the variables in the weight list
        print(f"{w:<8}", end="")    # prints current weight, formatted to 8 spaces, keeps line going
        for h in height_list:   # while on the current weight, run through every item in the height list and perform the following function
            print(f"{w / (h*h) * 703:<8.1f}", end="")   # for every weight and height in the lists, performs the bmi calculation and formats to one decimal place and 8 spaces for neat organization
        print()

def main(): #the main body
        
    while True: # continues the main program until it is exited manually
    
        w = input("How much do you weigh in pounds?: ") #assigning the weight variable
        
        while True: #added a while True condition to keep looping to the start until the input is correct
            
            if w.isalpha(): #checks the input to be alphanumeric and if so continues to the next if
                if w.title() in ("Quit", "Q", "Leave", "Exit", "No", "N", "End"):    #   The list of quit commands
                    sys.exit()  # using the sys module to quit the program
                else:   # if the input is alphanumeric but is not in the list of quit words the following input suggests quitting, but you are also still able to enter your weight
                    w = input("I didn't catch that. If you'd like to quit, please type the letter Q: ")
                    
            else:   # if the input is not alphanumeric the loop continues to this section
                try:    #the loop tries the following code to see if it is a usable variable
                    
                    if float(w) > 0: #added a nested if condition to ensure weight is a non-negative number less than 1000
                        if float(w) < 1000: #continues if the input is between 0 and 1000. Constraint validation
                            w = float(w)    # floats the input
                            w = round(w, 1) # rounds the float to one decimal place
                            break #this path ends successfully and the next while section begins
                        else: #anything other than the if condition produces this result
                            w = input("Please enter a weight less than 1000 lbs: ") #continues asking for valid weight
                    else: #anything other than the if condition produces this result. Data type validation
                        w = input("Please enter a positive integer: ")  #continues asking for positive numbers
                except ValueError:  # any other errors get handled with this input loop
                    w = input("Please enter your weight in pounds: ")
                
            
        f = input("How tall is your height in feet?: ")   #asks for the user's height in feet 
        
        while True: #stays in this section until it is exited
    
            if f.isalpha(): # same alphanumeric checking as above
                if f.title() in ("Quit", "Q", "Leave", "Exit", "No", "N", "End"):
                    sys.exit()
                else:
                    f = input("I didn't catch that. If you'd like to quit at any time, please type the letter Q: ")
                    
            else:   #same concept as above, but with int instead of float
                try:
                    if int(f) > 0:  # since we want a whole number, we try to convert the input to an int class, if it works and it is greater than zero and less than 8, it is successful input
                        if int(f) < 8:
                            break
                        else:
                            f = input("Please enter your actual height in feet: ")
                    else:
                        f = input("Please enter a positive whole integer: ")
    
                except ValueError:
                    f = input("Error, input not recognized. Please enter your height in feet: ")
    
        i = input("How tall is your height in inches? ")    # same idea as the height in feet
        
        while True:
    
            if i.isalpha():
                if i.title() in ("Quit", "Q", "Leave", "Exit", "No", "N", "End"):
                    sys.exit()
                else:
                    i = input("I didn't catch that. If you'd like to quit at any time, please type the letter Q: ")
                    
            else:
                try:
                    if int(i) >= 0:
                        if int(i) < 12:
                            break
                        else:
                            i = input("\nPlease enter your height in inches (0-11): ")
                    else:
                        i = input("\nPlease enter a positive whole integer: ")
            
                except ValueError:
                    i = input("\nUnrecognized characters, please enter your height in inches: ")
                    
        f = float(f)    #re-declaring the variables to be exactly what I need to calculate with later
        i = float(i)
        w = float(w)
        
        f = f * 12  # converting feet to inches
                    
        h = f + i   # creating the height in inches
        
        bmi = w / (h*h) * 703   #calculating the bmi
        
        bmi = round(bmi, 1) # rounding the results
        
        print("\nYour BMI is:", bmi) # returning the results
        
        if bmi < 18.5: # tells the user which category they fall into
            print(f"{RESET}\nYou are {YELLOW}Underweight{RESET} according to the WHO.")
        elif bmi > 18.5 and bmi < 25.0:
            print(f"{RESET}\nYou are in the {GREEN}Normal Range{RESET} according to the WHO.")
        elif bmi >= 25.00:
            print(f"{RESET}\nYou are {RED}Overweight{RESET} according to the WHO.")
            
        print(f"{RESET}\n~~::{ORANGE}BMI Values Legend{RESET}::~~") #legend for the bmi
        print(f"{RESET}\n{YELLOW}Underweight{RESET}: < 18.5")
        print(f"{RESET}{GREEN}Normal Range{RESET}: 18.5 - 24.99")
        print(f"{RESET}{RED}Overweight{RESET}: >= 25.00")
        
        bmi_table() # runs the bmi_table function at the start to produce the full table
        
        print(f"{RESET}\n{WHITE}Source{RESET}: Adapted from WHO, 1995, WHO, 2000 and WHO, 2004")

        while True: # starts a continue/exit choice loop
            choice = input("\nWould you like to calculate your BMI again? (Y/N): ").strip().title() # takes input and reduces it to just the characters typed, removes spaces, capitalizes first letter
            if choice in ("Y", "N"): # if the input is valid we continue
                break   # exits this if loop on success
            print("\nDidn't catch that, would you like to go again? (Y/N): ") # keeps asking for valid input

        if choice == "N":   # if N is entered, the program finally ends, but if Y is entered it goes right back to the top
            break
        
    print("\nThank you for using this calculator :)")
    
main()