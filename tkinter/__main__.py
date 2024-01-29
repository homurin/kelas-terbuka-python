import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# window init

window = tk.Tk()

window.title('Kyubey Apps')
window.configure(bg='white')
window.geometry("300x200")
window.resizable(False, False)

# variable and function

FIRST_NAME = tk.StringVar()
LAST_NAME = tk.StringVar()


def click_button():
    title = 'GOOD NEWS'
    message = f'YOU SHOULD BECOME MAGICAL GIRL! {FIRST_NAME.get()} {LAST_NAME.get()}'
    showinfo(title=title, message=message)

# frame


frame_input = ttk.Frame(window)

# grid, pack, place

frame_input.pack(padx=10, pady=10, fill='x', expand=True)

# components

# label

first_name_label = ttk.Label(frame_input, text='First Name')
first_name_label.pack(padx=10, pady=3, fill='x', expand=True)

# entry

first_name_entry = ttk.Entry(frame_input, textvariable=FIRST_NAME)
first_name_entry.pack(padx=10, pady=3, fill='x', expand=True)

# label

last_name_label = ttk.Label(frame_input, text='Last Name')
last_name_label.pack(padx=10, pady=3, fill='x', expand=True)

# entry

last_name_entry = ttk.Entry(frame_input, textvariable=LAST_NAME)
last_name_entry.pack(padx=10, pady=3, fill='x', expand=True)

# button


greeting_button = ttk.Button(
    frame_input, text='Greeting!', command=click_button)

greeting_button.pack(fill='x', padx=10, pady=5)


window.mainloop()
