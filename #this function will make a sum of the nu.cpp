#this function will make a sum of the number like this 1+2+3+4+5+6+7+8+9+10
def sum_of_n(n):
    sum = 1
    acum =0
    while acum < n:
        sum = sum + acum
        acum = acum + 1
    return sum

    print(sum_of_n(10))