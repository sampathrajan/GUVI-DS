import re
import os
import json
import tkinter as tk
import tkinter.messagebox
from functools import partial
from tkinter import *

from Tools.demo.spreadsheet import center

def forget_pwd(uname):
    with open('user.json', 'r') as openfile:
        user_object = json.load(openfile)
    val=False
    print(uname)
    for a in user_object:
        print("Uname: "+a["email"])
        if a["email"]==uname.get():
            tkinter.messagebox.showinfo("Password",a["pwd"])
            val=True
            break
    if val==False:
        tkinter.messagebox.showerror("Error", "E-Mail Id Not Registered")

def forget_pwd_frm(form):
    form.destroy()
    forget = tk.Tk()
    user=tk.StringVar()
    user_lbl = tk.Label(forget, text="E-Mail Id:").grid(row=0, column=0)
    user_text = tk.Entry(forget, textvariable=user).grid(row=0, column=1)
    pwd_btn = tk.Button(forget, text="Show Password", command=partial(forget_pwd,user)).grid(
        row=1, column=1)
    login_btn = tk.Button(forget, text="Login", command=partial(login_frm, forget)).grid(
        row=1, column=0)
    forget.geometry("+500+300")


def login(form,uname,pwd):
    with open('user.json', 'r') as openfile:
        user_object = json.load(openfile)
    user=False
    uname=uname.get()
    pwd=pwd.get()
    for a in user_object:
        if a["email"]==uname:
            user = True
            if a["pwd"]==pwd:
                form.destroy()
                wel=tk.Tk()
                user_lbl = tk.Label(wel, text="Welcome User").grid(row=0, column=1)
                login_btn = tk.Button(wel, text=" Logout ", command=partial(logout, wel)).grid(
                    row=1, column=1)
                wel.geometry("+500+300")
                wel.mainloop()
                break
            else:
                tk.messagebox.showerror("Error","Invalid Password")
                break
    if user==False:
        tk.messagebox.showerror("Error","Username not Found, kindly Register User.")


def logout(form):
    form.destroy()
    login_frm(False)

def login_frm(reg_frm):
    if reg_frm!=False:
        reg_frm.destroy()


    loginForm = tk.Tk()

    loginForm.title("APP Login")
    user=tk.StringVar()
    pwd=tk.StringVar()
    user_lbl = tk.Label(loginForm, text="E-Mail Id:").grid(row=0, column=0)
    user_text = tk.Entry(loginForm,textvariable=user).grid(row=0, column=1)

    pwd_lbl = tk.Label(loginForm, text="Password:").grid(row=1, column=0)
    pwd_text = tk.Entry(loginForm, show="*",textvariable=pwd).grid(row=1, column=1)

    reg_btn = tk.Button(loginForm, text="User Registration", command=partial(user_reg_frm,loginForm)).grid(row=3, column=0)
    login_btn = tk.Button(loginForm, text=" Login ", command=partial(login,loginForm,user,pwd)).grid(row=2, column=1)
    forget_btn = tk.Button(loginForm, text="Forget Password", command=partial(forget_pwd_frm,loginForm)).grid(row=2, column=0)
    loginForm.geometry("+500+300")
    loginForm.mainloop()

def user_reg_frm(loginForm):
    loginForm.destroy()
    user_reg=tk.Tk()
    user_reg.title("User Registration")

    user_lbl = tk.Label(user_reg, text="E-Mail Id:").grid(row=0, column=0)
    user=tk.StringVar()
    user_text = tk.Entry(user_reg,textvariable=user).grid(row=0, column=1)

    pwd=tk.StringVar()
    pwd_lbl = tk.Label(user_reg, text="Password:").grid(row=1, column=0)
    pwd_text = tk.Entry(user_reg, textvariable=pwd,show="*").grid(row=1, column=1)

    reg_btn = tk.Button(user_reg, text="Register", command=partial(user_regis,user,pwd)).grid(row=2, column=1)
    login_btn = tk.Button(user_reg, text=" Login ", command=partial(login_frm,user_reg)).grid(row=2, column=0)
    user_reg.geometry("+500+300")
    user_reg.mainloop()


def user_regis(uname,pwd):
    reg_uname = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    reg_pwd = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
    uname=uname.get()
    pwd=pwd.get()
    duplicate=False
    if (re.fullmatch(reg_uname, uname)):
        if(re.fullmatch(reg_pwd,pwd)):
             user_objects=[]
             if os.path.isfile('user.json'):
                 with open('user.json', 'r') as openfile:
                    user_objects = json.load(openfile)
                    for a in user_objects:
                        if a["email"]==uname:
                            tkinter.messagebox.showerror("Error","E-Mail Already Exsist")
                            duplicate=True
                            break
             if duplicate==False:
                 val={
                     "email":"",
                      "pwd":""
                      }
                 val["email"] = uname
                 val["pwd"] = pwd
                 user_objects.append(val)
                 with open("user.json", "w") as outfile:
                     json.dump(user_objects, outfile)

                 tkinter.messagebox.showinfo("Sucess","User Registration Successful")
        else:
            tkinter.messagebox.showerror("Error","Invalid Password.")
    else:
        tkinter.messagebox.showerror("Error","Invalid E-Mail Id.")

login_frm(False)


