from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("386x250+20+10")

class MyWindow:
    def __init__(self,window):

#Label and Entry
        self.fill=Label(text="                        ")
        self.fill.grid(row=0,column=0)
        self.lbl1 = Label(window, text="Simple Calculator")
        self.lbl1.grid(row=0,column=1,columnspan=2,pady=10)

        self.lbl2 = Label(window, text="Enter the 1st number:")
        self.lbl2.grid(row=1,column=1,pady=5)
        self.txt2 = Entry(window,bd=3)
        self.txt2.config(width=15)
        self.txt2.grid(row=1,column=2,pady=5,sticky=W)

        self.lbl3 = Label(window,text="Enter the 2nd number:")
        self.lbl3.grid(row=2,column=1,pady=5)
        self.txt3 = Entry(window, bd=3)
        self.txt3.config(width=15)
        self.txt3.grid(row=2,column=2,pady=5,sticky=W)

        self.lbl4 = Label(window, text="Result:")
        self.lbl4.grid(row=4, column=1, pady=25,sticky=E)
        self.txt4 = Entry(window, bd=3)
        self.txt4.config(width=15,state="readonly")
        self.txt4.grid(row=4, column=2, pady=25,sticky=W)


#Buttons
        self.btn1 = Button(window, text="Addition", command=self.add)
        self.btn1.grid(row=3,column=0,sticky=E,pady=5)
        self.btn2 = Button(window, text="Subtraction",command=self.sub)
        self.btn2.grid(row=3, column=1,pady=5)
        self.btn3 = Button(window, text="Multiplication",command=self.mul)
        self.btn3.grid(row=3, column=2,sticky=W,pady=5)
        self.btn4 = Button(window, text="Division",command=self.div)
        self.btn4.grid(row=3, column=3,columnspan=2,sticky=E,pady=5,padx=10)


#Functions
    def add(self):
        self.txt4.config(state="normal")
        self.txt4.delete(0, 'end')
        num1 = float(self.txt2.get())
        num2 = float(self.txt3.get())
        result = num1 + num2
        self.txt4.insert(END, str(result))
        self.txt4.config(state="readonly")

    def sub(self):
        self.txt4.config(state="normal")
        self.txt4.delete(0, 'end')
        num1 = float(self.txt2.get())
        num2 = float(self.txt3.get())
        result = num1 - num2
        self.txt4.insert(END, str(result))
        self.txt4.config(state="readonly")

    def mul(self):
        self.txt4.config(state="normal")
        self.txt4.delete(0, 'end')
        num1 = float(self.txt2.get())
        num2 = float(self.txt3.get())
        result = num1 * num2
        self.txt4.insert(END, str(result))
        self.txt4.config(state="readonly")

    def div(self):
        self.txt4.config(state="normal")
        self.txt4.delete(0, 'end')
        num1 = float(self.txt2.get())
        num2 = float(self.txt3.get())
        result = num1 / num2
        self.txt4.insert(END, str(result))
        self.txt4.config(state="readonly")


mywin=MyWindow(window)
window.mainloop()