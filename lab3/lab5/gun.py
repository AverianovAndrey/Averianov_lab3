from random import randrange as rnd, choice
import tkinter as tk
from tkinter import *
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        #self.x += self.vx
        #self.y -= self.vy
        if self.y<=500:
            self.vy-=1.2
            self.y-=self.vy
            self.x+=self.vx
            self.vx*=0.99
            self.set_coords()
        else:
            if self.vx**2+self.vy**2>10:
                self.vy=-self.vy/2
                self.vx=self.vx/2
                self.y=499
            if self.live<0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live-=1
        if self.x>780:
            self.vx=-self.vx/2
            self.x=779

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
            #return False
        if abs(obj.x-self.x)<=(self.r+obj.r) and abs(obj.y-self.y)<=(self.r+obj.r):
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.k=-1
        self.x = 20
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
        self.dx = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.x = self.x
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.k*self.f2_power * math.cos(self.an)
        new_ball.vy = - self.k*self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.x-self.x>0:
            self.an = math.atan((event.y-450) / (event.x-self.x))
            self.k=1
        if event and event.x-self.x<0:
            self.an = math.atan((event.y-450) / (self.x-event.x))
            self.k=-1
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, 450,
                    (self.x + self.k*max(self.f2_power, 20) * (math.cos(self.an))),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
    def move_gun1(self, event):
        #if event:
        self.x = self.x + 10
        #print(self.x)
    def move_gun2(self, event):
        self.x = self.x - 10
            
a1=0
a2=0
a3=0


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()
        self.cont = 0
        self.x = 0
        self.y = 0
        self.r = 0

    def new_target(self):
        global a1,a2,a3
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        a1=x
        a2=y
        a3=r
        self.vx = rnd(-4,4)
        self.vy = rnd(-4,4)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        self.cont = 0

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)
        self.cont = 1
    def move_target(self):
        x=self.x
        y=self.y
        r=self.r
        vx=self.vx
        vy=self.vy
        if self.cont == 0:
            if self.x < self.r:
                self.vx = -self.vx
            if self.x > 800-self.r:
                self.vx = -self.vx
            if self.y < self.r:
                self.vy = -self.vy
            if self.y > 600-self.r:
                self.vy = -self.vy
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            canv.coords(self.id,x-r,y-r,x+r,y+r)
            


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
cc = 0
rt = 0

def new_game(event=''):
    global gun, t1, screen1, balls, bullet, cc, rt
    t1.new_target()
    t2.new_target()
    #t1.move_target()
    bullet = 0
    balls = []
    a=0
    b=0
    c=0
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<Button-2>',g1.move_gun1)
    canv.bind('<Button-3>',g1.move_gun2)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while (t1.live or t2.live) or balls:
        t1.move_target()
        t2.move_target()
        if (g1.x-t1.x)**2+(450-t1.y)**2<t1.r**2 or (g1.x-t2.x)**2+(450-t2.y)**2<t2.r**2:
            t1.live = 0
            t2.live = 0
            t1.hit()
            t2.hit()
            a = 1
            b = 1
            c = 1
            cc = 1
        #g1.move_gun()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                rt = rt + 1
                a=1
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                rt = rt + 1
                b=1
            if a==1 and b==1:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                #canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    #canv.itemconfig(screen1, text='')
    canv.delete(gun)
    g1.x = 20
    return cc
def rote():
    global rt
    return rt
    #if cc == 0:
        #root.after(750, new_game)
    #else:
        #canv.delete(ALL)
        #canv.create_text(400,300,text="GAME OVER",justify=CENTER,font="Verdana 40")
        #canv.create_text(400,350,text="Your score "+str(rt),justify=CENTER,font="Verdana 20")
        #print(rt)       


#new_game()
#if cc == 1:
    #canv.delete(ALL)
    #canv.create_text(400,300,text="GAME OVER",justify=CENTER,font="Verdana 40")
    #canv.create_text(400,350,text="Your score "+str(rt),justify=CENTER,font="Verdana 20")

#mainloop()
