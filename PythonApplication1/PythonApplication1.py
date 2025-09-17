import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Negative input"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Consolas', 12))
        style.configure("TEntry", padding=5)

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(fill="x")
        self.display = ttk.Entry(display_frame, textvariable=self.result_var, font=('Consolas', 18), state="readonly", justify="right")
        self.display.pack(fill="x", ipady=10)

        # Button layout
        btn_frame = ttk.Frame(self.root, padding="10")
        btn_frame.pack(fill="both", expand=True)

        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'pow'],
            ['1', '2', '3', '-', 'sin'],
            ['0', '.', 'C', '+', 'cos'],
            ['(', ')', '=', 'tan', '']
        ]

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                if label:
                    btn = ttk.Button(btn_frame, text=label, width=6, command=lambda l=label: self.on_button_click(l))
                    btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

        # Make buttons expand
        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == '=':
            self.calculate()
        elif char == 'sqrt':
            self.expression += "sqrt("
            self.result_var.set(self.expression)
        elif char == 'pow':
            self.expression += "**"
            self.result_var.set(self.expression)
        elif char == 'sin':
            self.expression += "sin("
            self.result_var.set(self.expression)
        elif char == 'cos':
            self.expression += "cos("
            self.result_var.set(self.expression)
        elif char == 'tan':
            self.expression += "tan("
            self.result_var.set(self.expression)
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

    def calculate(self):
        try:
            # Safe eval with allowed functions
            allowed = {
                'sqrt': sqrt,
                'sin': sin,
                'cos': cos,
                'tan': tan,
                'pow': power,
                '__builtins__': None
            }
            result = eval(self.expression, allowed, {})
            self.result_var.set(str(result))
            self.expression = str(result)
        except Exception as e:
            self.result_var.set("Error")
            self.expression = ""

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()