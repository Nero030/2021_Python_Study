from tkinter import *

window = Tk()
window.title('거듭제곱이 포함된 계산기 202037636 이강현')

display = Entry(window, width = 50)

display.grid(row = 0, column = 0, columnspan = 4)


#####################################################

n = 0
key = 'calc'

def num_ins(num) :
    if key == 'equ' :
        display.delete(0, END)

    ins = display.get()
    display.delete(0, END)
    display.insert(0, str(ins) + str(num))

def num_clear() :
    display.delete(0, END)

def num_sum() :
    global n
    global key
    n = int(display.get())
    key = 'sum'
    display.delete(0, END)

def num_sub() :
    global n
    global key
    n = int(display.get())
    key = 'sub'
    display.delete(0, END)

def num_mult() :
    global n
    global key
    n = int(display.get())
    key = 'mult'
    display.delete(0, END)

def num_div() :
    global n
    global key
    n = int(display.get())
    key = 'div'
    display.delete(0, END)

def num_squ() :
    global n
    global key
    n = int(display.get())
    key = 'squ'
    display.delete(0, END)


def num_equ() :
    m = display.get()
    display.delete(0, END)
    global key
    if key == 'sum' :
        display.insert(0, n + int(m))
    if key == 'sub' :
        display.insert(0, n - int(m))
    if key == 'mult' :
        display.insert(0, n * int(m))
    if key == 'div' :
        display.insert(0, int(n / int(m)))
    if key == 'squ' :
        display.insert(0, n ** int(m))
    key = 'equ'


#####################################################


b1 = Button(window, text = '1', width = 10, command = lambda : num_ins(1))
b2 = Button(window, text = '2', width = 10, command = lambda : num_ins(2))
b3 = Button(window, text = '3', width = 10, command = lambda : num_ins(3))
b4 = Button(window, text = '+', width = 10, command = num_sum)

b5 = Button(window, text = '4', width = 10, command = lambda : num_ins(4))
b6 = Button(window, text = '5', width = 10, command = lambda : num_ins(5))
b7 = Button(window, text = '6', width = 10, command = lambda : num_ins(6))
b8 = Button(window, text = '-', width = 10, command = num_sub)

b9 = Button(window, text = '7', width = 10, command = lambda : num_ins(7))
b10 = Button(window, text = '8', width = 10, command = lambda : num_ins(8))
b11 = Button(window, text = '9', width = 10, command = lambda : num_ins(9))
b12 = Button(window, text = '*', width = 10, command = num_mult)

b13 = Button(window, text = 'C', width = 10, command = num_clear)
b14 = Button(window, text = '0', width = 10, command = lambda : num_ins(0))
b15 = Button(window, text = '=', width = 10, command = num_equ)
b16 = Button(window, text = '/', width = 10, command = num_div)

b17 = Button(window, text = '**', width = 10, command = num_squ)

#####################################################

b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 1, column = 3)

b5.grid(row = 2, column = 0)
b6.grid(row = 2, column = 1)
b7.grid(row = 2, column = 2)
b8.grid(row = 2, column = 3)

b9.grid(row = 3, column = 0)
b10.grid(row = 3, column = 1)
b11.grid(row = 3, column = 2)
b12.grid(row = 3, column = 3)

b13.grid(row = 4, column = 0)
b14.grid(row = 4, column = 1)
b15.grid(row = 4, column = 2)
b16.grid(row = 4, column = 3)

b17.grid(row = 5, column = 0)

#####################################################

window.mainloop()