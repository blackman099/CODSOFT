import random, string
from tkinter import *


root = Tk()
root.geometry("400x400")
root.title("Password Generator")

otpass = StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits,
             string.ascii_lowercase]


def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)
        password = password + random.choice(char_type)

    otpass.set(password)


pass_head = Label(root, text='Password Length', font='arial 12 bold').pack(pady=10)

pass_len = IntVar()
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font='arial 16').pack()


Button(root, command=randPassGen, text="Generate Password", font="Arial 10",  fg='black',
       padx=5, pady=5).pack(pady=20)

pass_label = Label(root, text='Random Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=otpass, width=24, font='arial 16').pack()


root.mainloop()