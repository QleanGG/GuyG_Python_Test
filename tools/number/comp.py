'''
complicated module-
adding two functions:
*sumofdigits - gets a number and returns sum of digits (for example 234 =>  9) V
*ispal - return True if the number is palindrome (1221 , 34543, ....) V
'''

from .simp import *

def sumofdigits(number):
    # checking for simp function calls
    if not simp_called_check():
        raise Exception("Call at least one function in simp module before using functions in comp module")
    
    #receives the sum of all digits
    sum = 0 
    str_num = str(number) # changing the number to string
    for st_digit in str_num: # looping through every digit

        #changing the digit back to an int
        digit = int(st_digit) 
        sum += digit
    
    return sum

def ispal(number):
    # checking for simp function calls
    if not simp_called_check():
        raise Exception("Call at least one function in simp module before using functions in comp module")
    
    #making the number a string
    number_str = str(number)

    #revesing the string
    revese_str = number_str[::-1]

    #changing back to num
    revese_num = int(revese_str)

    #checks if the number is the same
    if number == revese_num:
        return True
    return False
    
