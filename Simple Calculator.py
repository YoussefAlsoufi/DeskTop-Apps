from tkinter import *


class calculator(Frame):
    def __init__(self):
        Frame.__init__(self, bg="red")
        self.option_add('*font','arial 27 bold')  # to change the size of letter in all the frames inside the basic Frame
        self.pack(expand=YES,fill = BOTH)
        self.master.title("Calculator")
        
        # create a screen :
        display=StringVar()
        obj=Entry(self,relief=RIDGE ,textvariable=display,justify='right',bd=20,bg="powder blue",width=20)
        obj.pack(side=TOP,expand=YES,fill=BOTH)

       
        # create the buttons :
        for frame1 in ("987","456","123","0.+","/*-"):
            frame=Frame(self,bd=2,bg="blue")
            frame.pack(side=TOP,expand=YES,fill=BOTH)
            for char in frame1:
                button=Button(frame,text=char,bg="white",command=lambda stored =display , ch=char:stored.set(stored.get()+ch))
                button.pack(side=LEFT,expand=YES,fill=BOTH)
            
        frame2=Frame(self,bd=2,bg='silver')
        frame2.pack(side=TOP,expand=YES,fill=BOTH)
        # clear button :
        clearbutton=Button(frame2,text="Clear",bg="powder blue",bd=2, command=lambda stored =display: stored.set(""))
        clearbutton.pack(side=LEFT,expand=YES,fill=BOTH)
        
        # equal button : 
        equal=Button(frame2,text="=",bg="gray",bd=2 , command=lambda stored= display : evaluate (stored))
        equal.pack(side=LEFT,expand=YES,fill=BOTH)
        
        
        
def evaluate(stored):
    try :
        stored.set(eval(stored.get()))
    except :
        stored.set("ERROR")

        
calculator().mainloop()        
