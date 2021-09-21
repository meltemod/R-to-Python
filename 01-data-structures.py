# -*- coding: utf-8 -*-
"""
R-to-Python
Meltem odabas

01 - Data Structures Cheat Sheet
"""

#-----------------------------------------------------------------------
# Assigning variables, variables types,  print() function & indexing
#-----------------------------------------------------------------------

#Let's start with printing 'Hello World'
print('Hello World')

#assigning values with '=' *similar to R; but '<-' does not work as it does in R.
x = 'Hello Jupyter'
print(x)

#mathematical equations are similar to that of R.
y = 3 * 7
print(y)

#note that if you do not call print(y) and rather say y; IT WILL NOT PRINT! (different from R)
z = 24/4
z

#change the assign value by mathematical operations (similar to R)
y = y + 1
print(y)

#in text, you can use '+' as if you are using `paste0` function in R (Different from R)
mo = 'Meltem'
mo = mo + ' ' + 'Odabas'
print(mo)

#Print multiple elements together (different from R; you do not need `paste` function)
print('Greetings! My name is ', mo)

#indexing a string. Indexing starts at zero! (different from R)
#this way you can use -1 to refer to the last character!
print(mo[0]) #First letter. in R, mo[1]
print(mo[-1]) #last letter in R, mo[length(mo)]

#numbers. there are different versions: float, integer. Float takes more memory so if you do not have decimals use integer.
#Note: to check the element type, use function `type()` (different from R. in R we use `class()`)
a = 1
type(a) #integer

b = 1.2
type(b) #float

#Boolean -- binary values indicating Ture or False.
is_true = True
#or
y == 22 #output is boolean
type(y == 22) #bool

#------------------------------------------------------------
# Data Structures: list, tuple, set, dictionary
#------------------------------------------------------------

#Note: I almost never used tuple or dictionary or set in R. Go figure!

#list of characters
lc = ['a', 'b', 'c'] #in R: lc = c('a','b','c')
print(lc) #in R: lc
lc[0] #in R: lc[1]

#list of numbers
ln = [1, 4, 7]
print(ln) #in R: ln
ln[0] #in R: ln[1]

#length of list
len(ln) #in R: length(ln)

#can an element have length?
len(mo) #text has length
len(y) #numeric values do not have length

#can you make a list of mixed element types (not possible in R) in Python?
#the answer is: YES!
my_list = ['a', 94875, 'fly me to he moon!!!', 6.24]
print(my_list)

#Tuples: list that are not changable. Use parantheses instead of brackets
my_tuple = (2,4)
#Tuples are immutable
my_list[-1] = 'change the last item to this please'
print(my_list)
my_tuple[-1] = 8 #TypeError: 'tuple' object does not support item assignment

#Set: no multiples of the same value. Use curly brackets
my_set = {'a','a','a','b'}
print(my_set)

#Dictionary: we see them in json files as in list of dictionaries!
dictionary_of_definitions = {"meltem" : "Best name in the world.",
                             "odabas" : "Not the best last name in the world but it is my last name so I like it."}

print(dictionary_of_definitions["meltem"])

json_file_text = [
    {
    "name" : "Meltem",
    "age" : "34",
    "gender" : "Female"
    },
    {
     "name" : "John",
     "age" : "30",
     "gender" : "Male"
     }
    ]

#------------------------------------------------------------
# Conditionals (if) & Loops (for)
#------------------------------------------------------------

#test
