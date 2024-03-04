# Create a program that allows users to draw on a canvas using a GUI.

from tkinter import *

app = Tk()
app.geometry("800x600")

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_pic(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='black', width=2)
    lasx, lasy = event.x, event.y

canvas = Canvas(app, bg='white')
canvas.pack(anchor='nw', fill='both', expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_pic)

app.mainloop()