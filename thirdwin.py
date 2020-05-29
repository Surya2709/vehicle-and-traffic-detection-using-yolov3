import tkinter as tk
import tkinter.font as tkFont
import PIL
from PIL import Image,ImageTk

third_win=tk.Toplevel()
third_win.title('Vehicle Counting Application')
w=900
h=500
ws=third_win.winfo_screenwidth()
hs=third_win.winfo_screenheight()
x=(ws/2)-(w/2)
y=0
third_win.geometry('%dx%d+%d+%d'%(w,h,x,y))
third_win.config(background='sky blue')
third_win.resizable(0,0)
#creating frames
frame_manish=tk.Frame(third_win,background='#DAEEF3')
label_manish=tk.Label(frame_manish,text='Team Member',font=tkFont.Font(family='arial',size=15,weight='bold'),bg='#DAEEF3')
label_manish.pack()
tk.Label(frame_manish,text="Nobody",font=tkFont.Font(family='arial',size=14,weight='bold'),bg='#DAEEF3').place(relx=0.2,rely=0.8)
frame_manish.place(relwidth=0.3,relheight=0.49,relx=0.01,rely=0.01)

frame_about=tk.Frame(third_win,background='#DAEEF3')
label_about=tk.Label(frame_about,text="About",font=tkFont.Font(family='arial',size=20,weight='bold',underline=1),bg='#DAEEF3').pack()
text_about1=tk.Text(frame_about,height=20,width=39,bg='#DAEEF3',border=0,font=('arial',11,'bold'))
text_about1.insert(tk.INSERT,"VCA is a Vehicle Counting application\ndeveloped to control the traffic Congestion on the road in real-time by continuous moni-toring of the road via surveillance cameras.\n")
text_about1.insert(tk.INSERT,'\nObjective:Managing traffic congestion\nLanguage used:Python\nFront-end:Tkinter\nBack-end:Python(SQlite3 database)\nAlgorithm used:Yolov3\nDataset:COCO dataset')
text_about1.config(state='disable')
text_about1.place(relx=0.02,rely=0.18)
frame_about.place(relwidth=0.36,relheight=0.49,relx=0.32,rely=0.01)

frame_sumesh=tk.Frame(third_win,background='#DAEEF3')
tk.Label(frame_sumesh,text='Team Member',font=tkFont.Font(family='arial',size=15,weight='bold'),bg='#DAEEF3').pack()
tk.Label(frame_sumesh,border=0).pack()
tk.Label(frame_sumesh,text="A",font=tkFont.Font(family='arial',size=14,weight='bold'),bg='#DAEEF3').place(relx=0.2,rely=0.75)
frame_sumesh.place(relwidth=0.3,relheight=0.49,relx=0.69,rely=0.01)

frame_shreev=tk.Frame(third_win,background='#DAEEF3')
tk.Label(frame_shreev,text='Team Member',font=tkFont.Font(family='arial',size=15,weight='bold'),bg='#DAEEF3').pack()
tk.Label(frame_shreev,text="B",font=tkFont.Font(family='arial',size=14,weight='bold'),bg='#DAEEF3').place(relx=0.2,rely=0.8)
frame_shreev.place(relwidth=0.3,relheight=0.48,relx=0.01,rely=0.51)

frame_roli=tk.Frame(third_win,background='#DAEEF3')
tk.Label(frame_roli,text='Supervisor',font=tkFont.Font(family='arial',size=15,weight='bold'),bg='#DAEEF3').pack()
tk.Label(frame_roli,text="C",font=tkFont.Font(family='arial',size=14,weight='bold'),bg='#DAEEF3').place(relx=0.2,rely=0.8)
frame_roli.place(relwidth=0.36,relheight=0.48,relx=0.32,rely=0.51)

frame_lal=tk.Frame(third_win,background='#DAEEF3')
tk.Label(frame_lal,text='Team Member',font=tkFont.Font(family='arial',size=15,weight='bold'),bg='#DAEEF3').pack()
tk0.Label(frame_lal,text="E",font=tkFont.Font(family='arial',size=14,weight='bold'),bg='#DAEEF3').place(relx=0.2,rely=0.8)
frame_lal.place(relwidth=0.3,relheight=0.48,relx=0.69,rely=0.51)


