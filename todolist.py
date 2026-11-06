import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import threading
import time
from datetime import datetime

FILE = "tasks.json"
tasks = []

if os.path.exists(FILE):
    try:
        with open(FILE, 'r') as f:
            tasks = json.load(f)
    except:
        tasks = []

def save():
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def refresh_list():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks, 1):
        listbox.insert(tk.END, f"{i}. {t['name']} | {t['priority']} | {t['time']}")

def add_task():
    name = entry_task.get()
    if not name:
        messagebox.showwarning("Empty", "Enter task name")
        return

    priority = combo_priority.get()
    notify_time = entry_time.get()

    tasks.append({"name": name, "priority": priority, "time": notify_time})
    save()
    refresh_list()
    entry_task.delete(0, tk.END)
    entry_time.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save()
        refresh_list()
    except:
        messagebox.showwarning("Select", "Select a task to delete")

def upgrade_task():
    try:
        index = listbox.curselection()[0]
        name = entry_task.get()
        if name:
            tasks[index]['name'] = name
        tasks[index]['priority'] = combo_priority.get()
        tasks[index]['time'] = entry_time.get()
        save()
        refresh_list()
        messagebox.showinfo("Done", "Task Upgraded!")
    except:
        messagebox.showwarning("Select", "Select a task and enter new name")

def notify_with_sound():
    root.bell() # This plays system sound
    print('\a')
    messagebox.showinfo("Reminder 🔔", "Check your tasks! \n" + "\n".join([t['name'] for t in tasks]))

def show_priority():
    imp = [t['name'] for t in tasks if "IMPORTANT" in t['priority']]
    norm = [t['name'] for t in tasks if "NORMAL" in t['priority']]
    messagebox.showinfo("Priority Tasks",
        f"IMPORTANT - Office Work:\n{', '.join(imp) if imp else 'None'}\n\nNORMAL - Eating/Daily:\n{', '.join(norm) if norm else 'None'}")

def auto_checker():
    while True:
        now = datetime.now().strftime("%H:%M")
        for t in tasks:
            if t['time'] == now and t['time']!= "":
                root.bell()
                print('\a')
        time.sleep(60)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Upgraded ToDo List")
root.geometry("500x500")

tk.Label(root, text="Task Name:").pack()
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

tk.Label(root, text="Priority:").pack()
combo_priority = ttk.Combobox(root, values=["IMPORTANT - Office Work", "NORMAL - Eating / Daily"], width=37)
combo_priority.current(1)
combo_priority.pack(pady=5)

tk.Label(root, text="Notify Time (HH:MM) e.g. 21:30:").pack()
entry_time = tk.Entry(root, width=40)
entry_time.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add Task", command=add_task, bg="lightgreen").grid(row=0, column=0, padx=5)
tk.Button(frame, text="Delete", command=delete_task, bg="lightcoral").grid(row=0, column=1, padx=5)
tk.Button(frame, text="Upgrade Task", command=upgrade_task, bg="lightblue").grid(row=0, column=2, padx=5)

frame2 = tk.Frame(root)
frame2.pack()

tk.Button(frame2, text="Notify with Sound 🔔", command=notify_with_sound).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame2, text="Show by Priority", command=show_priority).grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10)

refresh_list()

# start background thread for auto notify
threading.Thread(target=auto_checker, daemon=True).start()

root.mainloop()