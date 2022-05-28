from tkinter import *


window = Tk()
window.title('Calculator by DKING')
# window.geometry('300x500')
window.configure(bd=5)


def btn_click(number):
    global current
    current = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, current + str(number))

def btn_clear():
    entry.delete(0, END)
    message.config(text='')


def btn_add():
    global first_number
    global math
    math = 'addition'
    first_number = int(entry.get())
    # global f_num
    #f_num = int(first_number)
    entry.delete(0, END)

def btn_subtract():
    global first_number
    global math
    math = 'subtraction'
    first_number = int(entry.get())
    # global f_num
    # f_num = int(first_number)
    entry.delete(0, END)
def btn_multiply():
    global first_number
    global math
    math = 'multiplication'
    first_number = int(entry.get())
    # global f_num
    # f_num = int(first_number)
    entry.delete(0, END)
def btn_divide():
    global first_number
    global math
    math = 'divide'
    first_number = int(entry.get())
    # global f_num
    # f_num = int(first_number)
    entry.delete(0, END)

def btn_equal():
    try:
        second_number = entry.get()
        entry.delete(0, END)
        if math == 'addition':
            answer = first_number + int(second_number)
            message.configure(text=answer)
        if math == 'multiplication':
            answer = first_number * int(second_number)
            message.configure(text=answer)
        if math == 'subtraction':
            answer = first_number - int(second_number)
            message.configure(text=answer)
        if math == 'divide':
            answer = first_number / int(second_number)
            message.configure(text=answer)
    except ValueError:
        message.config(text='Calm down..')

# frame 1, slave of window
frame_1 = Frame(window)
frame_1.grid()

# entry, slave of frame 1

entry = Entry(frame_1, bd=5, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# message for displaying info, slave of frame 1
message = Label(frame_1,  font=('Arial',14 ), fg='red')

# buttons, slave of frame 1
button_1 = Button(frame_1, text='7', font='Arial', padx=30, pady=10, command=lambda: btn_click(7))
button_2 = Button(frame_1, text='8', font='Arial', padx=30, pady=10, command=lambda: btn_click(8))
button_3 = Button(frame_1, text='9', font='Arial', padx=30, pady=10, command=lambda: btn_click(9))
button_4 = Button(frame_1, text='4', font='Arial', padx=30, pady=10, command=lambda: btn_click(4))
button_5 = Button(frame_1, text='5', font='Arial', padx=30, pady=10, command=lambda: btn_click(5))
button_6 = Button(frame_1, text='6', font='Arial', padx=30, pady=10, command=lambda: btn_click(6))
button_7 = Button(frame_1, text='1', font='Arial', padx=30, pady=10, command=lambda: btn_click(1))
button_8 = Button(frame_1, text='2', font='Arial', padx=30, pady=10, command=lambda: btn_click(2))
button_9 = Button(frame_1, text='3', font='Arial', padx=30, pady=10, command=lambda: btn_click(3))
button_0 = Button(frame_1, text='0', font='Arial', padx=72, pady=10, command=lambda: btn_click(0))

clear_btn = Button(frame_1, text='C', font='Arial', padx=29, pady=10, command=lambda: btn_clear())
add_btn = Button(frame_1, text='+', font='Arial', padx=29, pady=10, command=btn_add)
multiply_btn = Button(frame_1, text='*', font='Arial', padx=31, pady=10, command=btn_multiply)
subtract_btn = Button(frame_1, text='-', font='Arial', padx=32, pady=10, command=btn_subtract)
divide_btn = Button(frame_1, text='/', font='Arial', padx=33, pady=10, command=btn_divide)
equal_btn = Button(frame_1, text='=', font='Arial', padx=30, pady=10, command=btn_equal)

# displaying buttons on screen
clear_btn.grid(row=1, column=0)
message.grid(row=1, column=1, columnspan=3)
add_btn.grid(row=2, column=3)
multiply_btn.grid(row=3, column=3)
subtract_btn.grid(row=4, column=3)
equal_btn.grid(row=5, column=2)
divide_btn.grid(row=5, column=3)


button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=5, column=0, columnspan=2)



window.mainloop()