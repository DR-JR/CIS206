# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:18:38 2026

@author: indig
"""

"""
This assignment was about learning to use regex or regular expressions in Python. These are shortcuts to use complex functions quickly to save space and ease legibility of code.
It was great to learn there are all these features built into Python, and more all the time I'm discovering new ways to approach problems. With the use of search, match, and sub now
and understanding re syntax there are new ways of implementing data validation I can begin to think of.
"""

import re    # allows use of regular expressions


def re_01():    # problem #1
    test1 = "ABCDEFabcdef123450"    # first test string
    test2 = "*&%@#!}{"
    print("\nTESTING FOR ALPHANUMERIC ONLY CHARACTERS\n")
    for test in (test1, test2):    # iterates for each string
        if re.fullmatch(r"[A-Za-z0-9]+", test):    # as long as every character in the string is alphanumeric, it passes
            print()
            print(test, "IS ALL ALPHANUMERIC\n")
        else:    # otherwise it gets upset
            print(test, "OH NO\n")

def re_02():
    tests = ["ab", "abc", "a", "ab", "abb"]    # list of test strings for ease of testing
    print("TESTING FOR ZERO OR MORE b's\n")
    for test in tests:
        if re.fullmatch(r"ab*.*", test):    # if the test string completely matches the pattern of an a followed by 0 or more b's as indicated by the *, and then followed by 0 or more of any character, it is a match
            print(test, ": MATCH\n")
        else:
            print(test, ": NO MATCH\n")

def re_03():
    tests = ["ab", "abc", "a", "ab", "abb"]
    print("TESTING FOR ONE OR MORE b's\n")    
    for test in tests:
        if re.fullmatch(r"ab+.*", test):    # similar to the last one except b+ indicating one or more b characters
            print(test, ": MATCH\n")
        else:
            print(test, ": NO MATCH\n")

def re_04():
    tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
    print("TESTING FOR SEQUENCES OF LOWERCASE LETTERS JOINED BY UNDERSCORE\n")
    for test in tests:
        t = re.findall(r"[a-z]_[a-z]", test)    # assigns a variable to hold found sequences, findall looks for any instance in the test string for a lowercase letter followed by an underscore followed by a lowercase letter. This excludes the middle test string which has an uppercase next to the underscore
        print(test, " SEQUENCES : ", t)

def re_05():
    test1 = "The quick brown fox jumps over the lazy dog."
    test2 = " The quick brown fox jumps over the lazy dog."
    print("\nTESTING FOR MATCHING WORD AT BEGINNING OF STRING\n")
    if re.match(test1.strip(), test2.strip()):    # strip removes any leading or trailing white spaces on a string, making the two string identical, and the match is a success
        print(test1, "\n-MATCHES-\n", test2.strip())
    else:
        print("OH NO")
        
def re_06():
    tests = ["The quick brown fox jumps over the lazy dog.", "Python Exercises"]
    print("\nTESTING FOR MATCHING A WORD WITH LETTER z\n")
    for test in tests:
        w = re.search(r"\w*z\w*", test)    # giving variable w the results of a search for any word containing z as denoted by \w matching a word character with 0 or more characters in it before the letter we want, and 0 or more characters making up the word after the letter we want
        if w:    # when there is a result found in the search we print it
            print("The word wound was :", w.group())
            
def re_07():
    test = "216.08.094.196"
    print("\nTEST TO REMOVE LEADING ZEROES FROM AN IP ADDRESS\n")
    ip_removed = re.sub(r"\b0+(\d)", r"\1", test)    # sub takes the pattern of anything matching a start of any number of zeroes, then the digit after the final zero becomes the value. this lets 000 beocme 0 and leaves 100 as is
    print(test, "becomes:\n")
    print(ip_removed)

def re_08():
    text = "The quick brown fox jumps over the lazy dog."    # the test text
    words = ["fox", "dog", "horse"]           # the list of words to search for
    print("\nTEST TO SEARCH FOR LITERAL STRINGS IN STRINGS\n")
    print(text, "\n")

    for word in words:
        if re.search(word, text):    # search looks for the first value in the second, in this case it goes through each word in the list of search terms and searches for that in the test sentence
            print(f"Searching for '{word}': MATCH")    # f strings make formatting easier with variable use
        else:
            print(f"Searching for '{word}': NO MATCH")

def re_09():
    text = "The quick brown fox jumps over the lazy dog."
    words = "fox"
    print("\nTEST TO SEARCH FOR LITERAL STRINGS IN STRINGS AND POSITIONS\n")
    print(text, "\n")
    
    w = re.search(words, text)    # variable given to the result of a search for a word in the sentence, and if true it continues
    if w:
        print(f"FOUND '{words}' AT POSITION {w.start()} to {w.end()}")    # w.start() is the index position it begins at and w.end() is where the index ends

def re_10():
    test1 = "Regular Expressions"
    test2 = "Code_Examples"
    print("\nTEST TO REPLACE WHITESPACE WITH AN UNDERSCORE, AND VICE VERSA\n")
    print(test1)
    print(test2)
    print("\nBECOMES\n")
    print(re.sub(" ", "_", test1))    # sub replaces the first with the second characters
    print(re.sub("_", " ", test2))

def re_11():
    test = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    print("\nTEST TO EXTRACT DATE FROM A URL\n")
    print(test)
    
    d = re.search(r"/(\d{4})/(\d{1,2})/(\d{1,2})/", test)    # searches for any pattern matching a / followed by 4 digits and another / then one or two digits and another / and another two digits and a /
    if d:
        y, m, d = d.groups()    # groups is carrying the three parts of the date captured in the search, and are assigned to y, m, d to be used easily in output
        print("\nThe date in the url is", y, m, d)
    
def re_12():
    test = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    print("\nTESTING TO FIND ALL WORDS STARTING WITH a OR e\n")
    print(test)
    print("\nTHE WORDS BEGINNING WITH a OR e WERE:\n")
    print(re.findall(r"\b[ae]\w*", test, flags=re.IGNORECASE))    # findall looks through everything for the pattern of \b a boundary beginning with [ae] an a or an e, being a word of some length \w*, and IGNORECASE allows upper or lowercase words to be caught

def re_13():
    test = "Python Exercises, PHP exercises."
    print("\nTESTING TO REPLACE SPACE COMMA OR DOT WITH COLON\n")
    print(test)
    print("\nTHE NEW SENTENCE:\n")
    print(re.sub(r"[ ,.]", ":", test))    # this takes any instance of a space comma or dot and replaces it with a colon using the sub feature 

def re_14():
    test = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    print("\nTESTING TO FIND ALL WORDS STARTING WITH a OR e\n")
    print(test)
    print("\nTHE WORDS BEGINNING WITH a OR e WERE:\n")
    print(re.findall(r"\b[ae]\w*", test, flags=re.IGNORECASE))    # this seems like a repeat of problem 12

def re_15():
    test = "Python      Exercises"
    print("\nTESTING TO REMOVE MULTIPLE SPACES FROM A STRING\n")
    print(test)
    print("\nTHE NEW STRING:\n")
    print(re.sub(r" +", " ", test))    # this sub takes any instance of multiple blank spaces in a row and replaces them with a single blank space

def main():
    
    re_01()
    re_02()
    re_03()
    re_04()
    re_05()
    re_06()
    re_07()
    re_08()
    re_09()
    re_10()
    re_11()
    re_12()
    re_13()
    re_14()
    re_15()
main()
