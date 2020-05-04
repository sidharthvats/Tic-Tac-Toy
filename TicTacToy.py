from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title('Tic Tac Toy: Player 1')

#PlayerOptimization

ActivePlayer=1
P1=[]
P2=[]

#AddButtons

def BuClick(id):
    print("ID : {}".format(id))


B1=ttk.Button(root,text=' ')
B1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
B1.config(command=lambda :BuClick(1))

B2=ttk.Button(root,text=' ')
B2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
B2.config(command=lambda:BuClick(2))

B3=ttk.Button(root,text=' ')
B3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
B3.config(command=lambda:BuClick(3))

B4=ttk.Button(root,text=' ')
B4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
B4.config(command=lambda:BuClick(4))

B5=ttk.Button(root,text=' ')
B5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
B5.config(command=lambda:BuClick(5))

B6=ttk.Button(root,text=' ')
B6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
B6.config(command=lambda:BuClick(6))

B7=ttk.Button(root,text=' ')
B7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
B7.config(command=lambda:BuClick(7))

B8=ttk.Button(root,text=' ')
B8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
B8.config(command=lambda:BuClick(8))

B9=ttk.Button(root,text=' ')
B9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
B9.config(command=lambda:BuClick(9))


def BuClick(id):
    global ActivePlayer
    if(ActivePlayer==1):
        SetLayout(id,"X")
        root.title("Tic Tac Toe : Player2")
        P1.append(id)
        ActivePlayer=2
    elif(ActivePlayer==2):
        SetLayout(id, "0")
        root.title("Tic Tac Toe : Player1")
        P2.append(id)
        ActivePlayer = 1

    checkwinner()

def checkwinner():
    winner=-1
    if((1 in P1) and (2 in P1) and(3 in P1)):
        winner=1
    if ((1 in P2) and (2 in P2) and (3 in P2)):
        winner = 2

    if ((4 in P1) and (5 in P1) and (6 in P1)):
        winner = 1
    if ((4 in P2) and (5 in P2) and (6 in P2)):
        winner = 2

    if ((7 in P1) and (8 in P1) and (9 in P1)):
        winner = 1
    if ((7 in P2) and (8 in P2) and (9 in P2)):
        winner = 2

    if ((1 in P1) and (4 in P1) and (7 in P1)):
        winner = 1
    if ((1 in P2) and (4 in P2) and (7 in P2)):
        winner = 2

    if ((2 in P1) and (5 in P1) and (8 in P1)):
        winner = 1
    if ((2 in P2) and (5 in P2) and (8 in P2)):
        winner = 2

    if ((3 in P1) and (6 in P1) and (9 in P1)):
        winner = 1
    if ((3 in P2) and (6 in P2) and (9 in P2)):
        winner = 2

    if ((1 in P1) and (5 in P1) and (9 in P1)):
        winner = 1
    if ((1 in P2) and (5 in P2) and (9 in P2)):
        winner = 2

    if ((3 in P1) and (5 in P1) and (7 in P1)):
        winner = 1
    if ((3 in P2) and (5 in P2) and (7 in P2)):
        winner = 2


    if(winner==1):
        messagebox.showinfo('GAME OVER',message="Congrats Player 1 , you are the winner my nigga!")
    elif (winner == 2):
        messagebox.showinfo('GAME OVER', message="Congrats Player 2 , you are the winner my nigga!")


def SetLayout(id,playersymbol):
    if(id==1):
        B1.config(text=playersymbol)
        B1.state(['disabled'])

    elif id==2:
        B2.config(text=playersymbol)
        B2.state(['disabled'])

    elif id == 3:
        B3.config(text=playersymbol)
        B3.state(['disabled'])

    elif id == 4:
        B4.config(text=playersymbol)
        B4.state(['disabled'])

    elif id == 5:
        B5.config(text=playersymbol)
        B5.state(['disabled'])

    elif id == 6:
        B6.config(text=playersymbol)
        B6.state(['disabled'])

    elif id == 7:
        B7.config(text=playersymbol)
        B7.state(['disabled'])

    elif id == 8:
        B8.config(text=playersymbol)
        B8.state(['disabled'])

    elif id == 9:
        B9.config(text=playersymbol)
        B9.state(['disabled'])


root.mainloop()