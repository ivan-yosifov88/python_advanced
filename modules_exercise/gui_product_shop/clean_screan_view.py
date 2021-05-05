from gui_product_shop.global_window import app


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()