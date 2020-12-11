import matplotlib.pyplot as plt
from random import randint, uniform
import os
#os.system('clear')
def hum(n,x,y):
    a = []
    b = []
    c = []
    s = 0
    for i in range(n):
        val = float(input("guess:"))
        valrand = randint(x,y)
        print("machine:",valrand,"homme:",val)
        if valrand == val:
            print("NICE")
        else:
            print("failed")
        if valrand == val:
            s +=1
        a.append(i)
        title = "humaine score is "+str(s)+"/"+str(i)
        b.append(val)
        c.append(valrand)
        want = int(input("if you wanna rep graphique no:[0] yes:[1]>>:"))
        if want == 1:
            plt.plot(a,b,label="guess")
            plt.plot(a,c,label="aleatoire")
            plt.title(title)
            plt.legend()
            plt.show()
        else:
            continue
    plt.plot(a,b,label="guess")
    plt.plot(a,c,label="aleatoire")
    title = "humaine score is "+str(s)+"/"+str(n)
    plt.legend()
    plt.title(title)
    plt.show()
    hum(n)
def mach(n,x,y):
    a = []
    b = []
    c = []
    s = 0
    for i in range(n):
        val1 = randint(x,y)
        val2 = randint(x,y)
        print("machine1:",val1,"machine2:",val2)
        if val1 == val2:
            s +=1
        a.append(i)
        title = "humaine score is "+str(s)+"/"+str(i)
        b.append(val1)
        c.append(val2)
    plt.plot(a,b,label="machine1")
    plt.plot(a,c,label="macine2")
    title = "machine1 score is "+str(s)+"/"+str(n)
    plt.legend()
    plt.title(title)
    plt.show()
#mach(10,0,10)
#hum(10,0,10)