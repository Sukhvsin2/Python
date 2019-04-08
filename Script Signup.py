from tkinter import *
from tkinter import ttk
import os

creds = 'tempfile.temp'
'''
def FSSsignup():
    with open(creds,'w') as f:
        f.write(entryL.get())
        f.write('\n')
        f.write(entryL1.get())
        f.close()

    root.destroy()
    Login()
'''

def Signup():
    global pwordE
    global nameE
    global root
        
    root = Tk()
    root.title('Signup')

    instr = Label(root,text = 'Please Enter new Credidentials\n')
    instr.grid(row=0,padx=10,pady=10)

    nameL =Label(root,text='New Username')
    nameL.grid(row=4,column=0)

    nameE = Entry(root)
    nameE.grid(row=4,column=1,sticky = W,ipadx=5,ipady=3,pady=2)

    passL =Label(root,text='Newpassword').grid(row=5,column=0)

    pwordE = Entry(root,show='*')
    pwordE.grid(row=5,column=1,sticky = W,ipadx=5,ipady=3,pady=2)

    signupbutton = ttk.Button(root,text='SignUp',command=FSSsignup)
    signupbutton.grid(row=7,column=1,pady=5)


    root.geometry('400x400')
    root.mainloop()

def FSSsignup():
    with open(creds,'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    root.destroy()
    Login()

def Login():
    global nameEL
    global pwordEL
    global rootA
    
    rootA = Tk()
    rootA.title('Login')
    instr = Label(rootA,text = 'Please Login\n')
    instr.grid(sticky=E)

    nameL = Label(rootA,text='Username: ')
    passL = Label(rootA,text  = 'Password: ')
    nameL.grid(row=1,sticky = W)
    passL.grid(row=2,sticky = W)

    nameEL= Entry(rootA)
    pwordEL = Entry(rootA,show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = ttk.Button(rootA,text = 'Login',command = CheckLogin)
    loginB.grid(columnspan=2,sticky=W,pady=5,padx=3)

    remUser = ttk.Button(rootA,text="Delete User Account",command=Deluser)
    remUser.grid(columnspan=2,sticky=W,padx=3)
    rootA.geometry('250x250+120+120')
    rootA.mainloop()

def CheckLogin():
    with open(creds) as f:
        data  = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
        print(uname+' '+pword)
        print(nameEL)
        if nameEL.get() == uname and pwordEL.get() == pword:
            r = Tk()
            r.title(':D')
            rL = Label(r,text = '\n[+] Logged In').pack()
            r.geometry('250x250')
            r.mainloop()
        else:
            r = Tk()
            r.title(':D')
            r.geometry('250x250')
            rL = Label(r,text='\n[!] Invalid Login...').pack()
            r.mainloop()

def Deluser():
    os.remove(creds)
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    Login()
else:
    Signup()



















        
