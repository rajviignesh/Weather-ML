from tkinter import *
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('WeatherDATA1.csv')


def plot1():
    fromdate = e1.get()
    a = fromdate.split('-')
    todate = e2.get()
    b = todate.split('-')
    print(a[0])
    df1 = pd.read_csv('WeatherDATA1.csv')
    col1 = btn2.get()
    # print(df1.loc[(df1['Year'] == int(a[2])) & (df1['Month'] == int(a[1])) & (df1['Date'] == int(a[0]))].index)

    index1 = df1.loc[(df1['Year'] == int(a[2])) & (df1['Month'] == int(a[1])) & (df1['Date'] == int(a[0]))].index[0]
    index2 = df1.loc[(df1['Year'] == int(b[2])) & (df1['Month'] == int(b[1])) & (df1['Date'] == int(b[0]))].index[0]

    print(index1)
    print(index2)
    df1 = df1.iloc[index1:index2 + 1]
    a = list(df1[col1])
    b = list(df1['Date'])
    c = list(df1['Month'])
    d = list(df1['Year'])
    e = []

    df2 = pd.DataFrame(columns=[col1, 'Date'])

    for i in range(len(b)):
        e.append(str(int(b[i])) + '-' + str(int(c[i])) + '-' + str(int(d[i])))
        df2.loc[i] = [a[i]] + [str(e[i])]

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, master)
    bar1.get_tk_widget().grid(row=7, column=4)
    df2.plot(kind='line', x='Date', y=col1, legend=True, ax=ax1)
    # ax1.set_title('Country Vs. GDP Per Capita')


master = Tk()
master.title("STAGE 2")
master.geometry('1200x720')
btn2 = StringVar()

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
btn = Button(master, text="PLOT", fg="black", bg="black", command=plot1)
btn.grid(row=5, column=4)
gumb4 = Radiobutton(master, bg="black", text="Average", value="Average", variable=btn2).grid(row=6, column=3)
gumb5 = Radiobutton(master, bg="black", text="Minimum", value="Minimum", variable=btn2).grid(row=6, column=4)
gumb6 = Radiobutton(master, bg="black", text="Maximum", value="Maximum", variable=btn2).grid(row=6, column=5)


master.mainloop()
