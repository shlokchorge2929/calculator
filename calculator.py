from tkinter import *

# Assigning top widget and title

def buttonClick(number):
    global operator
    operator = operator + str(number)   #append the button on display ; so multiple click build expression
    input_value.set(operator)  # so that user could see the no. on display


def clearButton():
    global operator
    operator=""
    input_value.set("")     #giving empty set cause whenever clicked will clear display
    
def   buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)               
    operator=""                # used to clear operator on display

main = Tk()
main.title("Calculator")



operator =""   



# creating display of calculator , giving font ,giving color, etc.

input_value = StringVar()
display_text=Entry( main,font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="black",justify=RIGHT,fg="white")
display_text.grid(columnspan=4)

# creating row 1 (7,8,9,+):

button_7 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="7",bg = "dark grey", command=lambda: buttonClick(7))
button_7.grid(row=1,column=0 )     # here row 0 not used  because 0 is for display

button_8 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="8",bg = "dark grey", command=lambda: buttonClick(8))
button_8.grid(row=1,column=1)

button_9 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="9",bg = "dark grey", command=lambda: buttonClick(9))
button_9.grid(row=1,column=2)

button_add= Button(main,padx=16,bd=8,fg="white", font=("arial",20,"bold"),text="+",bg="orange", command=lambda: buttonClick("+"))  
button_add.grid(row=1,column=3)

# creating row 2 (4,5,6,-)

button_4 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="4",bg = "dark grey", command=lambda: buttonClick(4),)
button_4.grid(row=2,column=0)

button_5 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="5",bg = "dark grey", command=lambda: buttonClick(5))
button_5.grid(row=2,column=1)

button_6 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="6",bg = "dark grey", command=lambda: buttonClick(6))
button_6.grid(row=2,column=2)

button_sub= Button(main,padx=16,bd=8,fg="white", font=("arial",20,"bold"),text="-",bg="orange", command=lambda: buttonClick("-"))  
button_sub.grid(row=2,column=3)

# row 3 (1,2,3,x)

button_1 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="1",bg = "dark grey", command=lambda: buttonClick(1))
button_1.grid(row=3,column=0)

button_2 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="2",bg = "dark grey", command=lambda: buttonClick(2))
button_2.grid(row=3,column=1)

button_3 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="3",bg = "dark grey", command=lambda: buttonClick(3))
button_3.grid(row=3,column=2)


button_mul= Button(main,padx=16,bd=8,fg="white", font=("arial",20,"bold"),text="x",bg="orange", command=lambda: buttonClick("*"))  
button_mul.grid(row=3,column=3)

# row 4 (0,clear[c],=,/)

button_0 = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="0",bg = "dark grey", command=lambda: buttonClick(0))
button_0.grid(row=4,column=0)

button_clear = Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="C",bg = "dark grey",command=clearButton)
button_clear.grid(row=4,column=1)

button_equal= Button(main,padx=16,bd=8,fg="black", font=("arial",20,"bold"),text="=",bg = "dark grey", command=buttonEqual)
button_equal.grid(row=4,column=2)

button_div= Button(main,padx=16,bd=8,fg="white", font=("arial",20,"bold"),text="/",bg="orange", command=lambda: buttonClick("/"))  
button_div.grid(row=4,column=3)






main.mainloop()  # this will let my cal work on loop