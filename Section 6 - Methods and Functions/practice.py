'''
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()
'''

from curses.ascii import islower


mystring = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def calculate(mystring):
    lowercase_count = 0
    uppercase_count = 0

    for letter in mystring:
        if letter.islower():
            lowercase_count += 1
        elif letter.isupper():
            uppercase_count += 1
        else:
            pass

    print(f"No. of Upper case characters: {uppercase_count}\nNo. of Lower case characters: {lowercase_count}")

calculate(mystring)