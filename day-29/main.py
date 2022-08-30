from tkinter import *
from tkinter import messagebox
import secrets
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_entry = Entry(width=25)
website_entry.focus()
username_entry = Entry(width=40)
username_entry.insert(0, "some@email.com")
password_entry = Entry(width=23)


def gen_password():
    password = secrets.token_hex(16)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


def search_handler() -> None:
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message="No passwords found")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title="Found", message=f"Email: {data[website]['username']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Not found", message="No passwords found")


def save_to_file(data: dict) -> None:
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=2)


def save() -> None:
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        save_to_file(new_data)
    else:
        data.update(new_data)
        save_to_file(data)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        messagebox.showinfo(title="Saved", message="Password saved successfully!")


generate_password_button = Button(text="Generate Password", command=gen_password)
add_button = Button(text="Add", width=38, command=save)
search_button = Button(text="Search", command=search_handler)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
website_entry.grid(row=1, column=1)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()
