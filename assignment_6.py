# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:49:15 2026

@author: indig
"""



from itertools import batched, compress, groupby, repeat # import all the iterable tools I use in the program


def ilen(iterable):     # gives back the number of items in the iterable, from the wiki
    
    """
    >>> ilen(x for x in range(1000000) if x % 3 == 0)
    333334
    """
    
    # using zip() to wrap the input with 1-tuples which compress() reads as true values.
    return sum(compress(repeat(1), zip(iterable)))


def rle_main(s):    # the rle main for determining whether to encode or decode, or if it is a valid string at all
    
    """
    >>> rle_main("AAAABBBCCDAA")
    '##00A4B3C2DA2'
    >>> rle_main("##00A4B3C2DA2")
    'AAAABBBCCDAA'
    >>> rle_main("Room 101")
    '##00Ro2m #1#0#1'
    """
    
    if not isinstance(s, str):      # catches anything that's not a string and gives a soft error
        raise TypeError("input must be a string")

    if s.startswith("##00"):        # checks if this is something to decode
        return rle_decode(s)
    
    return rle_encode(s)            # if all pass, this is a valid string to begin to encode


def rle_encode(s):  # to encode the string input into ##00 format
    
    """
    >>> rle_encode("AAAABBBCCDAA")
    '##00A4B3C2DA2'
    >>> rle_encode("##5555")
    '##00##2#54'
    """
    
    if not isinstance(s, str):      # more string validation before we try to encode
        raise TypeError("input must be a string")

    result = "##00"     # starts the encoded string so we can add on to encode
    
    for a, b in groupby(s):     # stores each entry in the string as a character and then all of the characters like that in a row
        
        n = ilen(b)   # ilen(b): length of iterable b, counts the number of characters in a row for each character entry in the string
        
        if a == "#":
            a = "##"        # a # is written as ##
            
        elif a.isdigit():
            a = f"#{a}"     # a 1 is written as #1

        if n > 1:
            result += f"{a}{n}"     # multiple characters (KKKKKKK) are written as K7
                
        else:
            result += a             # or else it is a single character and it is written to the result
            
    return result                   # gives back the finished encoded string


def split_string(s):    # splits the encoded string into list of characters and counts to work with easier in the decode function
    
    """
    >>> split_string("A4B3C2DA2")
    ['A', '4', 'B', '3', 'C', '2', 'D', '1', 'A', '2']
    
    >>> split_string("##2#54")
    ['#', '2', '5', '4']
    """
    
    pieces = []     # list to store the split parts
    i = 0           # count for the loop

    while i < len(s):   # continue loop until the whole string has been iterated through one character at a time
        
        if s[i] == "#": # trips if the first character is a #, and checks what the next character is as well
            
            if i + 1 < len(s) and (s[i + 1] == "#" or s[i + 1].isdigit()):  # as long as there is another character after the current # character, and the next character is another # or a digit, it reads the next position and 
                char = s[i + 1]   # ## gives #, #5 gives 5  # reads the first # as a pass and records the # or digit after
                i += 2            # moves the counter up twice because the decoded part was two characters long
                
            else:   # catches valueerrors from input
                raise ValueError("# must be followed by a digit or another #")
                
        elif s[i].isdigit():
            raise ValueError("a count must come after a character")
            
        else:       # the current character is stored temporarily as char to be added after checking for a count
            char = s[i]
            i += 1

        count = ""
        while i < len(s) and s[i].isdigit():    # position has moved up after storing character, and if current s[i] is a number, the count is recorded to the count string temporarily
            count += s[i]   # if the next position is a number, it is counted together until a non-number is reached, then that number is recorded as the count number for the character
            i += 1

        if count == "": # if nothing was added to the count string, it returns a 1 for the character
            count = "1"
            
        elif int(count) == 0:   # catch for 0
            raise ValueError("a count can't be 0")

        pieces.append(char)     # adds the character and count to the pieces list, building the encoded string
        pieces.append(count)

    return pieces   # returns the finished encoded list


def rle_decode(s):  # decodes an encoded string
    
    """
    >>> rle_decode("##00A4B3C2DA2")
    'AAAABBBCCDAA'
    
    >>> rle_decode("##00##2#54")
    '##5555'
    
    >>> rle_decode("A4B2")
    Traceback (most recent call last):
        ...
    ValueError: encoded string must start with ##00
    
    >>> rle_decode("##00#A")
    Traceback (most recent call last):
        ...
    ValueError: # must be followed by a digit or another #
    
    >>> rle_decode("##005A")
    Traceback (most recent call last):
        ...
    ValueError: a count must come after a character
    
    >>> rle_decode("##00A0")
    Traceback (most recent call last):
        ...
    ValueError: a count can't be 0
    """
    
    if not isinstance(s, str):
        raise TypeError("input must be a string")
        
    if not s.startswith("##00"):            # error catching for string input
        raise ValueError("encoded string must start with ##00")

    pieces = split_string(s[4:])    # starts reading the encoded string at position 4, after the ##00

    r = ""          # starts a blank string for the returned decoded string
    
    for a, b in batched(pieces, 2):     # takes two values at a time and pairs them together from the string after splitting it into pair values
        r += a * int(b)             # adds the character the number of times it should be repeated
        
    return r    # gives back the finished decoded string


def main():
    
    while True:     # while loop to keep the user in the program unless they want to exit with a blank line
        text = input("Please enter a string to encode, start with ##00 to decode, or a blank line to quit: ")

        if text == "":  # exit condition
            break

        try:    # tries the whole program cleanly in the main(), with a try/except for error catching
            print(rle_main(text).upper())
            
        except ValueError as e:
            print(f"Error: {e}")

main()
