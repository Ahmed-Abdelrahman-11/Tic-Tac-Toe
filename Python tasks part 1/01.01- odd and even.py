'''
Create a python function that takes 2 numbers x , y and prints 2 lists containing the odd and even numbers in the x,y range
'''

def odd_even (x,y):
    odd_nums = []
    even_nums = []
    for i in range(x,y+1):
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    print(odd_nums)
    print(even_nums)
