import json

from gui_product_shop.clean_screan_view import clean_screen

from gui_product_shop.global_window import app

from PIL import ImageTk, Image

from tkinter import Button, Label


def check_if_product_available(product_count):
    if product_count == 0:
        return False
    return True


def reduce_available_products(product_id):
    file_path = "db\\available_products.txt"
    with open(file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            products = json.loads(line)
            if products["id"] == product_id:
                products['count'] -= 1
            file.write(json.dumps(products))
            file.write("\n")


def add_products(*args):
    user, product_id, product_count = args
    if check_if_product_available(product_count):
        file_path = "db\\users.txt"
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                user_info = json.loads(line)
                if user_info['username'] == user:
                    user_info['products'].append(product_id)
                    reduce_available_products(product_id)
                file.write(json.dumps(user_info))
                file.write("\n")
                render_products_view(user)
    else:
        error_text = "Product is not available"
        return Label(app, text=error_text, fg="red", font=('Georgia', 14), justify="left").grid(row=1,
                                                                                                column=product_id - 1)


def load_product_view(*args, **kwargs):
    col, user = args
    products = kwargs
    product_name = f"{products['name']}"
    product_count = f"available: {products['count']}"
    button_text = "Buy"
    exit_text = "Logout"
    image_path = products['image_path']
    image = Image.open(image_path)
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image=photo)
    image_label.image = photo
    image_label.grid(row=2, column=col)
    Label(app, text=product_name, fg="black", font=('Georgia', 12), justify="left").grid(row=1, column=col)
    Label(app, text=product_count, fg="black", font=('Georgia', 12), justify="left").grid(row=3, column=col)
    Button(app, text=button_text, bg="black", fg="white", font=('Georgia', 14),
           command=lambda: add_products(user, products['id'], products['count'])).grid(row=4, column=col)


def render_products_view(user):
    fail_path = "db\\available_products.txt"
    clean_screen()
    welcome_text = f"Hello {user}"
    Label(app, text=welcome_text, fg="black", font=('Georgia', 12), justify="left").grid(row=0, column=0)
    with open(fail_path, 'r') as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            line.rstrip()
            load_product_view(counter, user, **json.loads(line))
            counter += 1
