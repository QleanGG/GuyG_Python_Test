'''
simple module-
adding two functions:
*add_two_nums = adds two numbers and return the result
*sub_two_nums = subtracts two numbers and return the result
'''

simp_called = False 

# adding two numbers together
def add_two_nums(num1,num2):
    global simp_called
    simp_called = True
    return num1+num2

# subtracting two numbers
def sub_two_nums(num1,num2):
    global simp_called
    simp_called = True
    return num1-num2

#sends to comp if simp_called is true or false
def simp_called_check():
    if simp_called == True:
        return True
    else:
        return False

