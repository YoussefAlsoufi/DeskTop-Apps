from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from random import randint 

ActivePlayer=1  # set active player .
P1=[]   # what player 1 selected .
P2=[]   # what player 2 selected .
 

root =Tk()
root.title("Tiz Tac Toy : Player 1")
style=ttk.Style()
style.theme_use("classic")

bu1=ttk.Button(root,text =" ")
bu1.grid(row=0,column=0,sticky="snew",ipadx=40, ipady=40)
bu1.config(command= lambda : Buclick(1))

bu2=ttk.Button(root,text =" ")
bu2.grid(row=0,column=1,sticky="snew",ipadx=40, ipady=40)
bu2.config(command= lambda : Buclick(2))

bu3=ttk.Button(root,text =" ")
bu3.grid(row=0,column=2,sticky="snew",ipadx=40, ipady=40)
bu3.config(command= lambda : Buclick(3))

bu4=ttk.Button(root,text =" ")
bu4.grid(row=1,column=0,sticky="snew",ipadx=40, ipady=40)
bu4.config(command= lambda : Buclick(4))

bu5=ttk.Button(root,text =" ")
bu5.grid(row=1,column=1,sticky="snew",ipadx=40, ipady=40)
bu5.config(command= lambda : Buclick(5))

bu6=ttk.Button(root,text =" ")
bu6.grid(row=1,column=2,sticky="snew",ipadx=40, ipady=40)
bu6.config(command= lambda : Buclick(6))

bu7=ttk.Button(root,text =" ")
bu7.grid(row=2,column=0,sticky="snew",ipadx=40, ipady=40)
bu7.config(command= lambda : Buclick(7))

bu8=ttk.Button(root,text =" ")
bu8.grid(row=2,column=1,sticky="snew",ipadx=40, ipady=40)
bu8.config(command= lambda : Buclick(8))

bu9=ttk.Button(root,text =" ")
bu9.grid(row=2,column=2,sticky="snew",ipadx=40, ipady=40)
bu9.config(command= lambda : Buclick(9))

def Buclick(id):
    global ActivePlayer 
    global P1
    global P2
    if (ActivePlayer ==1):
        SetLayout(id,"X")
        P1.append(id)
        root.title("Tic Tac toy : Player 2")
        ActivePlayer =2
        print ("P1:{}".format(P1))
        Autoplay()
    elif (ActivePlayer ==2):
        SetLayout(id,"O")
        P2.append(id)
        root.title("Tic Tac toy : Player 1")
        ActivePlayer =1
        print ("P2:{}".format(P2))   
    checkwinner()    
   #  print ("x={}".format (x)) Now i don't need this .
    
def SetLayout (id,text):
    if (id==1):
        bu1.config(text= text)
        bu1.state(["disabled"])
    elif (id==2):
        bu2.config(text= text)
        bu2.state(["disabled"])
    
    elif (id==3):
        bu3.config(text= text)
        bu3.state(["disabled"])
    
    elif (id==4):
        bu4.config(text= text)
        bu4.state(["disabled"])
    
    elif (id==5):
        bu5.config(text= text)
        bu5.state(["disabled"])
    
    elif (id==6):
        bu6.config(text= text)
        bu6.state(["disabled"])
    
    elif (id==7):
        bu7.config(text= text)
        bu7.state(["disabled"])
    
    elif (id==8):
        bu8.config(text= text)
        bu8.state(["disabled"])
    
    elif (id==9):
        bu9.config(text= text)
        bu9.state(["disabled"])
    
def checkwinner ():
    Winer=0
    if (1 in P1) and (2 in P1) and (3 in P1):
        Winer=1 
    elif (1 in P2) and (2 in P2) and (3 in P2):
        Winer=2
    elif (4 in P1) and (5 in P1) and (6 in P1):
        Winer=1 
    elif (4 in P2) and (5 in P2) and (6 in P2):
        Winer=2 
    elif (7 in P1) and (8 in P1) and (9 in P1):
        Winer=1  
    elif (7 in P2) and (8 in P2) and (9 in P2):
        Winer=2    
    elif (1 in P1) and (4 in P1) and (7 in P1):
        Winer=1   
    elif (1 in P2) and (4 in P2) and (7 in P2):
        Winer=2
    elif (2 in P1) and (5 in P1) and (8 in P1):
        Winer=1   
    elif (2 in P2) and (5 in P2) and (8 in P2):
        Winer=2   
    elif (3 in P1) and (6 in P1) and (9 in P1):
        Winer=1  
    elif (3 in P2) and (6 in P2) and (9 in P2):
        Winer=2   
    elif (1 in P1) and (5 in P1) and (9 in P1):
        Winer=1    
    elif (1 in P2) and (5 in P2) and (9 in P2):
        Winer=2   
    elif (7 in P1) and (5 in P1) and (3 in P1):
        Winer=1     
    elif (7 in P2) and (5 in P2) and (3 in P2):
        Winer=2
        
    if Winer ==1:
        messagebox.showinfo(title="The Result ",message ="Player 1 is Winer \n programmer Youssef ,You win ")
        RandIndex=0
    
    elif Winer ==2:
        messagebox.showinfo(title="The Result ",message ="Player 2 is Winer \n programmer Youssef ,Good Luck ")
        RandIndex=0
 
def Autoplay ():
    global P1
    global P2
    EmptyCell=[]
    for cell in range (9):
        if (not( (cell+1 in P1 ) or (cell+1 in P2) )):
           EmptyCell.append(cell+1)
    RandIndex=randint(0,len(EmptyCell)-1)
    Buclick (EmptyCell[RandIndex])      




       
root.mainloop()
