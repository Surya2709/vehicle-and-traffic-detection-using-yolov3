import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import PIL
from PIL import Image,ImageTk
import cv2


root=tk.Tk()
root.title('Vehicle Counting APP')
w=600
h=700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 7) - (h / 7)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0,0)
root.config(background='#33A1C9')


#adding icon
icon=tk.PhotoImage(file="photos/app_logo.png")
root.iconphoto(True,icon)


#logo image
img_logo = Image.open("photos/logo1.png")
img_logo = img_logo.resize((120,120), Image.ANTIALIAS)
img1_logo = ImageTk.PhotoImage(img_logo)
img_login = Image.open("photos/login.png")
img1_login1 = ImageTk.PhotoImage(img_login)



def create_window():
    try:
        root.withdraw()
        import secondwin
    except:
        msg.showerror("ERROR","unable to open the second window !")

def check():
    try:
        
        if(name.get()=='trafficapp' and password.get()=='vehicle32'):
            create_window()
        elif(name.get()=='trafficapp' and password.get()!='vehicle32'):
            msg.showerror('Error : ', 'Invalid Password ')
        elif (name.get() != 'trafficapp' and password.get() == 'vehicle32'):
            msg.showerror('Error : ', ' Ivalid UserName')
        else:
            msg.showerror('Error : ', ' Ivalid UserName And Password')
    except:
        msg.showinfo("Information","pls Try again !")
        
        
fontStyle_login = tkFont.Font(family="arial", size=25,weight='bold')
fontStyle_other=tkFont.Font(family="arial", size=13,weight='bold')
fontStyle_button=tkFont.Font(family="arial", size=10)
label2=tk.Label(root,text='LOGIN',font=fontStyle_login,foreground='white',background='#33A1C9')
label2.place(relx=0.38,rely=0.04)
frame_inner=tk.Frame(root,borderwidth=1,relief="solid",background='white')
label1_logo = tk.Label(frame_inner, image=img1_logo,border=0)
label1_logo.place(relx=0.06,rely=0.12)
user=tk.Label(frame_inner,text='UserName:',foreground='#33A1C9',font=fontStyle_other,background='white').place(relx=0.4,rely=0.1)
pas=tk.Label(frame_inner,text='Password:',foreground='#33A1C9',font=fontStyle_other,background='white').place(relx=0.4,rely=0.4)

#Adding Entry
name=tk.StringVar()
User_name=tk.Entry(frame_inner,width=30,textvariable=name,foreground='#33A1C9',font=fontStyle_button)
User_name.insert(0,"Enter Username ")
User_name.place(relx=0.4,rely=0.2,height=25)
password=tk.StringVar()
Pass_word=ttk.Entry(frame_inner,width=35,textvariable=password,show='*',foreground='#33A1C9')
Pass_word.insert(0,'Enter Password')
Pass_word.place(relx=0.4,rely=0.5,height=25)

#button
button_login=tk.Button(frame_inner,image=img1_login1,command=check,border=0,bg='white')
button_login.place(relx=0.4,rely=0.75)
frame_inner.place(relwidth=1,relheight=0.7,relx=0,rely=0.15)

label3=tk.Label(root,text='Note:Username and Password requried',foreground='white',background='#33A1C9',font=fontStyle_other)
label3.place(relx=0.15,rely=0.9)


root.mainloop()