from tkinter import *
from tkinter.ttk import Progressbar
import time 
def close():
    root.destroy()
root = Tk()
root.geometry('600x250+230+220')
root.config(bg="black")
root.title("PROGRESS BAR")
progress = Progressbar(root, orient = HORIZONTAL,length = 350)
progress.place(x=100,y=110)
lb=Label(root,text='STARTING..........',bg="black",fg="white",font=("Arial",20))
lb.place(x=200,y=60)
lb1=Label(root,text='0%',bg="black",fg="white",font=("Arial",20))
lb1.place(x=250,y=150)
def bar(): 
        for i in range(1,101,1):
                progress['value'] = i
                root.update_idletasks() 
                time.sleep(.001)
                s=str(i)+" %"
                lb1.config(text= s)
root.after(3000,close)
root.after(1000,bar)
root.mainloop()
import ak_welcome_screen