# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:25:18 2026

@author: indig
"""

"""
Ryne McCormick
Assignment 8
CIS 206 - Fall 2026

This was fun to research and try-and-fail at building. Creating the sorting function was pretty straight-forward once I had a way to clean up the text from the file.
The search function was a little trickier, but came out fairly simply as well. I haven't used lists like this before so it was fun to see how they can be called and used.

"""


def rows_search(rows, header, x):       # the search function, takes in three variables, the list of rows of customer info, the list of header info, and the user entered variable
    
    if x == '3': 
        cat = 1     # if user entered 3, set the new variable cat to 1, which is used later to give the place of the column to search through
        q = input("Please enter any part of a company name to perform a search: ").lower()      # lowers the input to make it match the text
    elif x == '4':
        cat = 2     # if user entered 4, set new variable cat to 2, used to give the contact column to search through
        q = input("Please enter any part of a contact name to perform a search: ").lower()
    else:
        print("Unknown error. WEIRD :O")    # covers all other x variables
        return
    
    matches = []        # new list for possible matches to return
    
    for n in rows:      # goes through each entry in the rows list
        if q in n[cat].lower():     # looks at only the set cat from earlier, and compares the text input to what's in this one category for each row, and if any of it is a match
            matches.append([n[1], n[2], n[9]])      # the new matches list gets appended with the customer info
    
    if len(matches) == 0:       # if no matches are found, returns that info
        print("No matches found.")
        return
    
    matches.insert(0, [header[1], header[2], header[9]])    # inserts the header info before the completed matches search
    for r in matches:
        for v in r:         # goes through each entry in the matches list and separates them out and formats them so it is all neat and easy to read
            print("|", f"{v:<40}", end=" ")
        print("|")
        

    
def rows_sorting(rows, header, x):      # the sorting function which takes 3 variables, the list of rows, the list of headers, and the entry of the user
    
    if x == '1':
        cat = [1, 2, 9]         # if the user enters 1 to sort by company name, set a new list to the number order 1, 2, 9 to hold the order of the columns to be returned later
    
    elif x == '2':              # if user enters 2 then set the list to 2, 1, 9 to hold the order and search by contact name later
        cat = [2, 1, 9]
    
    else:
        print("Unknown option. WEIRD! 8{D")     # if user enters anything besides 1 or 2
        return
    
    result = []         # new list for the results
    for r in rows:      # goes through each row in the rows list
        row = []        # sets the row list blank
        for c in cat:   # goes through each entry in the cat list selected earlier
            row.append(r[c])    # adds each entry to the temp row list
        result.append(row)      # adds the temp row list onto the above result list, runs until the rows list has run throgh
        
    result.sort()       # sorts the result list by the first column, having set the first one earlier lets the sort be taken care of very simply
    
    header_result = []      # blank list for the headers
    for c in cat:           # through each entry selected above
        header_result.append(header[c])     # adds the header title to the header results list
        
    result.insert(0, header_result)     # inserts the header results list at position 0, the first position
    for r in result:    # each entry in the results is going to get some formatting
        for v in r:     # for every part of each entry in the result list
            print("|", f"{v:<40}", end=" ")     # start with a wall and a space, then give 40 characters to print the entry, and instead of a new line, give a space at the end
        print("|")      # add a wall on the end of each one

    
def customer_info_clean():      # reads and copies and cleans the text from the file
    with open("Northwind_Customers.txt", "r") as customers_txt:     # with open closes the file once it's done being used, and r only reads the file
        customers = customers_txt.readlines()       # readlines takes each line from the file as a separate piece and adds them into the new list customers
    
    header = []     # the header list, to store the header entries
    rows = []       # the rows list, to store the remaining pieces of customer information
    
    titles = customers[0].strip()[1:-1].split('","')        # the new list titles is created using only the first entry in the customers list, and stripped of everything except the letters
    for t in titles:        # for each entry in the new titles list
        header.append(t.strip())        # add onto the new header list the newly stripped title
        
    for c in customers[1:]:     # for each entry in the rest of the customers list after the headers
        if c.strip() == "":     # in case any part of the text got erased and left a blank spot
            continue
        values = c.strip()[1:-1].split('","')   # strips the spaces between entries, cuts the quotes off the ends, and removes anywhere it finds a ","
        clean = []          # clean list for the new cleaned words
        for v in values:    # goes through the values list
            v = v.strip()   # strips the piece of the values list
            if v == "":     # if it strips into a blank
                v = "N/A"   # the blank becomes a string
                
            clean.append(v)     # adds the piece of the values into the clean list
        rows.append(clean)      # adds the clean list onto the finalized rows list
    return rows, header         # returns the rows and header, sorted

def main(): # the main body of the program
    
    rows, header = customer_info_clean()    # runs the cleaner on the info

    print("Press '1' to sort by Company Name")  # the main menu of our program
    print("Press '2' to sort by Contact Name")
    print("Press '3' to search by Company Name")
    print("Press '4' to search by Contact Name")
    
    while True: # loop to keep us in this until quit
            
        q = input("What would you like to do?: ")   # the input
        if q in ['1', '2']:     # if 1 or 2 it must be a sort, so run the sorting function
            rows_sorting(rows, header, q)
        elif q in ['3', '4']:   # if 3 or 4 it must be a search, so run the search function
            rows_search(rows, header, q)
        elif q in ["q", "Q", "Quit", "QUIT"]:   # or if a variety of quit options are entered, the program loop breaks and the program ends
            break
        else:       # if all else fails, ask again
            print("Please make a valid selection (Q to quit): ")
            
    
main()