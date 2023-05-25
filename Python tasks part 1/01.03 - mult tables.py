'''
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
'''
def mult_tables(x,y):
    for a in range(x,y+1):
        for i in range(1,13):
            print(f"{a} * {i} = {a*i}")
        print('----------------')
