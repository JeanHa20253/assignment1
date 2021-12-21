import pyperclip
from tkinter import *
# text= input('What is your message? \n')

LETTER=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ']
MORSED_LETTER= ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__','_.','___','.__.','__._',"_._",'...','_','.._','..._','.__',"_.._",'_.__','__..','.____' , '..___' ,'...__' ,'...._' ,'.....' ,'_....' ,'__...' ,'___..' ,'____.' ,'_____','|']

def encrypt(text):
    pure_lettter = LETTER
    morsed_letter = MORSED_LETTER
    text_list= list(text.lower())
    morsed_text=[]

    for letter in text_list:
        if letter in pure_lettter:
            morsed_text.append(morsed_letter[pure_lettter.index(letter)])
        else:
            morsed_text.append(letter)

    code= ' '.join(morsed_text)
    canvas.itemconfig(big_title, text=code,font="Times 10 bold",fill='white')
    canvas.itemconfig(notification, text='Morse code is copied to clipboard')
    pyperclip.copy(code)



def save():
    text= e1.get("1.0",'end-1c')
    encrypt(text)


def reset():
    canvas.itemconfig(big_title,fill="#F5E8C7",
                   font="Courier 35 bold", text="LET'S HAVE YOUR MESSAGE ENCYPTED.")
    canvas.itemconfig(notification, text='')
    e1.delete("1.0","end")


# ----------------------------------------UI-------------------------------------
window = Tk()

# by default the size of window is 0?
window.minsize(width=100, height=100)
window.title('Morse Converter')

canvas= Canvas(width=1200, height=700, highlightthickness=0)


image = PhotoImage(file='ui.png')
canvas.create_image(600,300,image=image)

big_title= canvas.create_text(600,
                   80,
                    fill="#F5E8C7",
                   font="Courier 35 bold",
                    text="LET'S HAVE YOUR MESSAGE ENCRYPTED.")

e1= Text(canvas)
e1.configure(background='#F7D59C')
input= canvas.create_window(600,300,window = e1, width=500, height=300)


label1= canvas.create_text(290,
                   160,
                    fill="#C7B198",
                   font="Times 14",
                    text="Your message: ")

button1 = Button(text = "Encrypt", command = save)
button1.configure(width = 10, activebackground = "#66806A", background='#66806A',foreground='white', relief = FLAT)
button1_window = canvas.create_window(500, 500,anchor='center', window=button1)

button2 = Button(text = "Again", command = reset)
button2.configure(width = 10, background='#A45D5D', activebackground = "#A45D5D",foreground='#FFC069')
button2_window = canvas.create_window(650, 500,anchor='center', window=button2)

notification= canvas.create_text(600,
                   600,
                    fill="white",
                   font="Times 14",
                    text="")


canvas.grid(row=0,column=0, columnspan=4)


window.mainloop()
