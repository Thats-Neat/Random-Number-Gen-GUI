import tkinter
import time
import random

def onPress():

    try:
        min = minInput.get()
        max = maxInput.get()
        number = random.randint(int(min), int(max))

        num.config(text=number)

    except ValueError:
        num.config(text='Please Enter Valid Numbers')

window = tkinter.Tk()

window.iconbitmap('gear.ico')

window.title('Random Number')
window.geometry('700x600')
window.resizable(width=False, height=False)
window.config(background='lightgray')


title = tkinter.Label(text='Random Number Generator')
title.place(x=100, y=20)
title.config(font=('Times New Roman', 30, 'bold'), background='lightgray')

minTxt = tkinter.Label(text='Minimum')
minTxt.place(x=260, y=100)
minTxt.config(font=('Times New Roman', 23, 'bold'), background='lightgray')

maxTxt = tkinter.Label(text='Maximum')
maxTxt.place(x=260, y=200)
maxTxt.config(font=('Times New Roman', 23, 'bold'), background='lightgray')

minInput = tkinter.Entry()
minInput.place(x=255, y=145)
minInput.config(font=('Times New Roman', 10, 'bold'))

maxInput = tkinter.Entry()
maxInput.place(x=255, y=245)
maxInput.config(font=('Times New Roman', 10, 'bold'))

button = tkinter.Button(text='Confirm', command=onPress)
button.place(x=280, y=325)
button.config(font=100, height=2, width=10)

num = tkinter.Label(text='')
num.place(x=330, y=450, anchor='center')
num.config(font=('Times New Roman', 20, 'bold'), background='lightgray')

window.mainloop()
