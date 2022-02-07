#every thing is widget in tkinter
from ast import Lambda
import math
from tkinter import *
from tkinter import Tk, ttk

#start with this very important
root=Tk()
root.title("simple calculator")

#entering into widget

e=Entry(root,width=35)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3,)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num 
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

def button_eq():
    second_number=e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_number))

    if math == "subtraction":
        e.insert(0,f_num - int(second_number))

    if math == "multiplication":
        e.insert(0,f_num * int(second_number))

def button_sub():
    first_number=e.get()
    global f_num 
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)
    

def button_mi():
    first_number=e.get()
    global f_num 
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)


button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1)).grid(row=3,column=0)
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2)).grid(row=3,column=1)
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3)).grid(row=3,column=2)
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4)).grid(row=2,column=0)
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=1)
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=2)
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7)).grid(row=1,column=0)
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8)).grid(row=1,column=1)
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9)).grid(row=1,column=2)
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=0)
button_clc = Button(root,text="clc",padx=35,pady=20,command=button_clear).grid(row=5,column=2)
button_eq = Button(root,text="=",padx=35,pady=20,command=button_eq).grid(row=4,column=2)
button_add = Button(root,text="+",padx=35,pady=20,command=button_add).grid(row=5,column=0)
button_sub = Button(root,text="-",padx=35,pady=20,command=button_sub).grid(row=5,column=1)
button_mi = Button(root,text="*",padx=35,pady=20,command=button_mi).grid(row=4,column=1)

root.mainloop()




