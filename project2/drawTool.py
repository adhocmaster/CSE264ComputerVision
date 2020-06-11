import sys
import tkinter
import traceback
import cv2
from PIL import ImageTk, Image
import numpy as np


# takes input image and ask to give 4 consicutive points and crop and calculate RGB channel

if len(sys.argv) != 2:
    print(" No input given  %s " % sys.argv[0])
    sys.exit(-1)
    
_, IMG_FILENAME = sys.argv
IMG_FILENAME = 'images/' + IMG_FILENAME + '.jpg'



master = tkinter.Tk()
img_cv2 = cv2.imread(IMG_FILENAME)
# IMG = ImageTk.PhotoImage(Image.open(IMG_FILENAME).resize((1600, 1200), resample = 0))
IMG = ImageTk.PhotoImage(Image.open(IMG_FILENAME))
IMG_WIDTH, IMG_HEIGHT = IMG.width(), IMG.height()
print("Image H and W" , IMG_HEIGHT, IMG_WIDTH)

canvas = tkinter.Canvas(master, width=IMG_WIDTH, height=IMG_HEIGHT)
canvas.pack()

TOP_LEFT = None
BOTTOM_RIGHT = None

lines = []


def on_click(event):

    global TOP_LEFT, BOTTOM_RIGHT
    # print("Inside on_click")
    # if TOP_LEFT and BOTTOM_RIGHT:
    #     TOP_LEFT = None
    #     BOTTOM_RIGHT = None
        

    if not TOP_LEFT:
        TOP_LEFT = event.x, event.y
        print("TOP_LEFT ", TOP_LEFT)

    else:
        BOTTOM_RIGHT = event.x, event.y
        print("BOTTOM_RIGHT", BOTTOM_RIGHT)
        try:
            canvas.create_line(TOP_LEFT, BOTTOM_RIGHT, fill = "yellow")

        except:
            BOTTOM_RIGHT = None
            traceback.print_exc()
        
        lines.append([TOP_LEFT, BOTTOM_RIGHT])
        TOP_LEFT = None
        BOTTOM_RIGHT = None



canvas.bind('<Button-1>', on_click)

canvas.create_image((0,0), anchor=tkinter.NW, image=IMG)

def onClose(e):
    np.save('buildingLines.npy', np.array(lines))
    master.destroy()
    print('saved line points in buildingLines.npy')

master.bind('<Escape>', onClose)
master.mainloop()