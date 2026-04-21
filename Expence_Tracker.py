import tkinter as tk
from tkinter import messagebox

FILE_NAME = "expenses.txt"


def add_expense():
    name = entry_name.get()
    amount = entry_amount.get()

    if name == "" or amount == "":
        messagebox.showerror("Error", "Enter all fields")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Invalid amount")
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{amount}\n")

    messagebox.showinfo("Success", "Expense added")

    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


def view_expenses():
    listbox.delete(0, tk.END)

    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                listbox.insert(tk.END, line.strip())


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                _, amount = line.strip().split(",")
                total += float(amount)

    messagebox.showinfo("Total Expense", f"{total}")

def exit_app():
    root.quit() 
def clear_list():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

tk.Label(root, text="Expense Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()


tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=5)
tk.Button(root, text="Total Expense", command=total_expense).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)
tk.Button(root, text="Clear List", command=clear_list).pack(pady=5) 

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)


root.mainloop()
