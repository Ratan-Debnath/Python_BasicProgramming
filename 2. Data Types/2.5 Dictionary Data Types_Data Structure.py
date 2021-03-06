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