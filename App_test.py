#First Test of a App design, build using tKinter package

from tkinter import *
import os 
os.system('clear')



root = Tk()
root.title('TaskBird - Test App Design')
root.geometry("800x1000")


#Prompting a hello user, with a name insert
def hello():
    if(myTextbox.get() == ""):
        name = "             Invalid              "
    else:
        name = ("      Hello " + myTextbox.get() + "!     ")

    hello_label = Label(root, text= name)
    hello_label.place(x=340, y=100)

def StudentStatus():
    status_label = Label(root, text= "Student")
    status_label.place(x=350, y=300)
    
def TeacherStatus():
    status_label = Label(root, text= "Teacher")
    status_label.place(x=350, y=300)

myLabel = Label(root, text="Enter your first name: ")
myTextbox = Entry(root, width=30)
myButton = Button(root, text="Submit", command=hello)

myLabel1 = Label(root, text="Select your status: ")
myStatusButtonS = Button(root, text="Student", command=StudentStatus)
myStatusButtonT = Button(root, text="Teacher", command=TeacherStatus)


myLabel.place(x=325, y=0)
myTextbox.place(x=250, y=30)
myButton.place(x=350, y=60)
myLabel1.place(x=325, y=200)
myStatusButtonS.place(x=340, y=230)
myStatusButtonT.place(x=340, y=260)



root.mainloop()