from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("Timer")
root.geometry("270x220")
root.resizable(0,0)
canvas=Canvas(root,width = 270, height = 220)
canvas.pack()
icon = PhotoImage(file='C:\Images\stopwatch.png')
root.iconphoto(False, icon)


def countdown():
    try:
        t = int(entry.get())
        while t:
             mins, secs = divmod(t, 60)
             timer = '{:02d}:{:02d}'.format(mins, secs)
             time.sleep(1)
             t = t-1
        messagebox.showinfo('Successful', "Timer completed!!!")
    except:
        messagebox.showerror('Error', "Please enter a time!!!")

entry = Entry(root,bd=5, background ='#000000',width = 5, bg='#c9d1cf', fg='#000000')
entry.place(x=207,y=78)
img = PhotoImage(file='C:\Images\Blue.png')
canvas.create_image(270,220,image=img,anchor='center')
label = Label(root,font=('open sans', 10, 'bold'),text="Enter the time in seconds: ",bg='#000000',
              fg='#ffffff').place(x=30,y=80)
button = Button(text="Start", width='6', font=('open sans', 12, 'bold'),bg='#000000',
                fg='#ffffff',command=countdown)
canvas.create_window(133,130,window=button)
root.mainloop()