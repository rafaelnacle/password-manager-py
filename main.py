from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def insert_copy_clipboard(password):
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied to Clipboard", message="Password copied do clipboard!")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    generated_password = "".join(password_list)
    if len(password_entry.get()) == 0:
        insert_copy_clipboard(generated_password)
    else:
        password_entry.delete(0, END)
        insert_copy_clipboard(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Hey...", message="The fields can't be empty my friend")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
emit_label = Label(text="Email/Username:")
emit_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "rafael@mail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=25,height=2, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=20)


window.mainloop()
