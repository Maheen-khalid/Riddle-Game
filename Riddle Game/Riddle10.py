import tkinter
import tkinter.messagebox
import tkinter.font as font
window2=tkinter.Tk()

def wrong():
    window2.destroy()
    import wrong

def nextr():
    window2.destroy()
    import Youwin


window2.configure(bg='black')
myFont = font.Font(family = "Comic Sans MS",size=12,weight='bold')
    
    
    #Riddle
a=tkinter.Label(window2,text='How many months has ',fg='yellow',bg='black')
a2=tkinter.Label(window2,text="28days?",fg='yellow',bg='black')

    #Options
opt1=tkinter.Button(window2,text='2'  ,command=wrong, width='30',bg='red')
opt2=tkinter.Button(window2,text='3',command=wrong, width='30',bg='green')
opt3=tkinter.Button(window2,text='All months',command=nextr, width='30',bg='purple')
opt4=tkinter.Button(window2,text='1',command=wrong , width='30',bg='blue')
    
    
    
    
opt1.place(x=55,y=140)
opt2.place(x=55,y=180)
opt3.place(x=55,y=220)
opt4.place(x=55,y=260)
a.place(x=70,y=30)
a2.place(x=120,y=70)

a['font'] = myFont
a2['font'] = myFont

    
window2.geometry("350x500")
window2.mainloop()
    