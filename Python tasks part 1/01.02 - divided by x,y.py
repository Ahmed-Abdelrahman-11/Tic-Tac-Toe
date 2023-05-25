def divided_by(x,y):
    result = []
    for i in range(1,101):
        if i % x == 0 and i % y == 0:
            result.append(i)
    return result
