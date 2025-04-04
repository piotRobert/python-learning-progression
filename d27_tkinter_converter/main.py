from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    result_label.config(text = f"{miles * 1.60934}")

window = Tk()
window.title("Mile to Km Converter")

miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 10, "normal"))
equal_label.grid(column=0, row=1)

result_label = Label(text=0, font=("Arial", 10, "normal"))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.grid(column=2, row=1)

button =Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)








window.mainloop()    