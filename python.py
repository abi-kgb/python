
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
#creating window
win1= Tk()
win1.geometry('600x600')
win1.title("denomination calculator")
#uploading image
upload=Image.open("image.jpg")
image=ImageTk.PhotoImage(upload)
L0=Label(win1,image=image)#win1 is name and image is inbuild = image is name
L0.pack()
#label
l1=Label(win1,text="Hello user! welcome to denominatior calculator",font=20)
l1.place(x=140,y=400)

#to get alter box
def alert():
    msgbox=messagebox.showinfo("alert","if you want to use denomination calculator click ok..")
    if msgbox=='ok':
        win2()

#button lets get started
add = Button(win1,text="Lets get started",command=alert,background='yellow',fg='blue')
add.place(x=240 ,y=450)

def win2():
#win2 after clicking ok
    cal=Tk()
    cal.title("calculator")
    cal.geometry('500x500')

#enter amount
    label1=Label(cal,text="Enter amout:")
    label1.place(x=20,y=20)
    en1=Entry(cal)
    en1.place(x=100,y=20)

    label2 = Label(cal, text="2000:")
    label2.place(x=20, y=120)
    en2 = Entry(cal)
    en2.place(x=100, y=120)

    label3 = Label(cal, text="1000:")
    label3.place(x=20, y=160)
    en3 = Entry(cal)
    en3.place(x=100, y=160)

    label4 = Label(cal, text="500:")
    label4.place(x=20, y=200)
    en4 = Entry(cal)
    en4.place(x=100, y=200)

    def calculate():
        global amt
        amt = int(en1.get())
        amt1=amt//2000
        en2.insert(END,str(amt1))
        
        amt=int(amt)%2000
        amt2=amt//1000
        en3.insert(END,str(amt2))
        
        amt=int(amt)%1000
        amt3=amt//500
        en4.insert(END,str(amt3))
        
# add button to calcutor
    add = Button(cal,text="calculate",command=calculate)
    add.place(x=80,y=60)

    


    cal.mainloop()

win1.mainloop()
