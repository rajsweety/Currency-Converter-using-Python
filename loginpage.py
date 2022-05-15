from tkinter import *
#importing all functions from tkinter[*=all]
from tkinter import messagebox
from subprocess import call

def ok():
    uname=e1.get()
    #entry done in entrybox of username will get stored in variable uname
    password=e2.get()
    #entry done in entrybox of password will get stored in variable password


    if(uname=="upwaaley" and password=="12345"):
        #uname and password entered by user will get with saved password,if it is correct
        #a message box will display of login success
        messagebox.showinfo(" ","Login Success")
        root.destroy()
        #current form will get close
        #we will directly jump into our main application
        call(["python","project.py"])
        return True

    else:
        #if incorrect username or password is entered then appropriate message
        #will be displayed on the screen
        messagebox.showinfo(" ","Incorrect username and password")
        return False
        
root=Tk()
#To create top level or main window we need to use a keyword(for ex-root)
root.title("Login")
#Login is title for main window
root.geometry("300x400")
#By using geometry we give size to the main window
l1=Label(root,text="Username")
l1.place(x=10,y=10)
#A label has been created of name username and positioned with the help of place
l2=Label(root,text="Password")
l2.place(x=10,y=40)
#A label has been created of name Password and positioned with the help of place
e1=Entry(root)
e1.place(x=140,y=10)
#Entry box is created in which user can write the input for Username.
#It is positioned in the front Username by adjusting [x] and keeping y constant as in username
e2=Entry(root)
e2.place(x=140,y=40)
#Entry box is created in which user can write the input for Password.
#It is positioned in the front Password by adjusting [x] and keeping y constant as in password
e2.config(show="#")
#when user will write password it will visible in form of [#] and it is
#set for entry box 2 by wriiting e2.config(show="#")
b=Button(root,text="Submit",font=("bold",15),command=ok,height=3,width=13,
         fg="green",bg="yellow",activebackground="red")
b.place(x=100,y=100)
#Button is created of name submit of appropriate size,normally background color
#is yellow but on clicking it will turn into red with help of activebackground
#command is also used it will call the function ok.
root.mainloop()
#To display window 

