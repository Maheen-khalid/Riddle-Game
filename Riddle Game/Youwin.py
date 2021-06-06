import tkinter
import tkinter.messagebox
import tkinter.font as font
window=tkinter.Tk()


window.configure(bg='blue')
#Setting font size
myFont = font.Font(family = "Comic Sans MS",size=20,weight='bold')

var=tkinter.Label(window,text="Congratulations !!",bg='blue',fg='yellow')
var2=tkinter.Label(window,text="You have scored",bg='blue',fg='yellow')
var3=tkinter.Label(window,text="10/10",bg='blue',fg='yellow')

var['font'] = myFont
var2['font']= myFont
var3['font']= myFont

var.place(x=30,y=20)
var2.place(x=30,y=60)
var3.place(x=60,y=100)

#setting Window's geometry
window.geometry("300x300")
window.mainloop()
