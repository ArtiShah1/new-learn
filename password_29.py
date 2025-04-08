import tkinter
import tkinter.messagebox
from random import choice, randint, shuffle
import pyperclip
import json


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# ----------PASSWORD GENERATOR -----------------------
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                                                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','+']

def generate_password():
    password_letters = [choice(letters)  for item in range(randint(8,10))]
    password_numbers = [choice(letters)  for item in range(randint(2,4))]
    password_symbol = [choice(letters)  for item in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

    print(f"your password is : {password}")

# -----------SAVE PASSWORD ---------------------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty")
    else:
        # is_ok = tkinter.messagebox.askokcancel(title="website", message=f"These are the details entered:\nEmail: {email} \npassword:{password}\n is it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
                # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
# -------------------find pass-----------------------

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="NO Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=website, message=f"Email:{email}\npassword:{password}")
        else:
            tkinter.messagebox.showinfo(title="Error", message=f"no details for{website}exists")

# ------------UI SETUP -----------------------------

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
pass_img = tkinter.PhotoImage(file="password_logo.png")
canvas.create_image(100,100, image=pass_img)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="website")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="email/username")
email_label.grid(row=2, column=0)

password = tkinter.Label(text="password")
password.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"aru@gmail.com")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_search_button = tkinter.Button(text="Search",width=13, command=find_password)
generate_search_button.grid(row=1, column=2)





window.mainloop()