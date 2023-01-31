import datetime
import tkinter as tk

def getinput():
    name=nameentry.get()
    m1=Person(name,datetime.date(int(yearentry.get()),int(monthentry.get()),int(dateentry.get())))
    textarea=tk.Text(win,height=5,width=30)
    textarea.grid(column=1,row=6)
    answer="Hey {m1}!!! You are {age} years old.".format(m1=name,age=m1.age())
    textarea.insert(tk.END,answer)

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age

win=tk.Tk()
win.title('Age Calculator')
win.geometry("620x780")

name=tk.Label(text="Name")
name.grid(column=0,row=1,padx=5,pady=5)
year=tk.Label(text="Year")
year.grid(column=0,row=2,padx=5,pady=5)
month=tk.Label(text="Month")
month.grid(column=0,row=3,padx=5,pady=5)
date=tk.Label(text="Date")
date.grid(column=0,row=4,padx=5,pady=5)

nameentry=tk.Entry()
nameentry.grid(column=1,row=1,padx=20)
yearentry=tk.Entry()
yearentry.grid(column=1,row=2,padx=20)
monthentry=tk.Entry()
monthentry.grid(column=1,row=3,padx=20)
dateentry=tk.Entry()
dateentry.grid(column=1,row=4,padx=20)


btn=tk.Button(win,text="Calculate Age",command=getinput,bg="lightblue")
btn.grid(column=1,row=5,padx=5,pady=20)

win.mainloop()
