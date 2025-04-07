from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message = "Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {email} \nPassword: {password} \nIs it okey to save?")
        if is_ok:
            with open("d29_password_manager/pass.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="d29_password_manager/logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0,column=1)

# Labels
webstie_label = Label(text="Website:",)
webstie_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:",)
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",)
password_label.grid(row=3,column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "myAwesomeMail@gmail.com")

password_entry = Entry(width=5)
password_entry.grid(row=3, column=1, sticky="ew")

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2, sticky="ew")

pass_button = Button(width=36, text="Add", command=save)
pass_button.grid(row=4,column=1, columnspan=2, sticky="ew")








window.mainloop()