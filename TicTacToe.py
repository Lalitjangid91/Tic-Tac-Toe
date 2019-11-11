from tkinter import *
import tkinter.messagebox
class TTK(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.iconbitmap('melody.ico')
        self.config(bg='powder blue')
        self.geometry('400x400')
        self.btn()
        self.start=Button(self,text='START',command=self.GameStart)
        self.start.grid(row=3,column=1,padx=10,pady=10,sticky='nswe')
        for i in range(4):
            self.grid_rowconfigure(i,weight=1)
        for i in range(3):
            self.grid_columnconfigure(i,weight=1)
    def btn(self):
        self.lb=[]
        for i in range(3):
            for j in range(3):
                self.lb.append(Button(self,state='disable',command=lambda t=(i,j):self.Turn(t)))
                self.lb[-1].grid(row=i,column=j,padx=10,pady=10,sticky='nswe')
        self.p1 = set()
        self.p2 = set()
        self.count=0
    def GameStart(self):
        for b in self.lb:
            b['state']='active'
        self.start['state']='disable'
        self.flag=True
        self.label1 = Label(self, text='Player 1',bg='red',font="arial 15 bold")
        self.label1.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')
        self.label2 = Label(self,text=None,bg='blue',font="arial 15 bold")
        self.label2.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')
    def Turn(self,t):
        if self.flag==True:
            self.lb[3*t[0]+t[1]]['bg']='red'
            self.flag=False
            self.label2['text']='Player2'
            self.label1['text']=''
            self.p1.add(3*t[0]+t[1])

        else:
            self.lb[3 * t[0] + t[1]]['bg'] = 'blue'
            self.flag = True
            self.label1['text'] = 'Player1'
            self.label2['text'] =''
            self.p2.add(3 * t[0] + t[1])
        self.lb[3 * t[0] + t[1]]['state'] = 'disable'
        self.count=self.count+1
        self.Result()
        if self.count==9:
            tkinter.messagebox.showinfo('Result','Draw')
            self.btn()
            self.start['state'] = 'active'

    def Result(self):
        win_com=[{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        for t in win_com:
            if t<=self.p1:
                tkinter.messagebox.showinfo('Result','Player 1 Win')
                self.btn()
                self.start['state'] = 'active'
                break
            if t<=self.p2:
                tkinter.messagebox.showinfo('Result','Player 2 Win')
                self.btn()
                self.start['state']='active'
                break
obj=TTK()
obj.mainloop()
