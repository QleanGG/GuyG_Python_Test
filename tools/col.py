'''
Need to add one function:
myzip(it1 , it2) - implement zip function for 2 collections V
'''

def myzip(it1 , it2):
    # Using the zip to combine elements from two collections and putting them in a list
    result = list(zip(it1,it2))
    return result

# myzip([1,2,3], ('a','b','c'))
# myzip(['u',2,3], ('u',1,'2'))