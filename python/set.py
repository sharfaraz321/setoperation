import tkinter as tk
from tkinter import messagebox

def parse_set(input_str):
    try:
        # Convert comma-separated string into a Python set
        return set(map(str.strip, input_str.split(",")))
    except:
        messagebox.showerror("Error", "Invalid input format!")
        return set()

def perform_operation():
    set1 = parse_set(entry_set1.get())
    set2 = parse_set(entry_set2.get())
    operation = operation_var.get()

    if operation == "Union":
        result = set1 | set2
    elif operation == "Intersection":
        result = set1 & set2
    elif operation == "Difference (A - B)":
        result = set1 - set2
    elif operation == "Difference (B - A)":
        result = set2 - set1
    elif operation == "Symmetric Difference":
        result = set1 ^ set2
    else:
        result = "Invalid operation"

    result_label.config(text=f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Set Operations Program")
root.geometry("400x350")

# Labels and Entries
tk.Label(root, text="Enter Set A (comma-separated):").pack(pady=5)
entry_set1 = tk.Entry(root, width=40)
entry_set1.pack()

tk.Label(root, text="Enter Set B (comma-separated):").pack(pady=5)
entry_set2 = tk.Entry(root, width=40)
entry_set2.pack()

# Operation selection
operation_var = tk.StringVar(value="Union")

operations = [
    "Union",
    "Intersection",
    "Difference (A - B)",
    "Difference (B - A)",
    "Symmetric Difference"
]

tk.Label(root, text="Select Operation:").pack(pady=5)

for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(anchor="w")

# Button
tk.Button(root, text="Compute", command=perform_operation).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ", fg="blue")
result_label.pack(pady=10)

# Run the app
root.mainloop()