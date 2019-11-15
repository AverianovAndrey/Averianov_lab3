from gun import*
from table import*
from gun import cc

cc = 0
def game():
    global cc
    while cc == 0:
        cc=new_game()
        print(cc)
    rt = rote()
    canv.delete(ALL)
    canv.create_text(400,300,text="GAME OVER",justify=CENTER,font="Verdana 40")
    canv.create_text(400,350,text="Your score "+str(rt),justify=CENTER,font="Verdana 20")
    print(rt)       
    lead(rt,name)
oo = 0
#while True:
name = input("введите имя")
    #if oo == 0:
        #print("press 1 to start the game")
        #cod = input()
        #oo == 1
    #else:
        #print("press 1 to restart")
        #cod = input()
    #if cod == '1':
        #game()
    #time.sleep(3000)
    #canv.delete(ALL)
    #game()
game()
cc = 0


mainloop()