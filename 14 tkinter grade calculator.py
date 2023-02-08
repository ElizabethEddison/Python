from tkinter import *
root = Tk()
root.geometry('640x480')

def gradecalculator():
    if score.get() > 90:
        Answertext =Label(root, text ="Grade A")
        Answertext.pack()
    elif score.get() > 80:
        Answertext =Label(root, text ="Grade B")
        Answertext.pack()
    elif score.get() >70:
        Answertext =Label(root, text ="Grade C")
        Answertext.pack()
    elif score.get()  >60:
        Answertext =Label(root, text ="Grade D")
        Answertext.pack()
    elif score.get()  >50:
        Answertext =Label(root, text ="Grade E")
        Answertext.pack()
    elif score.get()  >40:
        Answertext =Label(root, text ="Grade F")
        Answertext.pack()
    else:
        Answertext =Label(root, text ="Ungraded")
        Answertext.pack()
    
label_1 = Label(root, text= "Please Enter score")
label_1.pack()
score=IntVar()
question1=Entry(root, textvariable = score, bg = "cyan")
question1.pack()
button_1= Button(root, text = "Enter", command =gradecalculator, bg = "cyan")
button_1.pack()

root.mainloop()
