import tkinter as tk
import time
import speedtest
from tkinter import messagebox
r=Tk()
r.title("speed test")

L1= Label(r, text='download speed')
L1.grid(row=1, column=0)
e1= Entry(r, bd=5)
e1.grid(row=1, column=1)

L2= Label(r, text="upload speed")
L2.grid(row=2, column=0)
e2= Entry(r, bd=5)
e2.grid(row=2, column=1)

l3= Label(r, text='ping ')
l3.grid(row=3, column=0)
e3= Entry(r, bd=5)
e3.grid(row=3, column=1)

def check():
    st = speedtest.Speedtest()
    download = st.download()
    upload = st.upload()
    e1.insert(0,download//10**6,"Mbps")
    e2.insert(0,upload//10**6,"Mbps")
    e3.insert(0,int(st.results.ping),"MS")


b1 = tkinter.Button(text='CHECK', width=10, bg='#c3ff01', command=check)
b1.grid(row=4, column=2)
          
