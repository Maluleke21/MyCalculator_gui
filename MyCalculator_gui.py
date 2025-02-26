import tkinter as tk
from datetime import datetime

# Function to update the input field
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def clear_field():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))  # Evaluates the string expression
        log_operation(expression, result)  # Log the operation and result
        input_text.set(result)
        expression = result
    except Exception as e:
        log_operation(expression, "Error")  # Log the error
        input_text.set("Error")
        expression = ""

# Function to log operations
def log_operation(operation, result):
    """Logs operations to a file."""
    with open("operation_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} | Operation: {operation} | Result: {result}\n")

# Main program
expression = ""

# Create a window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.resizable(False, False)
window.configure(bg="#2C2C2C")

# Input field
input_text = tk.StringVar()
input_frame = tk.Frame(window, bg="#2C2C2C")
input_frame.pack(pady=10)

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=("Arial", 24),
    bg="#EEE",
    bd=10,
    justify="right"
)
input_field.grid(row=0, column=0, ipadx=8, ipady=15, columnspan=4)

# Button frame
btn_frame = tk.Frame(window, bg="#2C2C2C")
btn_frame.pack(pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Create buttons dynamically
for (text, row, col, *span) in buttons:
    btn_kwargs = {
        "font": ("Arial", 18),
        "fg": "white",
        "height": 2,
        "width": 8,
        "bd": 0,
        "highlightthickness": 0,
        "relief": "solid",  # Add border for better visibility
    }
    if text == "=":
        btn_kwargs.update({
            "bg": "#009688",
            "command": calculate,
            "width": 36,
        })
        btn = tk.Button(btn_frame, text=text, **btn_kwargs)
        btn.grid(row=row, column=col, columnspan=span[0], pady=5)
    elif text == "C":
        btn_kwargs.update({
            "bg": "#f44336",
            "command": clear_field,
        })
        btn = tk.Button(btn_frame, text=text, **btn_kwargs)
        btn.grid(row=row, column=col, pady=5)
    else:
        btn_kwargs.update({
            "bg": "#333",
            "command": lambda t=text: button_click(t),
        })
        btn = tk.Button(btn_frame, text=text, **btn_kwargs)
        btn.grid(row=row, column=col, pady=5)

# Run the GUI loop
window.mainloop()
