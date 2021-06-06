import tkinter
import tkinter.messagebox
import tkinter.font as font
window2=tkinter.Tk()

def wrong():
    window2.destroy()
    import wrong

def nextr():
    window2.destroy()
    import Riddle5


window2.configure(bg='black')
myFont = font.Font(family = "Comic Sans MS",size=12,weight='bold')
    
    
    #Riddle
a=tkinter.Label(window2,text='I am in Life but not in death,',fg='yellow',bg='black')
a2=tkinter.Label(window2,text="You can't have fun without me",fg='yellow',bg='black')
a3=tkinter.Label(window2,text='Who I am?',fg='yellow',bg='black')
    
    #Options
opt1=tkinter.Button(window2,text='F'  ,command=nextr, width='30',bg='red')
opt2=tkinter.Button(window2,text='E',command=wrong, width='30',bg='green')
opt3=tkinter.Button(window2,text='Children',command=wrong, width='30',bg='purple')
opt4=tkinter.Button(window2,text='Darkness',command=wrong , width='30',bg='blue')
    
    
    
    
opt1.place(x=55,y=130)
opt2.place(x=55,y=170)
opt3.place(x=55,y=210)
opt4.place(x=55,y=250)
a.place(x=60,y=10)
a2.place(x=30,y=40)
a3.place(x=120,y=70)
a['font'] = myFont
a2['font'] = myFont
a3['font'] = myFont
    
window2.geometry("350x500")
window2.mainloop()