from tkinter import *
root=Tk()
root.geometry("420x600")
root.title("calculator")
root.resizable(False,False)
def click(event):
    global scval
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            value=eval(scval.get())
            mainscreen.update()
        scval.set(value)
        mainscreen.update()

    elif text=="C":
        scval.set("")
        mainscreen.update()
    else:
        scval.set(scval.get()+ text)
        mainscreen.update()

#main output screen
scval=StringVar()
scval.set("")
mainscreen=Entry(root,text=scval,font="comicsansms 30 bold",bg="grey",)
mainscreen.pack(fill=X,pady=20,ipady=40)

#buttons alignment
f1=Frame(root,bg="grey",)
b=Button(f1,text="9",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="nw",padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="8",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="nw",padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="7",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="nw",padx=5,pady=5)
b.bind("<Button-1>",click)
f1.place(x=10,y=160)


#button alignment2
f1=Frame(root,bg="grey")
b=Button(f1,text="6",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="w",padx=5,pady=9)
b.bind("<Button-1>",click)

b=Button(f1,text="5",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="w",padx=5,pady=9)
b.bind("<Button-1>",click)

b=Button(f1,text="4",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(side=LEFT,anchor="w",padx=5,pady=9)
b.bind("<Button-1>",click)
f1.place(x=10,y=260)

#3rd alignment
f1=Frame(root,bg="grey")
b=Button(f1,text="3",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(anchor="sw",side=LEFT,padx=5,pady=9)
b.bind("<Button-1>",click)

b=Button(f1,text="2",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(anchor="sw",side=LEFT,padx=5,pady=9)
b.bind("<Button-1>",click)

b=Button(f1,text="1",font="lucida 25 bold",padx=11,pady=11,borderwidth=5)
b.pack(anchor="sw",side=LEFT,padx=5,pady=9)
b.bind("<Button-1>",click)
f1.place(x=10,y=360)

#4th alignment
f1=Frame(root,bg="grey")
b=Button(f1,text="C",font="lucida 31 bold",padx=31,pady=15,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5)
b.bind("<Button-1>",click)
f1.place(x=270,y=160)

#5th alignment
f1=Frame(root,bg="grey")
b=Button(f1,text="+",font="lucida 22 bold",padx=7,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,)
b.bind("<Button-1>",click)
f1.place(x=270,y=290)


f1=Frame(root,bg="grey")
b=Button(f1,text="-",font="lucida 25 bold",padx=8,pady=5,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,)
b.bind("<Button-1>",click)
f1.place(x=270,y=380)

f1=Frame(root,bg="grey")
b=Button(f1,text="*",font="lucida 22 bold",padx=11,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,)
b.bind("<Button-1>",click)
f1.place(x=340,y=290)

f1=Frame(root,bg="grey")
b=Button(f1,text="/",font="lucida 23 bold",padx=11,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,)
b.bind("<Button-1>",click)
f1.place(x=340,y=380)

#6th alignment
f2=Frame(root,bg="grey")
b=Button(f2,text="0",font="lucida 23 bold",padx=9,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f2,text="00",font="lucida 23 bold",padx=9,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f2,text=".",font="lucida 23 bold",padx=14,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,side=LEFT)
b.bind("<Button-1>",click)
f2.place(x=10,y=480,)

#7th button alignment
f3=Frame(root,bg="grey")
b= Button(f3,text="=",font="lucida 23 bold",padx=40,pady=7,borderwidth=5)
b.pack(anchor="sw",padx=5,pady=5,side=LEFT)
b.bind("<Button-1>",click)
f3.place(x=270,y=480)


root.mainloop()
