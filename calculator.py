import tkinter as tk

root = tk.Tk()
root.title("All Operators Calculator")
root.geometry("400x550")

entry = tk.Entry(root, font=("Arial", 200), justify="right")
entry.pack(fill="x", padx=10, pady=10)

def click(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        # This eval can handle +-*/ // % ** == != > < >= <= & | ^ ~ << >> and in, is, and, or, not
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons for ALL your operators
buttons = [
    ['7','8','9','+','=='],
    ['4','5','6','-','!='],
    ['1','2','3','*','>'],
    ['0','.','/','%','<'],
    ['//','**','&','|','^'],
    ['~','<<','>>','and','or'],
    ['not','is','in','not in','is not'],
    ['AC','=']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == 'AC':
            tk.Button(frame, text=btn, font=("Arial", 12), command=clear).pack(side="left", expand=True, fill="both", padx=2, pady=2)
        elif btn == '=':
            tk.Button(frame, text=btn, font=("Arial", 12), bg="orange", command=calculate).pack(side="left", expand=True, fill="both", padx=2, pady=2)
        else:
            tk.Button(frame, text=btn, font=("Arial", 12), command=lambda v=btn: click(f" {v} ")).pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()