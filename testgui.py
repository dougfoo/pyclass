from tkinter import *
 
def clicked():
    lbl.configure(text=txt1.get())

window = Tk()
 
window.title("Welcome to LikeGeeks app")

txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)

txt2 = Entry(window,width=10)
txt2.grid(column=2, row=0)

add = Button(window, text="Add", command=clicked) 
add.grid(column=3, row=0)

sub = Button(window, text="Sub", command=clicked) 
sub.grid(column=3, row=1)

mult = Button(window, text="Mult", command=clicked) 
mult.grid(column=3, row=2)

div = Button(window, text="Div", command=clicked) 
div.grid(column=3, row=3)

lbl = Label(window, text="Results", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

txt0 = Entry(window,width=10)
txt0.grid(column=0, row=1)

window.mainloop()

