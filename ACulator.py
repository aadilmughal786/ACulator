import tkinter
from math import *
from built_in import *
from user_define import *
#------------------- devloper variable ----------------------------------
devloper = "Aadil Mugal"
version = "v1.0"
#--------------------------- main window(root)  ----------------------------
root = tkinter.Tk()
root.title("ACulator")
root.resizable(0,0)
#------------------------- global variable --------------------------
font_btn_num = "bold 11"
font_entry = "bold 16"
entry_var = tkinter.StringVar()
#------------------------------- functons ----------------------
def WantExit():
    def exitt():
        root1.destroy()
        root.destroy()
      
    root1 = tkinter.Tk()
    root1.title("Want Exit?")
    root1.resizable(0,0)
    root1.geometry("300x100")
    Msg = tkinter.Label(root1,text = "Do you want to exit ?",font = "20")
    Msg.place(x = 70,y = 20)
    CalcleButton = tkinter.Button(root1,text = "Cancle",command = root1.destroy)
    CalcleButton.place(x =70,y = 60)
    YesButton = tkinter.Button(root1,text = "Yes",command = exitt)
    YesButton.place( x =190,y = 60)
    root1.mainloop()

def char_print(symbol):
    entry_var.set(entry_var.get()+symbol)

def facto():
    if len(entry_var.get())==0:
        entry_var.set("Enter Somthing")
        return 0
    try:
        if int(entry_var.get())>25:
            entry_var.set("Too Long")
        else:
            entry_var.set(str(factorial(int(entry_var.get()))))
    except:
        entry_var.set("Error")

def allclear():
    if len(entry_var.get())==0:
        entry_var.set("Nothing to clean")
        return 0
    else:
        entry_var.set("")

def sqrrt():
    if len(entry_var.get())==0:
        entry_var.set("Enter Somthing")
        return 0
    try:
        entry_var.set(str(sqrt(float(entry_var.get()))))
    except:
        entry_var.set("Error")

def persant():
    if len(entry_var.get())==0:
        entry_var.set("Enter Somthing")
        return 0
    try:
        entry_var.set(str(float(eval(entry_var.get()))/100))
    except:
        entry_var.set("Error")
    

def equal():
    if len(entry_var.get())==0:
        entry_var.set("Enter Somthing")
        return 0
    try:
        entry_var.set(eval(entry_var.get()))
    except:
        entry_var.set("Error")
#------------------------- menu -----------------------------------------

menubar = tkinter.Menu(root)
menubar.add_command(label = "About")
menubar.add_command(label = "Exit",command = WantExit)
root.config(menu = menubar)

#------------------ Entery for input ---------------------------
EntryInput = tkinter.Entry(root,font = font_entry,justify = tkinter.RIGHT,textvariable = entry_var)
EntryInput.grid(row = 0,column = 0,columnspan = 5,sticky="nsew",padx = 3,pady = (3,3))

#------------------ first Buttons Row ---------------------------
ButtonFactorial = tkinter.Button(root,text = "x!" ,width = 6,command = facto)
ButtonFactorial.grid(row = 3,column = 0,sticky="nsew",ipady = 3,padx = (3,0))

ParaOpen = tkinter.Button(root,text = "(",width = 6,command = lambda:char_print("("))
ParaOpen.grid(row = 3,column = 1,sticky="nsew")

ParaClose = tkinter.Button(root,text = ")",width = 6,command = lambda:char_print(")"))
ParaClose.grid(row = 3,column = 2,sticky="nsew")

PerButton = tkinter.Button(root,text = "%",width = 6,command = persant)
PerButton.grid(row = 3,column = 3,sticky="nsew")

AllClear = tkinter.Button(root,text = "AC",fg = "red",font = font_btn_num,width = 6,command = allclear)
AllClear.grid(row = 3,column = 4,sticky="nsew",padx = (0,3))

