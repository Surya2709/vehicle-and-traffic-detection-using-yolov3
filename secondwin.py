from tkinter import *
import tkinter as tk
import numpy as np
import PIL
from PIL import Image,ImageTk
import cv2
from tkinter import ttk
from connecting_to_db import dynamic_data_entry
from tkinter import messagebox as msg
import tkinter.font as tkFont
import sqlite3
import time 
global cap

 

# Load Yolo
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")
classes = []
with open("yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

 
#frame_id = 0
root=tk.Toplevel()
root.title('Vehicle Counting Application')
w=1100
h=690
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=0
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.resizable(1,1)
root.config(background="white")

def about():
    try:
        import thirdwin
    except:
        msg.showerror("ERROR","unable to go to about")
        

#loading necessary images
logo = Image.open("photos/app_logo.png")
logo = logo.resize((40,40), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
bicycle = Image.open("photos/b1.png")
bicycle = bicycle.resize((80,80), Image.ANTIALIAS)
bicycle1 = ImageTk.PhotoImage(bicycle)
bike = Image.open("photos/bike.png")
bike = bike.resize((80,80), Image.ANTIALIAS)
bike1 = ImageTk.PhotoImage(bike)
car = Image.open("photos/car.png")
car = car.resize((80,80), Image.ANTIALIAS)
car1 = ImageTk.PhotoImage(car)
bus = Image.open("photos/Bus.png")
bus = bus.resize((80,80), Image.ANTIALIAS)
bus1 = ImageTk.PhotoImage(bus)
truck = Image.open("photos/truck.png")
truck = truck.resize((80,80), Image.ANTIALIAS)
truck1 = ImageTk.PhotoImage(truck)
btn1 = Image.open("photos/d.png")
btn11 = ImageTk.PhotoImage(btn1)
btn2 = Image.open("photos/c.png")
btn12 = ImageTk.PhotoImage(btn2)
btn3 = Image.open("photos/a.png")
btn13 = ImageTk.PhotoImage(btn3)
btn4 = Image.open("photos/h.png")
btn14 = ImageTk.PhotoImage(btn4)
btn5 = Image.open("photos/i.png")
btn15 = ImageTk.PhotoImage(btn5)
logoframe = Image.open("photos/app_frame.png")
logoframe = logoframe.resize((int(w*0.35),int(h*0.35)), Image.ANTIALIAS)
logoframe1 = ImageTk.PhotoImage(logoframe)

#font style
font_welcome=tkFont.Font(family='arial',size='20',weight='bold')
font_root=tkFont.Font(family='arial',size='15',weight='bold')
font_total=tkFont.Font(family='arial',size='10',weight='bold')

root_label=tk.Label(root,text="Space for live cam",font=font_root,background='white').place(relx=0.39)
time=tk.Label(root,font=font_root,background='white')
time.place(relx=0.88)

#adding frames in root
left_frame=tk.Frame(root,background='#DAEEF3')
logo_label=tk.Label(left_frame,image=logo1,background='#DAEEF3').place(relx=0.1,rely=0.02)
label1=tk.Label(left_frame,text="Welcome Username",background='#DAEEF3',font=font_welcome).place(relx=0.25,rely=0.025)
inside_frame=tk.Frame(left_frame,background='#F2F2F2')
heading_label=tk.Label(inside_frame,text="DataBase",font=font_welcome,background='#F2F2F2').pack(pady=10)
inside_frame.place(relwidth=0.95,relheight=0.75,relx=0.03,rely=0.1)
left_frame.place(relwidth=0.38,relheight=1,relx=0,rely=0)

frame_right=tk.Frame(root,background='#F2F2F2',border=0)
labelframe=tk.Label(frame_right,image=logoframe1,background='#F2F2F2').pack(pady=70)
cap=cv2.VideoCapture("photos/sample.py")
lmain = tk.Label(frame_right)
lmain.place(relx=0,rely=0)
def clock():
    #current_time=time.strftime('%I:%M:%S%p')
    #time['text']=current_time
    root.after(1000,clock)

def logout():
    try:
        ans=msg.askokcancel('Logout INFO','Are you sure you want to logout?')
        if(ans==True):
            root.destroy()
            exit()
    except:
        msg.showerror("ERROR","unable to log out.pls try again!")


def quit(widget):
    global lmain,cap
    widget.destroy()
    lmain = tk.Label(frame_right)
    lmain.place(relx=0,rely=0)
    cap.release()
    cap=cv2.VideoCapture("photos/sample.mp4")
def database():
    try:
        conn = sqlite3.connect('CSVDB.db')
        c = conn.cursor()
        database = r"CSVDB.db"
        tree = ttk.Treeview(inside_frame, column=(1, 2, 3, 4, 5, 6,7), show='headings', height=22)
        treeScroll = ttk.Scrollbar(inside_frame, orient=tk.VERTICAL)
        treeScroll.configure(command=tree.yview)
        tree.configure(yscrollcommand=treeScroll.set)
        tree.heading(1, text='time')
        tree.column(1, minwidth=0,width=80, stretch=False)
        tree.heading(2, text='car')
        tree.column(2, minwidth=0, width=50, stretch=False)
        tree.heading(3, text='bike')
        tree.column(3, minwidth=0, width=50, stretch=False)
        tree.heading(4, text='bus')
        tree.column(4, minwidth=0, width=50, stretch=False)
        tree.heading(5, text='cycle')
        tree.column(5, minwidth=0, width=50, stretch=False)
        tree.heading(6, text='truck')
        tree.column(6, minwidth=0, width=50, stretch=False)
        tree.heading(7, text='total')
        tree.column(7, minwidth=0, width=50, stretch=False)
        cur = conn.cursor()
        cur.execute("SELECT * FROM countvehicle")

        rows = cur.fetchall()
        for row in rows:
            tree.insert('','end',values=row)
        tree.place(relx=0,rely=0.1)
        treeScroll.place(relx=0.96,rely=0.1,relheight=0.9)
    except:
        msg.showerror("ERROR","something went wrong with DB")
     # loading image
cap = cv2.VideoCapture("photos/sample.mp4")
font = cv2.FONT_HERSHEY_PLAIN


def yolo():
    frame_id = 0
    _, frame = cap.read()
    frame_id += 1
    height, width,channels = frame.shape
    total_length=0
    total_bus=0
    total_car=0
    total_cycle=0
    total_truck=0
    total_motorbike=0
   

    if _:
        # Detecting object
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = np.array([])
        confidences = np.array([])
        boxes = []
        detected_object = np.array([])

        for out in outs:  # OUTS CONTAINS ALL THE INFORMATION ABOUT OBJECTS DETECTED
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    # OBJECT DETECTED
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # RECTANGLE COORDINATES
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences = np.append(confidences, [confidence])
                    class_ids = np.append(class_ids, [class_id])

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[int(class_ids[i])])
                detected_object = np.append(detected_object, [label])
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
                cv2.putText(frame, label, (x, y), font, 1, color, 2)
                #seconds = time.time()
                #local_time = time.ctime(seconds)
                #cv2.putText(frame, local_time, (10, 30), font, 1, (0, 255, 255), 1)

                total_length = len(detected_object)

                total_length = len(detected_object)

                car = np.where(detected_object == "car")
                total_car = len(detected_object[car])
                #carlabel['text'] = total_car

                motorbike = np.where(detected_object == "motorbike")
                total_motorbike = len(detected_object[motorbike])
                #bikelabel['text'] = total_motorbike

                bus = np.where(detected_object == "bus")
                total_bus = len(detected_object[bus])
                #buslabel['text'] = total_bus

                cycle = np.where(detected_object == "bicycle")
                total_cycle = len(detected_object[cycle])
                #bilabel['text'] = total_cycle

                truck = np.where(detected_object == "truck")
                total_truck = len(detected_object[truck])
                #trucklabel['text'] = total_truck
       # timeclock=time.strftime('%I:%M:%S')
       # dynamic_data_entry(timeclock, total_car, total_motorbike, total_bus, total_cycle,total_truck,total_length)

        b = cv2.resize(frame, (700, 450), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        cv2image = cv2.cvtColor(b, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        carlabel['text'] = total_car
        bikelabel['text'] = total_motorbike
        buslabel['text'] = total_bus
        bilabel['text'] = total_cycle
        trucklabel['text'] = total_truck
        traffic=False
        if total_truck>=3 or total_motorbike>=10 or total_bus>=3 or total_cycle>=15 or total_car>=7 or total_length >=13:
            popup_traffic()
            traffic=True
        if traffic==True:
            total_length=0
            total_truck=0
            total_bus=0
            total_car=0
            total_cycle=0
            total_motorbike=0
            popup_new()
            traffic=False
        lmain.after(100, lambda: yolo())
       
            

frame_right.place(relheight=0.6,relwidth=0.6,relx=0.39,rely=0.05)


frame_b=tk.Frame(root,background='white')
label_bicycle=tk.Label(frame_b,image=bicycle1,border=0).place(relx=0.05,rely=0.05)
label_bike=tk.Label(frame_b,image=bike1,border=0).place(relx=0.25,rely=0.05)
label_car=tk.Label(frame_b,image=car1,border=0).place(relx=0.45,rely=0.05)
label_bus=tk.Label(frame_b,image=bus1,border=0).place(relx=0.65,rely=0.05)
label_truck=tk.Label(frame_b,image=truck1,border=0).place(relx=0.85,rely=0.05)
tk.Label(frame_b,text='Total:',font=font_total,background='white').place(relx=0.07,rely=0.6)
tk.Label(frame_b,text='Total:',font=font_total,background='white').place(relx=0.27,rely=0.6)
tk.Label(frame_b,text='Total:',font=font_total,background='white').place(relx=0.47,rely=0.6)
tk.Label(frame_b,text='Total:',font=font_total,background='white').place(relx=0.67,rely=0.6)
tk.Label(frame_b,text='Total:',font=font_total,background='white').place(relx=0.87,rely=0.6)
bilabel=tk.Label(frame_b,text='0',font=font_total,background='white')
bilabel.place(relx=0.13,rely=0.6)
bikelabel=tk.Label(frame_b,text='0',font=font_total,background='white')
bikelabel.place(relx=0.33,rely=0.6)
carlabel=tk.Label(frame_b,text='0',font=font_total,background='white')
carlabel.place(relx=0.53,rely=0.6)
buslabel=tk.Label(frame_b,text='0',font=font_total,background='white')
buslabel.place(relx=0.73,rely=0.6)
trucklabel=tk.Label(frame_b,text='0',font=font_total,background='white')
trucklabel.place(relx=0.93,rely=0.6)

frame_b.place(relwidth=0.6,relheight=0.25,relx=0.39,rely=0.75)

#buttons
button_cam1=tk.Button(root,image=btn11,border=0,bg='green',command=yolo).place(relx=0.41,rely=0.67)
button_cam2=tk.Button(root,text='End CAM',image=btn13,border=0,bg='red',command=lambda :quit(lmain)).place(relx=0.61,rely=0.67)
button_cam3=tk.Button(root,text='About System',image=btn12,border=0,bg='yellow',command=about).place(relx=0.81,rely=0.67)
button_cam4=tk.Button(left_frame,text='Show DB',image=btn14,bg='green',command=database).place(relx=0.04,rely=0.87)
button_cam5=tk.Button(left_frame,text='Logout',image=btn15,bg='red',command=logout).place(relx=0.5,rely=0.87)


def popup_traffic():
    msg.showwarning("Warning","oops traffic! please take another alternate route !")
def popup_new():
    msg.showinfo("Information","hope you took diversion and detecting vehicles again from zero")
clock()