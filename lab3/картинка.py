from graph import*
import math as m
ass = []



def ovalchik(x0, y0, A, B, f):
    n = 50
    a = []
    for i in range(n):
        x = x0 + A * m.cos(2 * m.pi * i / n)
        y = y0 + B * m.sin(2 * m.pi * i / n)
        x_f = x0 + (x - x0) * m.cos(f) - (y - y0) * m.sin(f)
        y_f = y0 + (y - y0) * m.cos(f) + (x - x0) * m.sin(f)
        a.append((x_f, y_f))
    polygon(a)

def prizrak(x, y, s):
    penColor(100, 100, 181)
    brushColor(100, 100, 181)
    #Тело
    p = [(x+0*s,y+0*s),(x-2*s,y),(x-8*s,y+8*s),(x-9*s,y+14*s), (x-9*s,y+17*s),(x-12*s,y+24),(x-16*s,y+36*s),(x-11*s,y+43*s),(x-16*s,y+55*s),(x-28*s,y+56*s),(x-32*s,y+64*s),(x-37*s,y+74*s),(x-41*s,y+83*s),(x-45*s,y+89*s),(x-53*s,y+77*s),(x-59*s,y+95*s),(x-62*s,y+116*s),(x-46*s,y+110*s),(x-40*s,y+108*s),(x-31*s,y+105*s),(x-29*s,y+104*s),(x-15*s,y+109*s),(x-10*s,y+117*s),(x+4*s,y+119*s),(x+13*s,y+115*s),(x+24*s,y+108*s),(x+43*s,y+ 104*s),(x+60*s,y+106*s),(x+64*s,y+107*s),(x+76*s,y+99*s), (x+81* s,y+95*s),(x+80*s,y+90*s),(x+80*s,y+79*s),(x+83*s,y+72*s),(x+89* s,y+72*s),(x+97*s,y+70*s),(x+103*s,y+61*s),(x+99*s,y+53*s),(x+96 *s,y+44*s),(x+88*s,y+57*s),(x+79*s,y+32*s),(x+66*s,y+14*s),(x+63 *s,y+9*s),(x+57*s,y-1*s),(x+51*s,y-10*s),(x+35*s,y-16*s),(x+28*s,y-17*s),(x+18*s,y-17*s),(x+5*s,y-6*s),(x-2*s,y+1*s)]
    polygon(p)
    #Поправки к телу
    ovalchik(x+87*s,y+46*s,18*s,7*s,m.pi/4)
    ovalchik(x-59*s,y+110*s,10*s,3*s,-m.pi/4)
    ovalchik(x-37*s,y+82*s,18*s,15*s,- m.pi/4)
    ovalchik(x-21*s,y+46*s,38*s,8*s,-1.3*m.pi/4)
    #Глаза
    circle(x+15*s,y+1*s,25*s)
    brushColor(136,206,223)
    circle(x+0*s,y-1*s,8*s)
    circle(x+22*s,y-7*s,8*s)
    brushColor(0,0,0)
    circle(x-2*s,y-1*s,3*s)
    circle(x+20*s,y-6*s,3*s)
    penColor(255,255,255)
    brushColor(255,255,255)
    ovalchik(x+3*s,y-5*s,5*s,2*s,-0.7*m.pi/4)
    ovalchik(x+25*s,y-10*s,5*s,2*s,-0.7*m.pi/4)
