from tkinter import *
#importing all functions from tkinter[*=all]
root=Tk()
#To create top level or main window we need to use a keyword(for ex-root)
root.geometry("800x400")
#By using geometry we give size to the main window
root.title("Currency converter")
#we have change the title from default to currency converter
OPTIONS={"Australian Dollar":0.019,"Brazilian Real":0.077,"British Pound":0.013,
         "Bulgarian Lev":0.023,"Chinese Yuan":0.090,"Euro":0.011,"Honkong Dollar":0.10,
         "Indonesian Rupiah":195.72,"Japanese Yen":1.40,"Pakistani Rupee":2.15,
         "SriLankan Rupee":2.47,"Swiss Franc":0.012,"Us Dollar":0.013}
#Dictionary is created
def done():
    price=e1.get()
    #whatever we will enter in the indian rupee text box that will store into price
    answere=variable.get()
    #whatever variable  key will be present will get stored in the answere
    Dict=OPTIONS.get(answere,None)
    #value of key is fetched from OPTIONS and stored in Dict,none is default if nothing has been passed
    calculate=float(Dict)*float(price)
    result.delete(1.0,END)
    #if anything has been typed then delete that item from starting to end
    result.insert(INSERT,"Value In",INSERT,answere,INSERT," = ",INSERT,calculate)
    #these things are going to be insert on the text box
    

l=Label(root,text="Currency",font=("arial",30,"bold"),fg="blue",bg="yellow")
l.grid(row=0,column=0,padx=30,pady=20,ipadx=15)
#A label of name Currency has been created on the root with mentioned designed
#It is positioned with the help of grid, external and internal padding is also used.
#grid organizes the widgets in the table like structure
l1=Label(root,text="Converter",font=("arial",30,"bold"),fg="blue",bg="yellow")
l1.grid(row=0,column=3)
#A label of name Converter has been created on the root with mentioned designed
#It is positioned with the help of grid.
l2=Label(root,text="Indian Rupees:-",font=("arial",15,"bold"),fg="dark green")
l2.grid(row=2,column=0,pady=5)
#A label of name Indian currency has been created on the root with mentioned designed
#It is positioned with the help of grid, external vertical padding is used.
e1=Entry(root,font=("bold",20))
e1.grid(row=2,column=1,pady=20)
#entry box is created for indian rupees in which user will enter the value in indian rs which he wan't to convert into other currency.
l3=Label(root,text="Country",font=("arial",15,"bold"),fg="dark green")
l3.grid(row=3,column=0)
#A label of name Counrty has been created on the root with mentioned designed.
variable=StringVar(root)
#string variable is created on root
variable.set(None)
#none is default value 
option=OptionMenu(root,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
#Option menu is created on the root and it is attached with the variable
#Sticky is used to indicate which sides and corners of the cell the widgets sticks to,when the widget is smaller than the cell
#here east west is used
button=Button(root,text="convert",fg="red",bg="yellow",activebackground="green",font=10,command=done)
button.grid(row=3,column=3,padx=20)
#Button of name convert is created
result=Text(root,height=4,width=50,font=("arial",10,"bold"),bd=5)
result.grid(row=4,columnspan=10,pady=40)
#A box is created in which our final converted value is displayed
#columnspan tells the layout manager that you wish for this widget to occcupy more than one collumn ........default it is 1
root.mainloop()


