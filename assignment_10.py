# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:18:38 2026

@author: indig
"""

import re


def re_01():
    test1 = "ABCDEFabcdef123450"
    test2 = "*&%@#!}{"

    for test in (test1, test2):
        if re.fullmatch(r"[A-Za-z0-9]+", test):
            print()
            print(test, "is all alphanumeric\n")
        else:
            print(test, "OH NO\n")

def re_02():
    tests = ["ab", "abc", "a", "ab", "abb"]
    print("TESTING FOR ZERO OR MORE b's\n")
    for test in tests:
        if re.fullmatch(r"ab*.*", test):
            print(test, ": MATCH\n")
        else:
            print(test, ": NO MATCH\n")

def re_03():
    tests = ["ab", "abc", "a", "ab", "abb"]
    print("TESTING FOR ONE OR MORE b's\n")
    for test in tests:
        if re.fullmatch(r"ab+.*", test):
            print(test, ": MATCH\n")
        else:
            print(test, ": NO MATCH\n")

def re_04():
    tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
    print("TESTING FOR SEQUENCES OF LOWERCASE LETTERS JOINED BY UNDERSCORE\n")
    for test in tests:
        t = re.findall(r"[a-z]_[a-z]", test)
        print(test, " SEQUENCES : ", t)

def re_05():
    test1 = "The quick brown fox jumps over the lazy dog."
    test2 = " The quick brown fox jumps over the lazy dog."
    print("\nTESTING FOR MATCHING WORD AT BEGINNING OF STRING\n")
    if re.match(test1.strip(), test2.strip()):
        print(test1, "\n-MATCHES-\n", test2.strip())
def re_06():
    tests = ["The quick brown fox jumps over the lazy dog.", "Python Exercises"]
    print("\nTESTING FOR MATCHING A WORD WITH LETTER z\n")
    for test in tests:
        w = re.search(r"\w*z\w*", test)
        if w:
            print("The word wound was :", w.group())
def re_07():
    test = "216.08.094.196"
    print("\nTEST TO REMOVE LEADING ZEROES FROM AN IP ADDRESS\n")
    ip_removed = re.sub(r"\b0+(\d)", r"\1", test)
    print(test, "becomes:\n")
    print(ip_removed)

def re_08():
    text = "The quick brown fox jumps over the lazy dog."
    words = ["fox", "dog", "horse"]
    print("\nTEST TO SEARCH FOR LITERAL STRINGS IN STRINGS\n")
    print(text, "\n")

    for word in words:
        if re.search(word, text):
            print(f"Searching for '{word}': MATCH")
        else:
            print(f"Searching for '{word}': NO MATCH")

def re_09():
    text = "The quick brown fox jumps over the lazy dog."
    words = "fox"
    print("\nTEST TO SEARCH FOR LITERAL STRINGS IN STRINGS AND POSITIONS\n")
    print(text, "\n")
    
    w = re.search(words, text)
    if w:
        print(f"FOUND '{w.group()}' AT POSITION {w.start()} to {w.end()}")

def re_10():
    test1 = "Regular Expressions"
    test2 = "Code_Examples"
    print("\nTEST TO REPLACE WHITESPACE WITH AN UNDERSCORE, AND VICE VERSA\n")
    print(test1)
    print(test2)
    print("\nBECOMES\n")
    print(re.sub(" ", "_", test1))
    print(re.sub("_", " ", test2))

def re_11():
    test = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    print("\nTEST TO EXTRACT DATE FROM A URL\n")
    print(test)
    
    d = re.search(r"/(\d{4})/(\d{1,2})/(\d{1,2})/", test)
    if d:
        y, m, d = d.groups()
        print("\nThe date in the url is", y, m, d)
    
def re_12():
    test = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    print("\nTESTING TO FIND ALL WORDS STARTING WITH a OR e\n")
    print(test)
    print("\nTHE WORDS BEGINNING WITH a OR e WERE:\n")
    print(re.findall(r"\b[ae]\w*", test, flags=re.IGNORECASE))

def re_13():
    test = "Python Exercises, PHP exercises."
    print("\nTESTING TO REPLACE SPACE COMMA OR DOT WITH COLON\n")
    print(test)
    print("\nTHE NEW SENTENCE:\n")
    print(re.sub(r"[ ,.]", ":", test))

def re_14():
    test = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    print("\nTESTING TO FIND ALL WORDS STARTING WITH a OR e\n")
    print(test)
    print("\nTHE WORDS BEGINNING WITH a OR e WERE:\n")
    print(re.findall(r"\b[ae]\w*", test, flags=re.IGNORECASE))

def re_15():
    test = "Python      Exercises"
    print("\nTESTING TO REMOVE MULTIPLE SPACES FROM A STRING\n")
    print(test)
    print("\nTHE NEW STRING:\n")
    print(re.sub(r" +", " ", test))

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