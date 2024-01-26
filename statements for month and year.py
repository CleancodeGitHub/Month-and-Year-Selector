""" Now when you press the Print Selected button, it will both print the selected month and year in the console and display a pop-up message with the same information. """

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def print_selected_month():
    print("Selected Month:", month.get())

def print_selected_year():
    print("Selected Year:", year.get())

def show_popup_info():
    messagebox.showinfo("Print Selected Information", "Month: {}\nYear: {}".format(month.get(), year.get()))

root = tk.Tk()
root.title("Month and Year Selector")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), padding=(5, 5))

# Month Selector
month_label = ttk.Label(root, text="Select Month:")
month_label.pack()

month = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=month, values=(
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
combobox.set('Dec')  # Set a default value
combobox.pack()

# Year Selector
year_label = ttk.Label(root, text="Select Year:")
year_label.pack()

year = tk.StringVar()
year_spinbox = ttk.Spinbox(root, from_=1990, to=2023, textvariable=year)
year_spinbox.pack()

# Print selected values
print_button = ttk.Button(root, text="Print Selected", command=lambda: [print_selected_month(), print_selected_year(), show_popup_info()])
print_button.pack()

root.mainloop()

