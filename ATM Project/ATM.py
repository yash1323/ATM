#!/usr/bin/env python
# coding: utf-8

# for json module 
import json
# for tkinter module
from tkinter import *
# for messagebox method
from tkinter import messagebox
# for image import pil module
from PIL import Image, ImageTk
# for random module
import random
# open json file
with open("Data.json", "r") as f1:
    data1 = json.load(f1)
# withdraw Function
def Withdraw(nw6,uname,password):
# check for negative and 0 value
    if float(scvalue.get()) == 0 and scvalue.get() < 0:
        message = "Please enter valid amount !!"
        messagebox.showinfo("Alert",message,icon="warning")
    else:
#         get the balance
        bal = data1[uname]['balance']
#     check balance if < 2000 isn't withdraw
        if float(scvalue.get()) <= (bal - 2000):
            bal -= float(scvalue.get())
            fee = 0.5/100
#             withdraw amount and apply fees
            data1[uname]['balance'] = bal - (bal * fee)
#     update balance
            with open("Data.json","w") as f2:
                json.dump(data1,f2)
                message = f"Withdraw Amount Successfully !! \n Account No:- {data1[uname]['ano']} \n Balance:- {data1[uname]['balance']}"
                messagebox.showinfo("Alert",message,icon="info")
        else:
#             message for insufficient balance 
            message = "Insufficient Balance !!"
            messagebox.showinfo("Alert",message,icon="warning")
#     function for deposit        
def Deposit(nw5,uname,password):
#     check negative and 0 value
    if float(scvalue.get()) == 0 and float(scvalue.get()) < 0:
        message = "Please enter valid amount !!"
        messagebox.showinfo("Alert",message,icon="warning")
    else:
        bal = data1[uname]['balance']
        bal += float(scvalue.get())
        fee = 0.5/100
#         deposit amount and apply fees
        data1[uname]['balance'] = bal - (bal * fee)
#     update balance 
        with open("Data.json","w") as f2:
            json.dump(data1,f2)
            message = f"Deposit Amount Successfully !! \n Account No:- {data1[uname]['ano']} \n Balance:- {data1[uname]['balance']}"
            messagebox.showinfo("Alert",message,icon="info")
# display input amount and deposit, withdraw button to work.
def nextScreen(nw1,uname,password):
#     destroy widgets of previous screen
    for widget in nw1.winfo_children():
        widget.destroy()
    Label(nw1,text="Enter the Amount", font=('Helvetica',20)).pack(pady=20)
#     for input amount
    global scvalue
    scvalue = IntVar()
    scvalue = Entry(nw1,width=20)
    scvalue.pack()
#     deposit button
    deposit = Button(nw1, text="Deposit", command=lambda:Deposit(nw1,uname,password))
    deposit.pack(pady=23)
#     withdraw button
    withdraw = Button(nw1, text="Withdraw", command=lambda:Withdraw(nw1,uname,password))
    withdraw.pack(pady=23)
#     back button
    back = Button(nw1, text="Back", command=lambda:home(nw1))
    back.pack(pady=23)
#    validation for create account credentials          
def checkValidate1(nw2,uname,password):
#     check for empty fields 
    if (uname.get() == "" and password.get() == ""):
        messagebox.showinfo("Alert","Please Provide Details.",icon="warning")
    else:
        messagebox.showinfo("Alert","Account Created Successfully.",icon="info")
#         get account no
        acc_no = random.randint(100000000, 9999999999)
#     check if account number exists then reasign account number
        for user in data1:
            if acc_no == data1[user]["ano"]:
                acc_no = random.randint(100000000, 9999999999)
#      write data in json of new user
        with open("Data.json","w") as f3:
            new_user = {
                "pin": password.get(),
                "ano": acc_no,
                "balance": 0.0
            }

            data1[uname.get()] = new_user

            json.dump(data1,f3)
#         return home screen for login
        home(nw2)
#      validations for login account credentials    
def checkValidate2(nw4,uname,password):
#     check for empty fields
    if (uname.get() == "" and password.get() == ""):
        messagebox.showinfo("Alert","Please Provide Details.",icon="warning")
    else:
#         check username and password is valid
        if uname.get() in data1:
            if password.get() == data1[uname.get()]['pin']:
                uname = uname.get()
                password= password.get()
                nextScreen(nw4,uname,password)
            else:
                messagebox.showinfo("Alert","Please Enter Valid Password.",icon="warning")
        else:
            messagebox.showinfo("Alert","Please Enter Valid Username.",icon="warning")
# function for create account provide inputs like username and password 
def create_account(nw3):
#     destroy widgets of previous screen 
    for widget in nw3.winfo_children():
        widget.destroy()
#     set icon
    image = Image.open("icon.png")
    resized_image= image.resize((300,205))
    photo = ImageTk.PhotoImage(resized_image)
    yash = Label(nw3,image=photo)
    yash.image = photo
    yash.pack()
#     create canvas for input credentials
    credentials = Canvas(nw3)
    
    Label(credentials,text="Enter the Username", font=('Helvetica',20)).pack(pady=20)

#Create Entry Widget for user name
    uname= Entry(credentials,width=20)
    uname.pack()

    Label(credentials,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)

#Create Entry Widget for password
    password= Entry(credentials,show="*",width=20)
    password.pack()
#     button for create account
    Button(credentials, text="Create Account", command=lambda:checkValidate1(nw3,uname,password)).pack(pady=23)
    credentials.pack()
# function for home screen or login screen contain inputs.
def home(nw7):
    for widget in nw7.winfo_children():
        widget.destroy()
#         apply title 
    nw7.title("ATM")
#     make 700x700 screen
    nw7.geometry("700x700")
#     set state zoomed 
    nw7.state('zoomed')
    # Set icon
    nw7.iconbitmap('icon1.ico')
# set image
    image = Image.open("icon.png")
    resized_image= image.resize((300,205))
    photo = ImageTk.PhotoImage(resized_image)
    yash = Label(image=photo)
    yash.image = photo
    yash.pack()
#     create canvas for input credentials
    credentials = Canvas(nw7)
    
    Label(credentials,text="Enter the Username", font=('Helvetica',20)).pack(pady=20)

    #Create Entry Widget for user name
    uname= Entry(credentials,width=20)
    uname.pack()

    Label(credentials,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)

    #Create Entry Widget for password
    password= Entry(credentials,show="*",width=20)
    password.pack()
# create button for validate username and password 
    Button(credentials, text="Submit", command=lambda:checkValidate2(nw7,uname,password)).pack(pady=23)

    Label(credentials,text="Don't have an account?", font=('Helvetica',20)).pack(pady=20)
# create button for create or register account
    Button(credentials, text="Sign Up", command=lambda:create_account(nw7)).pack(pady=23)
    
    credentials.pack()
#     create window
window = Tk()
# call home screen or function
home(window)
window.mainloop()