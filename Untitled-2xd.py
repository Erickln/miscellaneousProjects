#this function will make a sum of the number like this 1+2+3+4+5+6+7+8+9+10
def ciclos():
    acum=1
    cont=1
    print("Introduce n: ")
    n=int(input())
    while cont<=n:
        acum=acum*cont
        cont=cont+1
    print("El factorial de "+str(n)+" es: "+str(acum))

ciclos()
