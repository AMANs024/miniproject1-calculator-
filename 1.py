import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying input and results
entry = tk.Entry(root, font=("Arial", 18), justify="right", borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Creating buttons in a grid
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the application
root.mainloop()
