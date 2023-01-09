ip = "this is it"
print("the input string is : {}".format(ip))
# string to list

l1 = list(ip)
print("string to list: ",end=' ')
print(l1)

# string to tuple 

t1 = tuple(ip)
print("string to tuple: ",end=' ')
print(t1)

# string to set

s1 = set(ip)
print("string to set: ",end=' ')
print(s1)

# string to set

input_string = '{"a":"apple" , "b":"ballon"}'

output_dict = eval(input_string)
print("string to dictionary using eval: ",end=' ')
print(output_dict)

from json import loads as jl
# use json.loads to conver from string to dictionary however use single quote (' ') in case of enclosing the string

output_dict1 = jl(input_string)
print("string to dictionary using json.loads(): ",end=' ')
print(output_dict1)
