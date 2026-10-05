# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:17:13 2026

@author: indig
"""

"""
Ryne McCormick
CIS 206 - Fall 2026

This file reading and writing assignment was pretty good, the articles and tutorials from 
Blackboard really helped here with the general structure, and seemed to flow easily once
I started.
"""
       
def process(name):  # the function for running through the names in the file
    
    try:        # error catching for file not found
        with open("names.txt", "r") as names_txt:   # with open closes the file automatically and makes code 
            names = names_txt.read()    # reading the list of names from the file and assigning to a local variable
            
            if name in names:   # if the string is found in the list of names read from the file
                print(f"The string '{name}' is already in the file.")
            
            else:
                with open("nofound.txt", "w"):  # writes and creates the nofound.txt file, or overwrites if it already exists
                    print(f"The string '{name}' has been written to the nofound.txt.")
                    
    except FileNotFoundError as e:
        print("Error:", e)
        
    finally:    # closes the file for sure at the end
        names_txt.close()
        
def main():
    
    while True:     # main loop for string entry or exit
        try:            # error catching for value errors
            name = input("Enter a string (or type 'exit' to quit): ").title()   # capitalize the string to match the file data
    
        except ValueError as e:
            print(f"Error: {e}")
        
        if name in ['Exit']:    # exit condition
            break
        
        else:                   # if all pass it runs through the main loop
            process(name)
            
    
main()
