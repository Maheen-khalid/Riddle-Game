import tkinter
import tkinter.messagebox
import tkinter.font as font
window2=tkinter.Tk()

def wrong():
    window2.destroy()
    import wrong

def nextr():
    window2.destroy()
    import Riddle7


window2.configure(bg='black')
myFont = font.Font(family = "Comic Sans MS",size=12,weight='bold')
    
    
    #Riddle
a=tkinter.Label(window2,text='Say my name and I am no,',fg='yellow',bg='black')
a2=tkinter.Label(window2,text="more",fg='yellow',bg='black')

    
    #Options
opt1=tkinter.Button(window2,text='Devil'  ,command=wrong, width='30',bg='red')
opt2=tkinter.Button(window2,text='God',command=wrong, width='30',bg='green')
opt3=tkinter.Button(window2,text='Dog',command=wrong, width='30',bg='purple')
opt4=tkinter.Button(window2,text='Silence',command=nextr , width='30',bg='blue')
    
    
    
    
opt1.place(x=55,y=130)
opt2.place(x=55,y=170)
opt3.place(x=55,y=210)
opt4.place(x=55,y=250)
a.place(x=60,y=30)
a2.place(x=120,y=60)

a['font'] = myFont
a2['font'] = myFont

    
window2.geometry("350x500")
window2.mainloop()