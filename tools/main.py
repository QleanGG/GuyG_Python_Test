'''
Test module
can call all the functions from all modules to this program
'''

from col import *
from number import simp, comp

# checking myzip
print(myzip([1,2,3], ('a','b','c')))

#checking simp functions
print(simp.add_two_nums(6,4))
print(simp.sub_two_nums(19,17))

#checking comp functions
print(comp.ispal(232))
print(comp.ispal(1302))
print(comp.sumofdigits(5673))



