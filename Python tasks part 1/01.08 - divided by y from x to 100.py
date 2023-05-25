'''
Create a function that takes x,y and prints all the number that can be divide by y from x to 100
'''
def divided_by(x,y):
    result = []
    for i in range(x,101):
        if i % y == 0 :
            result.append(i)
    return result

def divided_by2 (x,y):
    return [i for i in range(x,101) if i % y == 0 ]
