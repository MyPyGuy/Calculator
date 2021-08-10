from tkinter import *
root = Tk()

root.title("Python Calculator")

operator = ""
text_input = StringVar()

textDisplay = Entry(root, font=("Arial", 20, "bold"), textvariable=text_input, bd=30, insertwidth=4, 
bg="powder blue", justify="right").grid(columnspan=4)

def btnClick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

##########################################Buttons##############################################

btn1 = Button(root, text="1", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(1)).grid(row=2, column=0)
btn2 = Button(root, text="2", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(2)).grid(row=2, column=1)
btn3 = Button(root, text="3", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(3)).grid(row=2, column=2)
btn4 = Button(root, text="4", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(root, text="5", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(root, text="6", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(6)).grid(row=3, column=2)
btn7 = Button(root, text="7", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(7)).grid(row=4, column=0)
btn8 = Button(root, text="8", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(8)).grid(row=4, column=1)
btn9 = Button(root, text="9", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(9)).grid(row=4, column=2)
btn0 = Button(root, text="0", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(0)).grid(row=5, column=1)
btnplus = Button(root, text="+", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick("+")).grid(row=2, column=3)
btnminus = Button(root, text="-", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick("-")).grid(row=3, column=3)
btnmulti = Button(root, text="*", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick("*")).grid(row=4, column=3)
btndiv = Button(root, text="/", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick("/")).grid(row=5, column=3)
btndot = Button(root, text=".", padx=16, font=("Arial", 16), width=4, command=lambda:btnClick(".")).grid(row=5, column=0)
btnclear = Button(root, text="Clear", padx=16, font=("Arial", 16), width=4, command=btnClearDisplay).grid(row=5, column=2)
btnequals = Button(root, text="=", padx=16, font=("Arial", 16), width=26, command=btnEqualsInput).grid(row=6, columnspan=4)
    
#########################################Buttons###############################################

root.mainloop()