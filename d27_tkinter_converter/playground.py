# def add(*args):
#     sum = 0
#     for n in args:
#         sum+= n
#     print(sum)

# add(3,5,6)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")
    
# my_car = Car(make = "Nissan")
# print(my_car.model)

from tkinter import *

def button_clicked():
    my_label.config(text = input.get())

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# button
button =Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New button
new_button =Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)