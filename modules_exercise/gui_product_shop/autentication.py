import json

from gui_product_shop.clean_screan_view import clean_screen
from gui_product_shop.global_window import app
from gui_product_shop.products import render_products_view
from tkinter import Button, Entry, Label


def login(*args):
    current_user, user_password = args
    file_path = "db\\users_credentials.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip()
            user, password = line.split(", ")
            if current_user == user and user_password == password:
                return render_products_view(current_user)
        return render_login(error=True)


def render_login(error=None):
    clean_screen()
    label_welcome_text = "Login form \n Please enter username and password"
    label_error_text = "Invalid username or password"
    label_username = "Enter your username:"
    label_password = "Enter your password:"
    Label(app, text=label_welcome_text, fg="black", font=('Georgia', 16)).grid(row=0, column=0)
    username = Entry(app)
    Label(app, text=label_username, fg="black", font=('Georgia', 12)).grid(row=1, column=0)
    username.grid(row=1, column=1)
    password = Entry(app, show="*")
    Label(app, text=label_password, fg="black", font=('Georgia', 12)).grid(row=2, column=0)
    password.grid(row=2, column=1)
    if error:
        Label(app, text=label_error_text, fg="red", font=('Georgia', 12)).grid(row=4, column=0)
    Button(app, text="Enter", bg="black", fg="white", font=('Georgia', 14),
           command=lambda: login(username.get(), password.get())).grid(row=3, column=1)
    Button(app, text="Go Back", bg="black", fg="white", font=('Georgia', 14),
           command=render_main_enter_screen).grid(row=5, column=1)


def username_validation(current_user, user_password):
    file_path = 'db\\users_credentials.txt'
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        if not lines:
            file.write(f'{current_user}, {user_password}' + '\n')
            return True
        for line in lines:
            line = line.rstrip('\n')
            user, password = line.split(", ")
            if current_user == user:
                Label(app, text="This username is not available", fg="red", font=('Georgia', 12),
                      ).grid(row=2, column=2)
                return False
        else:
            file.write(f'{current_user}, {user_password}')
            file.write('\n')
            return True


def register(*args, **kwargs):
    if username_validation(*args):
        kwargs.update({"products": []})
        file_path = 'db\\users.txt'
        with open(file_path, 'a') as file:
            file.writelines(json.dumps(kwargs) + '\n')
        render_login()


def render_register():
    clean_screen()
    Label(app, text="Registration form", font=('Georgia', 16)).grid(row=0, column=2)
    first_name = Entry(app)
    first_name.grid(row=1, column=1)
    Label(app, text="Enter your first name:", font=('Georgia', 12)).grid(row=1, column=0)
    last_name = Entry(app)
    last_name.grid(row=2, column=1)
    Label(app, text="Enter your last name:", font=('Georgia', 12)).grid(row=2, column=0)
    username = Entry(app)
    username.grid(row=3, column=1)
    Label(app, text="Enter your username:", font=('Georgia', 12)).grid(row=3, column=0)
    password = Entry(app)
    password.grid(row=4, column=1)
    Label(app, text="Enter your password:", font=('Georgia', 12), ).grid(row=4, column=0)
    Button(app, text="Register", bg="black", fg="white", font=('Georgia', 14),
           command=lambda: register(username.get(), password.get(), username=username.get(), password=password.get(),
                                    first_name=first_name.get(), last_name=last_name.get())).grid(row=5, column=2)
    Button(app, text="Go Back", bg="black", fg="white", font=('Georgia', 14),
           command=render_main_enter_screen).grid(row=6, column=2)


def render_main_enter_screen():
    clean_screen()
    Label(app, text="Welcome to my first shop!", fg="black", font=('Georgia', 12)).grid(row=0, column=0)
    Label(app, text="If you don't have account please use registration form: ",
          fg="black", font=('Georgia', 12), justify="left").grid(row=1, column=0)
    Label(app, text="To see our products, please: ", fg="black", font=('Georgia', 12), justify="left").grid(row=2,
                                                                                                            column=0)
    Button(app, text="Login", bg="black", fg="white", font=('Georgia', 14), command=render_login).grid(
        row=2, column=1)
    Button(app, text="Register", bg="black", fg="white", font=('Georgia', 14),
           command=render_register).grid(row=1,
                                         column=1)
