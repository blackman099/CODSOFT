from tkinter import*

root=Tk()
root.geometry("400x450")
root.resizable(False,False)
root.title("To-Do list")


def add():
    task= entryw.get()
    if task !="":
        list.insert(END,task)
        entryw.delete(0,"end")

def Del():
     list.delete(ANCHOR)

# content display
main=Frame(root)
main.pack(pady=19)
list=Listbox(main,width=26,height=11,font="lucida 13",highlightthickness=0,selectbackground="grey")
list.pack(side=LEFT,fill=BOTH)

# content
task=[ ""]
for item in task:
    list.insert(END,item)

# scrollbar y axis
scrollb=Scrollbar(main)
scrollb.pack(side=RIGHT,fill=BOTH)
list.config(yscrollcommand=scrollb.set)
scrollb.config(command=list.yview)

# entry widget
entryw=Entry(root,font="lucida,13")
entryw.pack(pady=10)

# button widget
buttonfr=Frame(root)
buttonfr.pack(pady=10)

addb=Button(buttonfr,text="ADD",font="lucida 15 bold",command=add)
addb.pack(side=LEFT,pady=8,padx=10)
delb=Button(buttonfr,text="DELETE",font="lucida  15 bold",command=Del)
delb.pack(side=RIGHT,pady=8,padx=10)

root.mainloop()