def prizrak2 (x,y,s):
    penColor(255,150,150)
    brushColor(255,150,150)
    p = [(x-0*s,y+0*s),(x+2*s,y),(x+8*s,y+8*s),(x+9*s,y+14*s), (x+9*s,y+17*s),(x+12*s,y+24),(x+16*s,y+36*s),(x+11*s,y+43*s),(x+16*s,y+55*s),(x+28*s,y+56*s),(x+32*s,y+64*s),(x+37*s,y+74*s),(x+41*s,y+83*s),(x+45*s,y+89*s),(x+53*s,y+77*s),(x+59*s,y+95*s),(x+62*s,y+116*s),(x+46*s,y+110*s),(x+40*s,y+108*s),(x+31*s,y+105*s),(x+29*s,y+104*s),(x+15*s,y+109*s),(x+10*s,y+117*s),(x-4*s,y+119*s),(x-13*s,y+115*s),(x-24*s,y+108*s),(x-43*s,y+ 104*s),(x-60*s,y+106*s),(x-64*s,y+107*s),(x-76*s,y+99*s),(x-81*s,y+95*s),(x-80*s,y+90*s),(x-80*s,y+79*s),(x-83*s,y+72*s),(x-89*s,y+72*s),(x-97*s,y+70*s),(x-103*s,y+61*s),(x-99*s,y+53*s),(x-96 *s,y+44*s),(x-88*s,y+57*s),(x-79*s,y+32*s),(x-66*s,y+14*s),(x-63 *s,y+9*s),(x-57*s,y-1*s),(x-51*s,y-10*s),(x-35*s,y-16*s),(x-28*s,y-17*s),(x-18*s,y-17*s),(x-5*s,y-6*s),(x+2*s,y+1*s)]
    polygon(p)
    #Поправки к телу
    ovalchik(x-87*s,y+46*s,18*s,7*s,m.pi-m.pi/4)
    ovalchik(x+59*s,y+110*s,10*s,3*s,m.pi+m.pi/4)
    ovalchik(x+37*s,y+82*s,18*s,15*s,m.pi+m.pi/4)
    ovalchik(x+21*s,y+46*s,38*s,8*s,m.pi+1.3*m.pi/4)
    #Глаза
    circle(x-15*s,y+1*s,25*s)
    brushColor(136,206,223)
    circle(x-0*s,y-1*s,8*s)
    circle(x-22*s,y-7*s,8*s)
    brushColor(0,0,0)
    circle(x+2*s,y-1*s,3*s)
    circle(x-20*s,y-6*s,3*s)
    penColor(255,255,255)
    brushColor(255,255,255)
    ovalchik(x-3*s,y-5*s,5*s,2*s,m.pi+0.7*m.pi/4)
    ovalchik(x-25*s,y-10*s,5*s,2*s,m.pi+0.7*m.pi/4)


def oval(x, y, A, B):
    n=60
    points_oval=[]
    for i in range(n):
        points_oval.append((x+A*m.cos(2*m.pi*i/n), y+B*m.sin(2*m.pi*i/n)))
    polygon(points_oval)

def coord(event):
    ass.append((event.x, event.y))
    print(ass)
onMouseDown(coord)





brushColor(102, 102, 102)
polygon([(500, 0),(500, 250),(0, 250),(0, 0)])

penColor(231,231,231)
brushColor(231,231,231)
circle(436, 60, 45)

penColor("Black")
brushColor(0, 0, 0)
polygon([(500, 250), (500, 600), (0, 600), (0, 250)])

penColor(19, 19, 19)
brushColor("black")
polygon([(227, 118), (246, 148),(0,148),(19,118)])

for i in range(23):
    penColor(0,11*i,0)
    brushColor(0,11*i,0)
    oval(498, 113, 230-10*i, 23-i)


for i in range(23):
    penColor(11*i,0,0)
    brushColor(11*i,0,0)
    oval(385, 164, 180-7*i, 23-i)

penColor(30, 30, 30)
brushColor(30, 30, 30)
polygon([(154,118),(164,118),(164,80),(154,80)])

brushColor(30, 30, 30)
polygon([(33, 133), (42, 133),(42,60),(33,60)])

for i in range(23):
    penColor(0,0,11*i)
    brushColor(0,0,11*i)
    oval(185, 70, 180-7*i, 30-1.3*i)


for i in range(23):
    penColor(11*i,11*i,0)
    brushColor(11*i,11*i,0)
    oval(343, 53, 156-6.7*i, 25-1.09*i)


penColor(30,30,30)
brushColor(30,30,30)
polygon([(56,136), (76, 136),(76,30),(56,30)])


polygon([(206,133),(216,133), (216, 70), (206, 70)])

penColor(43,34,0)
brushColor(43,34,0)
polygon([(22,148),(22,500),(224,500),(224,148)])

penColor(72,62,55)
brushColor(72,62,55)
rectangle(36, 240, 60, 148)
rectangle(80, 240, 104, 148)
rectangle(138, 240, 164, 148)
rectangle(191, 240,213, 148)

penColor(43, 17, 0)
brushColor(43, 17, 0)
rectangle(34, 390, 84, 330)
rectangle(99, 390, 149, 330)

penColor(212,170,0)
brushColor(212, 170,0)
rectangle(164, 390, 214, 330)

penColor(43, 17, 0)
brushColor(43, 17, 0)
rectangle(34, 470, 84, 410)
rectangle(164, 470, 214, 410)
rectangle(99, 470, 149, 410)

penColor(212,170,0)
brushColor(212, 170,0)
rectangle(99, 470, 149, 410)



penColor(26, 26, 26)
brushColor(26, 26, 26)
rectangle(0, 250, 246, 280)
rectangle(10, 220, 16, 250)
rectangle(236, 250, 230, 220)
for i in range(5):
    rectangle(34 + 40*i, 220, 44 + 40*i, 250 )
rectangle(16, 220, 230, 210)

prizrak(365, 424, 1)
prizrak2(250,500,0.5)

run()