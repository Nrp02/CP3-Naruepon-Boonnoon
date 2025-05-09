from tkinter import *
import math

def leftclick(event):
    answer = float(textboxweight.get()) / math.pow(float(textboxhight.get()) /100, 2)
    if answer >= 30:
        answer = "อ้วนมาก"
    elif 25.0 <= answer <= 29.9:
        answer = "อ้วน"
    elif 23.0 <= answer <= 24.9:
        answer = "น้ำหนักเกิน"
    elif 18.6 <= answer <= 22.9:
        answer = "น้ำหนักปกติ เหมาะสม"
    else:
        answer = "ผอมเกินไป"
    result.configure(text="Your BMI is: " + str(answer))

main = Tk()
weight = Label(main, text="weight (kg.):").grid(row=0, column=0)
textboxweight = Entry(main)
textboxweight.grid(row=0, column=1)

hight = Label(main, text="hight (cm.):").grid(row=1, column=0)
textboxhight = Entry(main)
textboxhight.grid(row=1, column=1)

calculate = Button(main, text="Calculate")
calculate.grid(row=2, column=0)
calculate.bind("<Button-1>", leftclick)

result = Label(main, text="result:")
result.grid(row=2, column=1)

main.mainloop()