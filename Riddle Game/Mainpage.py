import tkinter
import tkinter.messagebox
import tkinter.font as font
window=tkinter.Tk()


def nextr():
    window.destroy()
    import Riddle1


#main screen
window.configure(bg='blue')
#Setting font size
myFont = font.Font(family = "Comic Sans MS",size=20,weight='bold')

#headings
var=tkinter.Label(window,text="Tricky Riddles & Brain Teasers",bg='blue',fg='yellow')
var2=tkinter.Label(window,text="To Workout Your Mind !!",bg='blue',fg='yellow')

#buttons
Btn=tkinter.Button(window,text='Get Started',command=nextr)
Btn2=tkinter.Button(window,text='Quit',command=window.destroy)

var['font'] = myFont
var2['font']= myFont

Btn['font'] = myFont
Btn2['font']= myFont

#Setting Positions of buttons and heading
Btn.place(x=60,y=180)
Btn2.place(x=300,y=180)
var.place(x=50,y=20)
var2.place(x=70,y=60)


#setting Window's geometry
window.geometry("500x500")
window.mainloop()
