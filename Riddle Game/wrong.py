import tkinter
import tkinter.messagebox
import tkinter.font as font
window=tkinter.Tk()

def nextr():
    window.destroy()
    import Mainpage

#Setting background Colour
window.configure(bg='black')

#Setting Font sizes
myFont = font.Font(family = "Comic Sans MS",size=20,weight='bold')
btnFont =font.Font(family = "Comic Sans MS",size=10,weight='bold')

#Headings
a=tkinter.Label(window,text='Wrong Answer !!',fg='red',bg='black')
a2=tkinter.Label(window,text='You Loose',fg='blue',bg='black')


#buttons
Btn=tkinter.Button(window,text='Try Again',width='10',height='2',command=nextr)
Btn2=tkinter.Button(window,text='Quit',width='10',height='2',command=window.destroy)


#positioning Headings and Setting fonts
a.place(x=40,y=20)
a['font'] = myFont
a2.place(x=65,y=70)
a2['font'] = myFont

#Positioning Buttons and Setting fonts
Btn.place(x=40,y=150)
Btn['font'] = btnFont
Btn2.place(x=180,y=150)
Btn2['font'] = btnFont

window.geometry("300x300")
window.mainloop()