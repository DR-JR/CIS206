# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:36:56 2026

@author: indig
"""

"""
Ryne McCormick
CIS 206 --- Fall 2026 --- Assignment 9

This was a lot of fun to play with lots of dicts and sets and lists, and ways to pull out items from them
as well as search through their contents. I enjoy making all of the smaller functions that do hyper-specific things
and then lining them all up to execute in order in the main body. This assignment was all sort of similar revolving around the contents of 
dicts and sets, but with many different ways of manipulating them and viewing their contents. I look forward to diving further into advanced
versions of this kind of stuff in Python in the future.
"""


import sys

python_courses = {      # the dict of sets of courses and students
"Python": {"Alice", "Bob", "Charlie", "David"},
"Database": {"Bob", "Eve", "Frank", "Alice"},
"Networking": {"Charlie", "George", "Alice"},
"Cybersecurity": {"David", "Eve", "Henry", "Charlie"}
}

def student_list(courses):  # function that creates and prints a sorted list of each unique student enrolled in the courses
    
    all_students = set()    # creates a blank set to store the student names in as duplicates will not be added this way
    
    for course, students in courses.items():    # runs through each key and list of values in the dict of courses
        for student in students:    # each value in a set of values
            all_students.add(student)   # gets added to the new set of total students
            
    print(sorted(all_students))     # finally the function prints the sorted list of students

def course_list(student, courses):  # function for returning all courses taken by a name matching one given as input
    
    student_list = []   # blank list for holding student's classes
    
    for course, students in courses.items():    # runs through the keys and values
        if student in students:     # if the input name is in the list of students in the class key
            student_list.append(course) # the course name is added to the student's class list
    return student_list     # finally the list of classes is returned

def count_students(courses):    # function for counting the number of students in a course and sorting and printing them
    
    for course, students in courses.items():    # runs through each pair of keys and values
        student_count = 0   # blank counter started at 0
        student_list = set()    # blank set for holding the list of students for courses
        for student in students:    # runs through each value in the values of each key
            student_count += 1  # ticks the counter up one
            student_list.add(student)   # adds the student to the course list
        print(course, "has", student_count, "students: ", sorted(student_list)) # prints the summary of the course. does this for each course in the dict
        
def mult_courses(courses):  # prints the students taking multiple courses together
    
    print("Students in Python and Database: \n", sorted(courses["Python"] & courses["Database"]))   # the & symbol compares the values of two keys and returns only the things in common
    print("Students in Python and Cybersecurity: \n", sorted(courses["Python"] & courses["Cybersecurity"]))
    
def one_course(courses):    # counts the number of classes each student has, and pulls together only those with one total class
    
    count = {}  # blank dict for storing our keys(students) and values(counting number of classes)
    
    for courses, students in courses.items():   # runs through each course and student
        for student in students:    # for each student in the group for each course
            if student in count:    # if the student is in the new counting dict
                count[student] += 1 # that student gets another 1 added to their course count, otherwise
            else:
                count[student] = 1  # if this is the first appearance of the student, they are automatically set to one. If this never changes, they only were enrolled in one course. Everyone else will have a greater number.
    
    one_class = set()   # blank set for storing the list of students
    for student, n in count.items():    # runs through the new counting dict of students (keys) and number of classes (values)
        if n == 1:  # if the number of classes is exactly 1
            one_class.add(student)  # they get added to the new set
            
    print("Students enrolled in one course:\n", sorted(one_class))  # returning the list of students in one class only

def main():     # the main body
    # functions to output the assignment requirements
    count_students(python_courses)
    mult_courses(python_courses)
    print("The students are:")
    student_list(python_courses)
    one_course(python_courses)
    
    while True: # while loop for the student input and exit options
        
        name = input("What student would you like to see the classes for? (Q to exit): ").title()
        
        for course, students in python_courses.items():     # runs through each course and its list of students
            if name.title() in students:    # if the input name is found in the list of students for the current course
                
                print(name, "is enrolled in the following courses:")    # outputs the name entered as being in courses
                print(course_list(name, python_courses))    # runs the function that picks out only courses with the input name enrolled in them
                break   # ends

            elif name.title() in {"Quit", "No", "N", "Q", "Exit", "X", "Leave", "Stop"}:    # list of common quit terms
                sys.exit() #  quits the program
        
        else:   # if all else fails
            print("Student not found, try again.")  # try try again
        
main()  # runs the whole circus