#------------------ second Buttons Row ---------------------------
PiButton = tkinter.Button(root,text = "pi",command = lambda:char_print("pi"))
PiButton.grid(row = 4,column = 0,sticky="nsew",ipady = 3,padx = (3,0))

ButtonSeven = tkinter.Button(root,text = "7",font = font_btn_num,command = lambda:char_print("7"))
ButtonSeven.grid(row = 4,column = 1,sticky="nsew")

ButtonEight = tkinter.Button(root,text = "8",font = font_btn_num,command = lambda:char_print("8"))
ButtonEight.grid(row = 4,column = 2,sticky="nsew")

ButtonNine = tkinter.Button(root,text = "9",font = font_btn_num,command = lambda:char_print("9"))
ButtonNine.grid(row = 4,column = 3,sticky="nsew")

DivButton = tkinter.Button(root,text = "/",command = lambda:char_print("/"))
DivButton.grid(row = 4,column = 4,sticky="nsew",padx = (0,3))

#------------------ third Buttons Row ---------------------------
ValueOfe = tkinter.Button(root,text = "e",command = lambda:char_print("e"))
ValueOfe.grid(row = 5,column = 0,sticky="nsew",ipady = 3,padx = (3,0))

ButtonFour = tkinter.Button(root,text = "4",font = font_btn_num,command = lambda:char_print("4"))
ButtonFour.grid(row = 5,column = 1,sticky="nsew")

ButtonFive = tkinter.Button(root,text = "5",font = font_btn_num,command = lambda:char_print("5"))
ButtonFive.grid(row = 5,column = 2,sticky="nsew")

ButtonSix = tkinter.Button(root,text = "6",font = font_btn_num,command = lambda:char_print("6"))
ButtonSix.grid(row = 5,column = 3,sticky="nsew")

MulButton = tkinter.Button(root,text = "*",command = lambda:char_print("*"))
MulButton.grid(row = 5,column = 4,sticky="nsew",padx = (0,3))

#------------------ forth Buttons Row ---------------------------
ButtonSqrt = tkinter.Button(root,text = "√",command = sqrrt)
ButtonSqrt.grid(row = 6,column = 0,sticky="nsew",ipady = 3,padx = (3,0))

ButtonOne = tkinter.Button(root,text = "1",font = font_btn_num,command = lambda:char_print("1"))
ButtonOne.grid(row = 6,column = 1,sticky="nsew")

ButtonTwo = tkinter.Button(root,text = "2",font = font_btn_num,command = lambda:char_print("2"))
ButtonTwo.grid(row = 6,column = 2,sticky="nsew")

ButtonThree = tkinter.Button(root,text = "3",font = font_btn_num,command = lambda:char_print("3"))
ButtonThree.grid(row = 6,column = 3,sticky="nsew")

SubButton = tkinter.Button(root,text = "-",command = lambda:char_print("-"))
SubButton.grid(row = 6,column = 4,sticky="nsew",padx = (0,3))

#------------------ fifth Buttons Row ---------------------------
DotButton = tkinter.Button(root,text = ".",command = lambda:char_print("."))
DotButton.grid(row = 7,column = 0,sticky="nsew",ipady = 3,padx = (3,0),pady = (0,3))

ButtonZero = tkinter.Button(root,text = "0",font = font_btn_num,command = lambda:char_print("0"))
ButtonZero.grid(row = 7,column = 1,sticky="nsew",pady = (0,3))

EvalButton = tkinter.Button(root,text = "=",font = font_btn_num,command = equal)
EvalButton.grid(row = 7,column = 2 ,columnspan = 2,sticky="nsew",pady = (0,3))

AddButton = tkinter.Button(root,text = "+",command = lambda:char_print("+"))
AddButton.grid(row = 7,column = 4,sticky="nsew",padx = (0,3),pady = (0,3))

#------------------- event loop(for event hndling) -----------------------------
root.mainloop()
