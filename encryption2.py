from tkinter import *
from tkinter.ttk import *
import random
import pyperclip as pc
from tkinter import messagebox as ms
window = Tk()
window.title("PASSWORD GENERATOR")
window.geometry('360x300')
window.resizable(False,False)

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
key = "0101929"

def strcheck(*args):
    global rb, rad1, rad2, rad3
    if rb.get()==1:
        rad1.config(style="w.TRadiobutton")
        rad2.config(style="b.TRadiobutton")
        rad3.config(style="b.TRadiobutton")
    elif rb.get()==2:
        rad1.config(style="b.TRadiobutton")
        rad2.config(style="m.TRadiobutton")
        rad3.config(style="b.TRadiobutton")
    elif rb.get()==3:
        rad1.config(style="b.TRadiobutton")
        rad2.config(style="b.TRadiobutton")
        rad3.config(style="s.TRadiobutton")

def gen():
    global combo, password, txt1, stre, leng
    btn2.config(state="normal")
    btn3.config(state="normal")
    btn4.config(state="disabled")
    txt2.config(state="normal")
    txt2.delete(0, END)
    txt2.config(state="readonly")
    txt1.config(state="normal")
    txt1.delete(0, END)
    txt1.config(state="readonly")
    stre = int(rb.get())
    leng = int(combo.get())
    password = ""
    for i in range(0,leng):
        if stre==1:
            a = str(random.choice(lower))
            password+=a
        elif stre==2:
            a = str(random.choice(upper))
            password += a
        elif stre==3:
            a = str(random.choice(digits))
            password += a
    txt1.config(state="normal")
    txt1.insert(0,password)
    txt1.config(state="readonly")

def enc():
    global combo, password, txt1, stre, leng, encrypted, key
    btn4.config(state="normal")
    txt2.config(state="normal")
    txt1.config(state="normal")
    txt2.delete(0, END)
    txt2.config(state="readonly")
    stre = int(rb.get())
    leng = int(combo.get())
    txt1.delete(0, END)
    txt1.config(state="readonly")
    encrypted = password
    btn3.config(state="disabled")
    for i in range(0, leng):
        if i==0: kpos=0
        else: kpos+=1
        if kpos == 7: kpos = 0
        if stre == 1:
            encrypted1 = encrypted[0:i]
            encrypted2 = encrypted[(i+1):]
            char = password[i]
            pos1 = lower.find(char)
            pos2 = pos1 + int(key[kpos])
            if pos2 > 25: pos2-=26
            newchar = lower[pos2]
            encrypted = encrypted1 + newchar + encrypted2
        elif stre == 2:
            encrypted1 = encrypted[0:i]
            encrypted2 = encrypted[(i + 1):]
            char = password[i]
            pos1 = upper.find(char)
            pos2 = pos1 + int(key[kpos])
            if pos2 > 51: pos2 -= 52
            newchar = upper[pos2]
            encrypted = encrypted1 + newchar + encrypted2
        elif stre == 3:
            encrypted1 = encrypted[0:i]
            encrypted2 = encrypted[(i + 1):]
            char = password[i]
            pos1 = digits.find(char)
            pos2 = pos1 + int(key[kpos])
            if pos2 > 71: pos2 -= 72
            newchar = digits[pos2]
            encrypted = encrypted1 + newchar + encrypted2
    txt2.config(state="normal")
    txt2.insert(0, encrypted)
    txt2.config(state="readonly")

def copy():
    pc.copy(password)

def exit():
    a = ms.askyesno("ALERT","ARE YOU SURE YOU WANT TO EXIT?")
    if a: window.destroy()

def dec():
    btn3.config(state="enabled")
    btn4.config(state="disabled")
    txt1.config(state="normal")
    txt1.insert(0,password)
    txt1.config(state="readonly")
    txt2.config(state="normal")
    txt2.delete(0, END)
    txt2.config(state="readonly")

style0 = Style(window)
style0.configure("My.TButton", font=("Segoe UI",10))
style1 = Style(window)
style1.configure("w.TRadiobutton",foreground="green")
style2 = Style(window)
style2.configure("m.TRadiobutton",foreground="orange")
style3 = Style(window)
style3.configure("s.TRadiobutton",foreground="red")
styleb = Style(window)
styleb.configure("b.TRadiobutton",foreground="black")

lbl0 = Label(window,text=" PASSWORD ",font=("Segoe UI",25),borderwidth=20,relief="groove")
lbl0.place(x=10,y=10)
lbl1 = Label(window,text="STRENGTH:",font=("Segoe UI",15,"underline"))
lbl1.place(x=15,y=100)
lbl2 =Label(window,text="LENGTH:",font=("Segoe UI",15,"underline"))
lbl2.place(x=15,y=130)
lbl3 = Label(window,text="⤷",font=(120))
lbl3.place(x=25,y=70)
lbl4 = Label(window,text="⤶",font=(120))
lbl4.place(x=280,y=220)
lbl5 = Label(window,text="⮧",font=(120))
lbl5.place(x=230,y=20)

btn1 = Button(window,text=" ~generate~ ",style="My.TButton",command=gen)
btn1.place(x=15,y=180)
btn2 = Button(window,text=" ~copy_pass~ ",style="My.TButton", command=copy,state="disabled")
btn2.place(x=117,y=180)
btn3 = Button(window,text=" ~encrypt~ ",style="My.TButton",command=enc,state="disabled")
btn3.place(x=225,y=180)
btn4 = Button(window,text=" ~decrypt~ ",style="My.TButton",command=dec,state="disabled")
btn4.place(x=15,y=260)
btn5 = Button(window,text=" ~exit~ ",style="My.TButton",command=exit)
btn5.place(x=115,y=260)

combo = Combobox(window,state="readonly")
combo["values"] = ("7","8","9","10","11","12","14")
combo.current("3")
combo.place(x=130,y=137)

rb = IntVar()
rb.set("2")
rad1 = Radiobutton(window, text="Weak",value="1",variable=rb,command=strcheck)
rad1.place(x=130,y=105)
rad2 = Radiobutton(window, text="Medium",value="2",variable=rb,style="m.TRadiobutton",command=strcheck)
rad2.place(x=190,y=105)
rad3 = Radiobutton(window, text="Strong",value="3",variable=rb,command=strcheck)
rad3.place(x=265,y=105)

txt1 = Entry(window,width=25,font=("SegoeUI"),state="readonly")
txt1.place(x=60,y=70)
txt2 = Entry(window,width=22,font=("SegoeUI"),state="readonly")
txt2.place(x=15,y=220)

window.mainloop()