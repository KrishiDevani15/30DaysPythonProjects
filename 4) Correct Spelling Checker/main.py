from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()

    enter2.delete(0, END)
    enter2.insert(0, data)

def main_window():
    global enter1, enter2
    root = Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    root.title("Spelling Checker | Developed by Krishi")
    root.config(bg='#111827')

    title_label = Label(root, text="Welcome to my Spelling Checker App", font=("Time new Roman", 22, 'bold'), fg='#d0d0d2', bg='#111827')
    title_label.place(x=0, y=20, relwidth=1)
    
    label1 = Label(root, text="Incorrect Spelling", font=("Ariel", 15, 'bold'), fg='white', bg='#111827')
    label1.place(x=0, y=90, height=50, relwidth=1)

    enter1 = Entry(root, font="Arial")
    enter1.place(x=150, y=150, width=300, height=30)

    label2 = Label(root, text="Correct Spelling", font=("Ariel", 15, 'bold'), fg='white', bg='#111827')
    label2.place(x=0, y=200, height=50, relwidth=1)
    
    enter2 = Entry(root, font="Arial")
    enter2.place(x=150, y=250, width=300, height=30)

    button1 = Button(root, text="Check!", font=("Time New Roman", 15, 'bold'), bg='#FFD0D2', command=correct_spelling)
    button1.place(x=245, y=320, width=100, height=35)
    
    root.mainloop()

main_window()
