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
