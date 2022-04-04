import time
from multiprocessing import Process, Lock, Value, Event
import random
import os
def sell(lock,event,Num,total,totalVendidas):
    proc_id = os.getpid()
    event.wait()
    VendedorNum=random.randint(1,200)
    x=0
    cont=0
    while True:
        time.sleep(0.01)
        if total.value==0:
            break
        if random.randint(0,1)==1:
            cont+=1
            if Num==1:
                CompNum=cont
            else:
                CompNum=cont+(Num.value*5)
            x=random.randint(1,200)
            lock.acquire()
            if total.value-x >=0:
                totalVendidas.value+=x
                total.value-=x
                print("Soy el vendedor #"
                +str(Num.value)+" y le vendí: "
                +str(x)+" al comprador #"
                +str(CompNum)+" y ahora solo quedan "
                +str(total.value)+" leches. Total de leches vendidas son "
                +str(totalVendidas.value))
                lock.release()                                                  #Release
            else:
                cont-=1
                lock.release()                                                  #Release
                continue
        if cont==5:                                                             #Release
            break

if __name__ == '__main__':
    e=Event()
    totalInventario = Value('i', 1000)
    totalVendidas = Value('i', 0)
    Num = Value('i',0)
    lock = Lock()
    Num=Value('i',Num.value+1)
    Seller1 = Process(target=sell, args=(lock,e,Num,totalInventario,totalVendidas))
    Num=Value('i',Num.value+1)
    Seller2 = Process(target=sell, args=(lock,e,Num,totalInventario,totalVendidas))
    Num=Value('i',Num.value+1)
    Seller3 = Process(target=sell, args=(lock,e,Num,totalInventario,totalVendidas))
    Num=Value('i',Num.value+1)
    Seller4 = Process(target=sell, args=(lock,e,Num,totalInventario,totalVendidas))
    Num=Value('i',Num.value+1)
    Seller5 = Process(target=sell, args=(lock,e,Num,totalInventario,totalVendidas))

    Seller1.start()
    Seller2.start()
    Seller3.start()
    Seller4.start()
    Seller5.start()

    e.set()

    Seller1.join()
    Seller2.join()
    Seller3.join()
    Seller4.join()
    Seller5.join()

    print(  "\|/          (__) \n"+
            "     `\------(oo)    La vaquita ya no tiene leche :( \n"+
            "       ||    (__)\n"+
            "       ||w--||     \|/\n"+
            "   \|/\n")
