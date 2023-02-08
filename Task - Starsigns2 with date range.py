from tkinter import *

root = Tk()
root.geometry('500x500')
root.configure(bg = "green")

root.title("Star Sign Checker")

def Starsign():
    if givenanswer.get() == "January":
        if givenanswer2.get() <= 19:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Capricorn", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
            
        elif givenanswer2.get() >= 20 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign =Label(root, text = "Your starsign is Aquarius", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            
    elif givenanswer.get() == "Feburary":
        if givenanswer2.get() <=18:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Aquarius", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=19 and  givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Pisces", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
            
    elif givenanswer.get() == "March":
        if givenanswer2.get() <=20:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Pisces", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=21 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Aries", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
            
    elif givenanswer.get() == "April":
        if givenanswer2.get() <=20:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Aries", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get()  <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Taurus", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
            
    elif givenanswer.get() == "May":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Taurus", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Gemini", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
            
    elif givenanswer.get() == "June":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Gemini", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Cancer", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "July":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Cancer", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Leo", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "August":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Leo", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Virgo", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "September":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Virgo", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Libra", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "October":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Libra", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Scorpio", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "November":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Scorpio", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Sagittarius", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)

    elif givenanswer.get() == "December":
        if givenanswer2.get() <=21:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Sagittarius", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)
        elif givenanswer2.get() >=22 and givenanswer2.get() <=31:
            starsign =Label(root, text = "                                                                ", bg = "green", fg = "yellow", font = ("arial", 14)).place(x = 125, y = 200)
            starsign = Label(root, text = "Your star sign is Capricorn", bg = "green",fg = "yellow", font = ("arial",14)).place(x = 125, y = 200)


question = Label(root, text = "What is your month of birth?", bg = "green",  fg = "yellow", font = ("arial",14) ).pack()
givenanswer = StringVar()
answer = Entry(root, textvariable = givenanswer, fg = "blue", font = ("arial",14)).pack()
question2 = Label(root, text = "What is your day of birth?", bg = "green", fg = "yellow", font = ("arial", 14)).pack()
givenanswer2 =IntVar()
answer2 = Entry(root, textvariable = givenanswer2, fg = "blue", font = ("arial", 14)). pack()
button = Button(root, text = "Click Me", command = Starsign, bg = "magenta", font=("arial", 14)).pack()





root.mainloop()
