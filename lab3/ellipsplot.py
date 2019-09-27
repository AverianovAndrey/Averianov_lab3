from graph import *
windowSize(1000,1000)
penColor(0,0,0)
brushColor(0,0,0)
def ellipse(x1,y1,x2,y2,bp):
    A=[]
    for x in range(1000):
        for y in range(1000):
            k=((x-x1)**2+(y-y1)**2)**0.5
            l=((x-x2)**2+(y-y2)**2)**0.5
            rad=((x1-x2)**2+(y1-y2)**2)**0.5
            r=(2*bp-rad)/2
            d=(rad+2*r)/10
            if k+l<d*10-4.27+0.1*d and k+l>d*10-4.27-0.1*d:
                A.append((x,y))
    polygon(A)
ellipse(250,250,250,250,250)
run()