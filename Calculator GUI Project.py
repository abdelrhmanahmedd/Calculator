import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter

window = Tk()
window.title("Calculator GUI Project")
window.config(background="Black")
entry_label = Label(window, text="Calculator | Abdelrhman Ahmed", foreground="White", background="Black").grid(row=0, column=0, sticky=W)

def set_1():
    text_edit.insert(END,"1")
def set_2():
    text_edit.insert(END,"2")
def set_3():
    text_edit.insert(END,"3")        
def set_4():
    text_edit.insert(END,"4")
def set_5():
    text_edit.insert(END,"5")    
def set_6():
    text_edit.insert(END,"6")    
def set_7():
    text_edit.insert(END,"7")    
def set_8():
    text_edit.insert(END,"8")    
def set_9():
    text_edit.insert(END,"9")
def set_0():
    text_edit.insert(END,".")
def set_0():
    text_edit.insert(END,"0")
def set_Rb():
    text_edit.insert(END,"(")
def set_Lb():
    text_edit.insert(END,")")
def set_add():
    text_edit.insert(END,"+")
def set_sub():
    text_edit.insert(END,"-")
def set_mul():
    text_edit.insert(END,"×")
def set_div():
    text_edit.insert(END,"÷")                                
def set_dot():
    text_edit.insert(END,".")
def set_c():
    T.set("")     
def sum():
    sum = text_edit.get()
    if sum == "":
        T.set("")
        
    newSum = ""
    for x in range(len(sum)):
        if "×" == sum[x]:
            newSum += "*"
        elif "÷" == sum[x]:
            newSum += "/"
        else:      
            newSum += sum[x]
    try:
        result = eval(newSum)
        T.set(result)
    except:
        if sum == "":
            T.set("")
        else:
            T.set("Syntax Error")                     


    
frame1 = Frame(window, background="black")
T = tk.StringVar()
text_edit = tk.Entry(frame1, font=("Arial", 40), foreground="White", background="Black", bd=0, textvariable=T)
text_edit.grid(row=0, column=0, sticky=tk.W+tk.E, padx=10)

frame2 = Frame(frame1)
frame2.grid(row=1, column=0)

but1 = Button(frame2, text="1", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_1)
but1.grid(row=2, column=0, sticky=tk.W+tk.E)
but2 = Button(frame2, text="2", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_2)
but2.grid(row=2, column=1, sticky=tk.W+tk.E)
but3 = Button(frame2, text="3", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_3)
but3.grid(row=2, column=2, sticky=tk.W+tk.E)
but4 = Button(frame2, text="4", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_4)
but4.grid(row=3, column=0, sticky=tk.W+tk.E)
but5 = Button(frame2, text="5", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_5)
but5.grid(row=3, column=1, sticky=tk.W+tk.E)
but6 = Button(frame2, text="6", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_6)
but6.grid(row=3, column=2, sticky=tk.W+tk.E)
but7 = Button(frame2, text="7", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_7)
but7.grid(row=4, column=0, sticky=tk.W+tk.E)
but8 = Button(frame2, text="8", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_8)
but8.grid(row=4, column=1, sticky=tk.W+tk.E)
but9 = Button(frame2, text="9", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_9)
but9.grid(row=4, column=2, sticky=tk.W+tk.E)
but_dot = Button(frame2, text=".", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_dot)
but_dot.grid(row=5, column=2, sticky=tk.W+tk.E)
but0 = Button(frame2, text="0", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_0)
but0.grid(row=5, column=1, sticky=tk.W+tk.E)
but_eq = Button(frame2, text="=", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=sum)
but_eq.grid(row=5, column=3, sticky=tk.W+tk.E)
but_clear = Button(frame2, text="c", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_c)
but_clear.grid(row=1, column=2, sticky=tk.W+tk.E)
but_R_B = Button(frame2, text="(", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_Rb)
but_R_B.grid(row=1, column=0, sticky=tk.W+tk.E)
but_L_B = Button(frame2, text=")", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_Lb)
but_L_B.grid(row=1, column=1, sticky=tk.W+tk.E)

but_div = Button(frame2, text="÷", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_div)
but_div.grid(row=1, column=3, sticky=tk.W+tk.E)
but_mul = Button(frame2, text="×", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_mul)
but_mul.grid(row=2, column=3, sticky=tk.W+tk.E)
but_sub = Button(frame2, text="-", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_sub)
but_sub.grid(row=3, column=3, sticky=tk.W+tk.E)
but_add = Button(frame2, text="+", font=("Arial", 20), width=12, bd=0, foreground="white", background="#2B2B2B", command=set_add)
but_add.grid(row=4, column=3, sticky=tk.W+tk.E)


frame1.grid()
window.mainloop()