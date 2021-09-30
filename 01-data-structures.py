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

x = 5

if x < 20:
    print("Smaller")
if x > 20:
    print("Bigger")
if x == 20:
    print("Equals 20")

for i in range(5):
    print(i)

#R:
# if(x<20){
#   print("Smaller")
#}

#------------------------------------------------------------
# Building Functions
#------------------------------------------------------------

def thing():
    print("Hello")
    print("Fun")

thing()

#R:

# thing = function() {
#   print("Hello")
#   print("Fun")
# }
# thing()

#-------------------------------------------------------------
# Strings
#-------------------------------------------------------------

fruit = "banana"
letter = fruit[0]
print(letter) # first letter index is zero, not 1 (not like in R)
# also, in R, you cannot use [0] to get the letter. You need the strsub() function.

x = len(fruit)
print(x) # R: nchar(fruit)

#loop that goes through characters of fruit:

fruit = 'banana'
index = 0
while (index < len(fruit)):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# R:

# for (i in 1:nchar(fruit)){
#    print(i, strsub(fruit,i,i))
#}

s = "Monty Python"
print(s[0:4]) #note: up to but not including 4. 0,1,2 and 3. Think of it as "between separators"

#R : s[1:4]


#----------------------------------------------------------------
# Opening files
#----------------------------------------------------------------

handle = open("filename.txt", "r") #read file
print(handle) #does not print the lines, prints the type of it!
for h in handle:
    print(h)

stuff = "Hello\nWorld!"
print(stuff)

#----------------------------------------------------------------
# Lists
#----------------------------------------------------------------
friends = ['Anne', 'Betty', 'Carl']
fruits = ['Apple', 'Banana', 'Coconut']

listinlist = [1, [1,2], 3]
print(listinlist)

for l in listinlist:
    print(l)

numbers = [4, 8, 12, 36, 47, 90]
print(len(numbers))
print(range(len(numbers)))

#slicing Lists
numbers = [4, 8, 12, 36, 47, 90]
print(numbers[:3])
print(numbers[1:4])
print(numbers[-2])
print(max(numbers))

stuff = list()
stuff.append('hello!')
print(stuff)
stuff.append('gm!')
stuff.append('bye!')
print(stuff)
stuff.pop(1)
print(stuff)

stuff.sort()
print(stuff)
