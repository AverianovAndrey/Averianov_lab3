from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x700')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
A=[]
C=[]
name=input("your name: ")

t=2000
rt=0
f=0
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global A,colors,t
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx=rnd(-5,5)
    vy=rnd(-5,5)
    color=choice(colors)
    A.append([x,y,r,vx,vy,color])
    if len(A)+len(A)<20:
        t=t*0.993
        root.after(int(t),new_ball)	

def new_rect():
    global C,colors,t
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx=rnd(-5,5)
    vy=rnd(-5,5)
    color=choice(colors)
    C.append([x,y,r,vx,vy,color])
    if len(C)+len(A)<20:
        t=t*0.993
        root.after(int(t),new_rect)	

def move_balls():
    global A
    canv.delete(ALL)
    canv.create_text(100,650,text=str(rt),justify=CENTER,font="Verdana 16")
    for i in A:
        i[0]=i[0]+i[3]
        i[1]=i[1]+i[4]
        canv.create_oval(i[0]-i[2],i[1]-i[2],i[0]+i[2],i[1]+i[2],fill = i[5], width=0)
        if i[0]>800-i[2]:
            i[3]=rnd(-5,-1)
            i[4]=rnd(-5,5)
        if i[0]<i[2]:
            i[3]=rnd(1,5)
            i[4]=rnd(-5,5)
        if i[1]>600-i[2]:
            i[4]=rnd(-5,-1)
            i[3]=rnd(-5,5)
        if i[1]<i[2]:
            i[4]=rnd(1,5)
            i[3]=rnd(-5,5)
    global C,f
    canv.create_text(100,650,text=str(rt),justify=CENTER,font="Verdana 16")
    for i in C:
        if f>=50:
            i[3]=int(i[3]+3*(-1)**rnd(1,100))
            i[4]=int(i[4]+3*(-1)**rnd(1,100))
            i[0]=i[0]+i[3]
            i[1]=i[1]+i[4]
            f=0
        else:
            i[0]=i[0]+i[3]
            i[1]=i[1]+i[4]
            f=f+1
        canv.create_rectangle(i[0]-i[2],i[1]-i[2],i[0]+i[2],i[1]+i[2],fill = i[5], width=0)
        if i[0]>800-i[2]:
            i[3]=rnd(-5,-1)
            i[4]=rnd(-5,5)
        if i[0]<i[2]:
            i[3]=rnd(1,5)
            i[4]=rnd(-5,5)
        if i[1]>600-i[2]:
            i[4]=rnd(-5,-1)
            i[3]=rnd(-5,5)
        if i[1]<i[2]:
            i[4]=rnd(1,5)
            i[3]=rnd(-5,5)
    if len(A)+len(C)<20:
        root.after(10,move_balls)
    else:
        canv.delete(ALL)
        canv.create_text(400,350,text="GAME OVER",justify=CENTER,font="Verdana 40")
        canv.create_text(400,400,text="Your score "+str(rt),justify=CENTER,font="Verdana 20")

def click1(event):
    global A,rt
    B=[]
    for i in A:
        if (event.x-i[0])**2+(event.y-i[1])**2>i[2]**2:
            B.append(i)
        else:
            rt=rt+1
            #print(str(rt))
    A=B
    global C
    N=[]
    for i in C:
        if (event.x-i[0])**2+(event.y-i[1])**2>(i[2]*1.2)**2:
            N.append(i)
        else:
            rt=rt+2
            #print(str(rt))
    C=N


canv.bind('<Button-1>', click1)
new_ball()
new_rect()
move_balls()
mainloop()
print(rt)
tx=open('reit.txt','r')
A=[]
S=[]
SR=[]
for line in tx:
    nb=0
    s=""
    num=""
    while s!=" ":
        s=line[nb]
        if s!=" ":
            num=num+s
            nb=nb+1
    A.append(int(num))
    S.append(line)
print(A)
ttt=0
B=[]
j=0
for i in A:
    if rt<i:
        B.append(i)
        SR.append(S[j])
        j=j+1
    else:
        if ttt==0:
            B.append(rt)
            SR.append(str(rt)+" "+name+"\n")
            ttt=1
            B.append(i)
            SR.append(S[j])
            j=j+1
        else:
            B.append(i)
            SR.append(S[j])
            j=j+1
if ttt==0:
    B.append(rt)
    SR.append(str(rt)+" "+name+"\n")
print(B)
print(S)
print(SR)
tx.close()
tx=open('reit.txt','w')
for i in SR:
    tx.write(i)

                                                                                                                                             