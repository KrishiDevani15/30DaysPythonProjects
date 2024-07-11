from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image


root=Tk()
root.geometry("400x400")
root.title("Image_Conversion_App")
canvas1 = Canvas(root,width = 400,height = 400,bg="azure2").pack()
root.resizable(False,False)


def jpg_to_png():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.png")
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=80,y=280)

def jpg_to_pdf():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15),bg="azure2")
        Label_2.place(x=80,y=280)

Label_1=Label(root,text="Welcome! This is My Image Convertor", font=("bold",15),bg="azure2")
Label_1.place(x=30,y=80)

Label_3=Label(root, text="Developed By :- Krishi Devani", width=35, font=("helvetica",8,"bold"),bg="azure2")
Label_3.place(x=62,y=365)




Button(root,text="JPG to PNG", width=20, height=2, bg="brown",fg="white",command=jpg_to_png).place(x=120,y=140)
Button(root,text="JPG to PDF", width=20, height=2, bg="brown",fg="white", command=jpg_to_pdf).place(x=120,y=220)

root.mainloop()