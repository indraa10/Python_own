list1 = ['a','b','c','d','1','4','10']

#list to string
print("list to string: ",end=' ')
string1 = ''.join(list1)
print(string1)
print(type(string1))

# list to tuple
print("list to tuple: ",end=' ')
tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))

#list to set
print("list to set: ",end=' ')
set1 = set(list1)
print(set1)
print(type(set1))

#list to dictionary
#   https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
#   https://betterprogramming.pub/10-ways-to-convert-lists-to-dictionaries-in-python-d2c728d2aeb8

list2 = list(i for i in range(len(list1)))

dict1 = dict(zip(list1,list2))
print("list to dictionary: ",end=' ')
print(dict1)
print(type(dict1))

