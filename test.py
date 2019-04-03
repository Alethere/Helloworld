

#### Welcome to my python tutorial ####

#1 Data types

#Numbers: integer, float and booleans
valA=3
valB=4.2,4,1.2,5
valC=True,False,False,True

sum(valC) #will return 2 (T=1, F=0)

7%3 #Modulus operator, returns the remainder
3**2 #to the power of two

#All are True
1==1
1!=2
1>0
1<2
1>=1
1>=0

#some numeric functions
float(9) #returns a float
int(9.1) #returns an integer (chopping off)
sum(valB)

#data-type methods (????)
(float).is_integer()

#Strings
simple_string="text"
simple_string2="more text"
len(simple_string)
text=simple_string+" "+simple_string2
text[0:1] #returns "te" (first and second character of the string)
text.capitalize() #makes the first letter capital

#variable in text
name="John Doe"
"My name is {}".format(name)
#take out whitespaces (space and tab)


#Lists
mylist = [1,2,[1,2,3],"Hello",3]
mylist[0:2] #first second and third element
mylist[-1] #from the end
[ mylist[i] for i in [3,1,2]] #if they don't follow a specific pattern

#concatenation is not nested
fruits = ["apples", "grapes", "oranges"]
veggies = ["corn", "kale", "mushrooms"]
grocery_list = fruits + veggies
# result is
#['apples', 'grapes', 'oranges', 'corn', 'kale', 'mushrooms']

#data.type methods
list.sort() #ATTENTION overwrites THE LIST to sorted LIST
list.pop() #takes one element out. If no index is given, the last.
#only one argument allowed
list.append() #add argument at the append
list.reverse() #reverse list

#Tuples
#Similar to lists but cannot be edited after creation(?)
my_tuple = ("Michael","Herman",32,"death")
my_tuple[1] #what you can imagine
#They support concatenation
list(my_tuple) #turn tuple into list

#Dictionaries
#Very useful, they contain key:value pairs
my_dict = {"Key1":2,"Key 2":"death","pi":3.14,2:"two"}
my_dict["Key 2"] #returns death
my_dict[2] #returns 2
key="Key 2"
my_dict[key] #also returns death
