from tkinter import Tk


def create_app():
    tk = Tk()
    tk.geometry("700x500")
    text = 'My first GUI'
    tk.title(text)
    return tk


app = create_app()
