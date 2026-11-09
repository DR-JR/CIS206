# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:07:50 2026

@author: indig
"""

"""
CIS 206 - Fall 2026
Assignment 11 - Databases
Ryne McCormick

This assignment was fun for me since I have been learning SQL in another class
this semester, so to have a crossover event was pretty cool. It was very cool to 
learn how to implement Python code to run sql commands and I expect this would come
in very useful in the future for me when working with large databases.
"""

import sqlite3

EDITABLE = ["Customers", "Employees", "Products"]


def get_tables(conn):   # fetches the tables from the db

    cursor = conn.execute(  # runs an sql script to get just table names
        "SELECT name FROM sqlite_master WHERE type = 'table' "  # picks just table name field where the type is table and name is not sqlite_%
        "AND name NOT LIKE 'sqlite_%' ORDER BY name")
    tables = []     # blank list of tables to fill in
    for row in cursor:  # goes row by row for each table name
        tables.append(row[0])   # sticks each name on one by one
    return tables   # gives back the list of tables


def pick_number(prompt, highest):   # asks user to enter a number from 0 to the end of the chosen list

    while True:     # loop to wait for valid input
        choice = input(prompt).strip()  # takes just the character entered
        if choice.isdigit() and 0 <= int(choice) <= highest:    # input validation, makes sure the input was a digit, positive, and lower than the limit of the table
            return int(choice)  # gives back the valid choice input
        print(f"Please enter a number from 0 to {highest}.")    # f string for nicer formatting with the changing highest value


def pick_action():  # asks user for choice in updating deleting or inserting into the db

    while True:
        action = input("\n(I)nsert, (U)pdate, (D)elete, or Enter to go back: ").strip().upper()     # input selection, cleaned and formatted for ease of use
        if action == "":    # Enter to go back
            return ""   # Blank entry returns user
        if action in ("I", "U", "D", "INSERT", "UPDATE", "DELETE"):     # list of terms that do an action
            return action[0]    # gives back the selected action by returning the first value in the selected term
        print("Please type I, U or D (or press Enter to go back to the table list).")   # if all else fails


def show_value(value):  # pulls value out of current cell in the table
    if value is None:   # if the value is None, give it a proper blank
        return ""
    return str(value).replace("\n", " ")[:30]   # otherwise give back the value, as a string, removing any line breaks and blanks spaces and also limiting the text


def display_table(conn, table):     # shows the selected table to the user
    cursor = conn.execute(f'SELECT rowid, * FROM "{table}"')    # takes the rowid separately, and then * for everything additionally, so saving one column as permanent rowid
    columns = [col[0] for col in cursor.description][1:]   # [1:] skips rowid and 
    rows = cursor.fetchall()    # stores the table information in rows with the fetchall() command

    print(f"\n{table}")
    print("Row | " + " | ".join(columns))   # formats and joins the columns together to be readable
    for number, row in enumerate(rows, start=1):    # numbers rows startint at 1 to skip over the rowid
        print(f"{number:<3} | " + " | ".join(show_value(v) for v in row[1:]))   # gives values to all of the data points in the table row by row
    return rows, columns    # gives back rows and column names with rowids


def insert_record(conn, table, columns):    # function for adding new records
    names = []
    values = []
    print("Enter a value for each field (press Enter to skip a field):")
    for column in columns:  # input for each data point when adding a record
        value = input(f"  {column}: ").strip()
        if value:   # if the field got any value entered, keep it
            names.append(f'"{column}"')     # input validation to save a name with spaces in it
            values.append(value)    # throws the accepted value into the pile of values
    if not values:  # nothing was entered
        print("Nothing entered.")
        return

    sql = (f'INSERT INTO "{table}" ({", ".join(names)}) '   # f-string keeps this legible, insert command for the sql db using the names and values lists just built
           f'VALUES ({", ".join("?" for _ in values)})')
    try:    # error handling 
        conn.execute(sql, values)   # executes the sql and gives the entered values to fill in any ? placeholders
        conn.commit()   # saves the db
        print("Record inserted.")
    except sqlite3.Error as error:  # error catching
        print("Insert failed:", error)


def update_record(conn, table, rows, columns):  # function that changes a record
    number = pick_number("Row to update (0 to cancel): ", len(rows))    # asks which row with the max being the number of rows
    if number == 0:     # 0 to cancel
        return
    rowid = rows[number - 1][0]     # the rowid for the chosen row is -1 because lists begin at position 0

    for i, column in enumerate(columns, start=1):   # enumerate lists and numbers things, this is asking to start at 1 and number everything in columns
        print(f"  {i}. {column}")
    field = pick_number("Field to update (0 to cancel): ", len(columns)) # which field to get changed
    if field == 0: # 0 to cancel
        return

    new_value = input("New value: ").strip()
    try:    # error catching
        conn.execute(f'UPDATE "{table}" SET "{columns[field - 1]}" = ? WHERE rowid = ?',    # sql commands to update the selected table, setting the rowid for the new value
                     (new_value, rowid))
        conn.commit()   # saves the db
        print("Record updated.")
    except sqlite3.Error as error:
        print("Update failed:", error)


def delete_record(conn, table, rows):   # function for deleting records
    number = pick_number("Row to delete (0 to cancel): ", len(rows))    # asks for a row, with the limit being the number of rows
    if number == 0: # 0 to cancel
        return
    rowid = rows[number - 1][0]     # chosen row and rowid

    if input("Are you sure? (y/n): ").strip().lower() != "y":   #only y confirms delete, anything else cancels
        return
    try:    # error catching
        conn.execute(f'DELETE FROM "{table}" WHERE rowid = ?', (rowid,))    # deletes the row
        conn.commit()   # saves the db
        print("Record deleted.")
    except sqlite3.Error as error:
        print("Delete failed:", error)


def main():     # the main
    conn = sqlite3.connect("northwind.db")  # opens the db
    tables = get_tables(conn)   # takes tables and puts them in a list

    while True:     # main loop until exited
        print("\nTables:")
        for i, table in enumerate(tables, start=1):     # starting at 1, lists the tables
            print(f"  {i}. {table}")
        choice = pick_number("Choose a table (0 to quit): ", len(tables))
        if choice == 0:     # 0 to quit
            break
        table = tables[choice - 1]  # lists begin at 0 so chosen table has to -1

        while True:     # loop for table menu
            rows, columns = display_table(conn, table)  # displays the table
            if table not in EDITABLE:   # input validation
                input("\nPress Enter to return to the table list.")
                break

            action = pick_action()  # insert, update, or delete?
            if action == "":    # enter to return to list
                break
            if action == "I":
                insert_record(conn, table, columns)
            elif action == "U":
                update_record(conn, table, rows, columns)
            else:
                delete_record(conn, table, rows)

    conn.close()    # closes the db


main()  # runs the main