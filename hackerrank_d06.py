##hacker rank day 6
num_test_case=int(input("Enter number of test case: "))
T=num_test_case+1

for i in range(1,T):
    input_string=input("Enter the string: ")
    even_index_char=''
    odd_index_char=''
    for j in range(len(input_string)):
        if j%2==0:
            even_index_char=even_index_char+input_string[j]
        else:
            odd_index_char=odd_index_char+input_string[j]
    print(even_index_char + " " + odd_index_char)