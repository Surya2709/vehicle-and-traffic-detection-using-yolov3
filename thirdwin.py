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

