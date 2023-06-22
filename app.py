import tkinter as tk
import pickle
import customtkinter as ck
import pandas as pd
import numpy as np
import mediapipe as mp
import cv2
from PIL import Image, ImageTk
from landmarks import landmarks

window = tk.Tk()
window.geometry("480x700")
window.title('wir bauen maschinen')
ck.set_appearance_mode("dark")

frame = tk.Frame(height=480, width=480)
frame.place(x=10, y=90)
lmain = tk.Label(frame)
lmain.place(x=0, y=0)




classLabel = ck.CTkLabel(window, height=40, width=120, text_color='black', padx='10')
classLabel.place(x=25, y=1)
classLabel.configure(text='EINS')
counterLabel = ck.CTkLabel(window, height=40, width=120,text_color='black', padx='10')
counterLabel.place(x=165, y=1)
counterLabel.configure(text='ZWEI')
probLabel = ck.CTkLabel(window, height=40, width=120, text_color="black", padx=10)
probLabel.place(x=315, y=1)
probLabel.configure(text='DREI')
classBOX = ck.CTkLabel(window, height=40, width=120, text_color="black",fg_color='blue')
classBOX.place(x=25, y=41)
classBOX.configure(text='0')
counterBox = ck.CTkLabel(window, height=40, width=120, text_color="black",fg_color='blue')
counterBox.place(x=175, y=41)
counterBox.configure(text='0')
probBox = ck.CTkLabel(window, height=40, width=120, text_color="black",fg_color='blue')
probBox.place(x=315, y=41)
probBox.configure(text='0')

def reset_counter():
    global couunter
    counter = 0

button = ck.CTkButton(window,text='Press', command=reset_counter, height=40, width=120, text_color='white', fg_color='blue')
button.place(x=10, y=600)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)



cap = cv2.VideoCapture(0)
def detect():

    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    mp_drawing.draw_landmarks(image, results.pose_landmarks,  mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5),
                              mp_drawing.DrawingSpec(color=(255, 102, 0), thickness=5, circle_radius=10))

    img = image[:, :460, :]
    imgarr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(imgarr)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, detect)


detect()
window.mainloop()