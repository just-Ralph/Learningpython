from tkinter import *
import math

import os 
os.system('clear')



root = Tk()

root.title('Scientific Calculator')


display = Entry(root, width=25, borderwidth=5, font=('Times New Roman', 16), justify='right')
display.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

def clear():
	display.delete(0, END)

def click(number):
	current = display.get()
	display.delete(0, END)
	display.insert(0,str(current) + str(number))
	
def add():
	first_number = display.get()
	global f_num 
	global math
	math = "addition"
	f_num = first_number
	display.delete(0, END)

def minus():
	first_number = display.get()
	global f_num 
	global math
	math = "subtraction"
	f_num = first_number
	display.delete(0, END)

def multiply():
	first_number = display.get()
	global f_num 
	global math
	math = "multiplication"
	f_num = first_number
	display.delete(0, END)

def divide():
	first_number = display.get()
	global f_num 
	global math
	math = "division"
	f_num = first_number
	display.delete(0, END)

def equal():
	second_number = display.get()
	display.delete(0, END)
	if math == 'addition':
		display.insert(0, f_num + second_number)
	elif math == 'subtraction':
		display.insert(0, f_num - second_number)
	elif math == 'multiplication':
		display.insert(0, f_num * second_number)
	elif math == 'division':
		display.insert(0, f_num / second_number)
	else:
		(0, END)





Button7 = Button(root, text=7, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(7))
Button8 = Button(root, text=8, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(8))
Button9 = Button(root, text=9, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(9))
Buttondivide = Button(root, text='/', width=5, height=2, font=('Times New Roman', 16), command=divide)

Button4 = Button(root, text=4, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(4))
Button5 = Button(root, text=5, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(5))
Button6 = Button(root, text=6,width=5, height=2, font=('Times New Roman', 16), command=lambda: click(6))
Buttonmultiply = Button(root, text='x', width=5, height=2, font=('Times New Roman', 16), command=multiply)

Button1 = Button(root, text=1, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(1))
Button2 = Button(root, text=2, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(2))
Button3 = Button(root, text=3, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(3))
Buttonsubtract = Button(root, text='-', width=5, height=2, font=('Times New Roman', 16), command=minus)

Button0 = Button(root, text=0, width=5, height=2, font=('Times New Roman', 16), command=lambda: click(0))
Buttondot = Button(root, text='.', width=5, height=2, font=('Times New Roman', 16), command=lambda: click('.'))
Buttonclear = Button(root, text='C', width=5, height=2, font=('Times New Roman', 16), fg='red', command=clear)
Buttonadd = Button(root, text='+', width=5, height=2, font=('Times New Roman', 16), command=add)

Buttonsin = Button(root, text='sin', width=5, height=2, font=('Times New Roman', 16), command=lambda: click(sin))
Buttoncos = Button(root, text='cos', width=5, height=2, font=('Times New Roman', 16), command=lambda: click(cos))
Buttontan = Button(root, text='tan', width=5, height=2, font=('Times New Roman', 16), command=lambda: click(tan))
Buttonequal = Button(root, text='=', width=5, height=2, font=('Times New Roman', 16), command=equal)






Button7.grid(row=1, column=0, padx=5, pady=5)
Button8.grid(row=1, column=1, padx=5, pady=5)
Button9.grid(row=1, column=2, padx=5, pady=5)
Buttondivide.grid(row=1, column=3, padx=5, pady=5)

Button4.grid(row=2, column=0, padx=5, pady=5)
Button5.grid(row=2, column=1, padx=5, pady=5)
Button6.grid(row=2, column=2, padx=5, pady=5)
Buttonmultiply.grid(row=2, column=3, padx=5, pady=5)

Button1.grid(row=3, column=0, padx=5, pady=5)
Button2.grid(row=3, column=1, padx=5, pady=5)
Button3.grid(row=3, column=2, padx=5, pady=5)
Buttonsubtract.grid(row=3, column=3, padx=5, pady=5)

Button0.grid(row=4, column=0, padx=5, pady=5)
Buttondot.grid(row=4, column=1, padx=5, pady=5)
Buttonclear.grid(row=4, column=2, padx=5, pady=5)
Buttonadd.grid(row=4, column=3, padx=5, pady=5)

Buttonsin.grid(row=5, column=0, padx=5, pady=5)
Buttoncos.grid(row=5, column=1, padx=5, pady=5)
Buttontan.grid(row=5, column=2, padx=5, pady=5)
Buttonequal.grid(row=5, column=3, padx=5, pady=5)





root.mainloop()