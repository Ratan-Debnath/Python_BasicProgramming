"""
Python provides various standard data types that define the storage method on each of them.
The data types defined in Python are given below.
1.Numbers 2.String 3.List 4.Tuple 5.Dictionary
"""
#Python provides 4 numeric data.(int,long,float,complex) to show [Number]
integerNumber = 5 #variableName = value [variable declere syntex]
largeNumber = 90809080
floatNumber: float = 10.5
complexNumber: complex = 2.0 + 2.3j
print(type(integerNumber))
print(type(largeNumber))
print(type(floatNumber))
type(complexNumber)

#String means sequence of characters
greating : str = 'Welcome to programming world!' #possible define with data type
first = "Hello, Ratan."
second = 'How are you!'
print(first[0:5]) #print 0 to 4 index value
print(first[8]) #print value which is index 8
print(first[0:]) # print first to last value
print(first[:7]) #print first 6 degit value
print(first*2) #string show twitch
print(first+second) #add two string values

#list :(elements and size can be changed,) Lists are similar to arrays in C. However; the list can contain data of different types.
#  The items stored in the list are separated with a comma (,) and enclosed within square
# brackets [].  content from javapoint website
listValue  = [1, "hi", "python", 2]
listUpdate = [100,200,300, "hello"]
print(listUpdate)
listUpdate[0] = [123] # updated value
print(listUpdate)
print (listValue[3:])
print (listValue[0:2])
print (listValue)
print (listValue + listValue)
print (listValue * 3)

#tuple similar to the list. but cannot be updated and use () not []
tupleVar = (100,200,300, "number")
print(tupleVar)
#tupleVar[0] = (123, "value") # Error
print(tupleVar)

#Dictionary is an ordered set of a key-value pair of items. It is like an associative
# array or a hash table where each key stores a specific value
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict['one']) # Prints value for 'one' key
print(dict[2]) # Prints value for 2 key

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(tinydict) # Prints complete dictionary
print(tinydict.keys()) # Prints all the keys
print(tinydict.values()) # Prints all the values







