import Tkinter as tk
import cv2
from cv2 import *
from Tkinter import *
import tkMessageBox
import urllib, urllib2
import numpy as np
import base64
import requests
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image, ImageTk

android = 0;

url='http://192.168.1.152:8080/shot.jpg'


def printcam() :
    cv2.imwrite("tmp.png", cv2image)
    encoded = base64.b64encode(open("tmp.png", "rb").read()).decode()
    pic = 'data:image/png;base64,{}'.format(encoded)
    mydata=[('hidden_data',pic)]
    path='http://192.168.8.1:8000/upload.php?name=pi'    #the url you want to POST to
    req = requests.post(path, data = {'hidden_data':pic})
    req.raise_for_status()
    pause.set(1)
    tkMessageBox.showinfo("Printing...", "Uploaded to Server")


#width, height = 500, 300
#cap = cv2.VideoCapture(0)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, int(width))
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, int(height))
#time.sleep(5)
camera = PiCamera()
camera.resolution = (500, 300)
camera.framerate = 100
rawCapture = PiRGBArray(camera, size=(500,300))


time.sleep(0.1)

root = tk.Tk()
root.title("Pixel Plotter Python Camera Interface")


pause = IntVar()
c = Checkbutton(root, text="Pause", variable=pause)
c.pack()

w1 = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=600)
w1.set(50)
w1.pack()

w2 = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=600)
w2.set(100)
w2.pack()





m = 0

def down(e):
    if m == 0:
        print 'Down\n', e.char, '\n', e
        global m
        pause.set(int(not bool(pause.get())))
        m = 1

def up(e):
    if m == 1:
        print 'Up\n', e.char, '\n', e
        global m
        m = 0

root.bind('<KeyPress>', down)
root.bind('<KeyRelease>', up)


root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()

stprint = Button(root,
                   text="print",
                    command=printcam)
stprint.pack()


frame = ""
cv2image = ""

def show_frame():
    global cv2image
    if pause.get() != 1:
        global frame
        if android == 0:
#            ret, frame = cap.read()
	     camera.capture(rawCapture, format="bgr")
	     frame = rawCapture.array
        else:
                imgResp = urllib.urlopen(url)
    
                # Numpy to convert into a array
                imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
                
                # Finally decode the array to OpenCV usable format ;) 
                frame = cv2.imdecode(imgNp,-1)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    cv2image = cv2.Canny(img_gray_blur, w1.get(), w2.get())
    
    # Do an invert binarize the image 
   # ret, cv2image = cv2.threshold(canny_edges, 250, 255, cv2.THRESH_BINARY_INV)

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
 #   time.sleep(0.5)
#    if(waitKey(30) >= 0):
#	x=0
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)

show_frame()
root.mainloop()
