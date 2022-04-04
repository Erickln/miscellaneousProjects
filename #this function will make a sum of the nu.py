#this function will make a sum of the number like this 1+2+3+4+5+6+7+8+9+10
def sum_of_numbers(n):
    num=0
    acum=0
    while num<=n:
        acum=acum+num
        num=num+1
    return acum

print(sum_of_numbers(10))
    