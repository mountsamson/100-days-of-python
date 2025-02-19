from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#generate random password
def generate_password():
    import random
    import string
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
   

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
    
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Missing Inputs", message="Please make sure you have entered all details!" )
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
            
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4 ) 
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

canvas = Canvas(width=200, height=200)

logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)

canvas.grid(row=0, column=1)


#labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
enail_label = Label(text="Email/Username: ")
enail_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "napa_4@live.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()