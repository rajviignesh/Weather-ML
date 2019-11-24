from tkinter import *
from tkinter import messagebox


def plot1():
    fromdate = e1.get()
    a = fromdate.split('-')
    todate = e2.get()
    b = todate.split('-')


master = Tk()
master.title("STAGE 2")
master.geometry('1200x720')

# te1 =Label(master, text="       ").grid(row=0)
te2 = Label(master, text="       ").grid(row=1)
te3 = Label(master, text="       ").grid(row=2, column=1)
te4 = Label(master, text="       ").grid(row=2, column=2)
te5 = Label(master, text="       ").grid(row=2, column=3)
te6 = Label(master, text="       ").grid(row=2, column=4)
t1 = Label(master, text="WEATHER STATISTICS", bg="yellow", fg="black").grid(row=2, column=4)
te7 = Label(master, text="       ").grid(row=3)
te8 = Label(master, text="       ").grid(row=4, column=1)
t2 = Label(master, text="FROM DATE", fg="black").grid(row=4, column=2)
e1 = Entry(master)
e1.grid(row=4, column=3)
t2 = Label(master, text="TO DATE", fg="black").grid(row=4, column=5)
e2 = Entry(master)
e2.grid(row=4, column=6)
btn = Button(master, text="PLOT", command=plot1)
btn.grid(row=5, column=4)


master.mainloop()
