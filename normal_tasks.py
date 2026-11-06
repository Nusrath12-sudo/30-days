import json
import os
import time
import threading
from datetime import datetime

# File to save tasks
SAVE_FILE = "my_tasks.json"

# Load old tasks if exist
tasks = []
if os.path.exists(SAVE_FILE):
    try:
        with open(SAVE_FILE, 'r') as f:
            tasks = json.load(f)
    except:
        tasks = []

class upgraded_tasks():

    @staticmethod
    def add_task():
        task_name = input("add your tasks: ")
        if not task_name:
            print("Task empty!")
            return

        print("\nSet Priority:")
        print("1. Important - office work, college work")
        print("2. Normal - eating, sleeping, walking")
        priority = input("Choose 1 or 2: ")

        if priority == '1':
            p_text = "IMPORTANT - Office Work"
        else:
            p_text = "NORMAL - Eating/Normal Work"

        time_str = input("Notify time? (HH:MM like 19:30) or press Enter to skip: ")

        new_task = {
            "name": task_name,
            "priority": p_text,
            "notify_time": time_str,
            "created": datetime.now().strftime("%d-%m-%Y %H:%M")
        }
        tasks.append(new_task)
        print(f"Task Added -> {task_name} [{p_text}]")
        upgraded_tasks.save_task()

    @staticmethod
    def delete_task():
        if not tasks:
            print("No tasks to delete")
            return

        upgraded_tasks.show_all_tasks()
        try:
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f"Deleted: {removed['name']}")
                upgraded_tasks.save_task()
            else:
                print("Wrong number")
        except:
            print("Enter valid number")

    @staticmethod
    def upgrade_task():
        if not tasks:
            print("No tasks to upgrade")
            return

        upgraded_tasks.show_all_tasks()
        try:
            num = int(input("Enter task number to upgrade/edit: ")) - 1
            if 0 <= num < len(tasks):
                print(f"Old Task: {tasks[num]['name']}")
                new_name = input("Enter new task name (press Enter to keep same): ")
                if new_name:
                    tasks[num]['name'] = new_name

                # upgrade priority also
                new_p = input("Upgrade priority? 1=Important, 2=Normal, Enter=keep: ")
                if new_p == '1':
                    tasks[num]['priority'] = "IMPORTANT - Office Work"
                elif new_p == '2':
                    tasks[num]['priority'] = "NORMAL - Eating/Normal Work"

                print("Task Upgraded!")
                upgraded_tasks.save_task()
            else:
                print("Wrong number")
        except:
            print("Enter valid number")

    @staticmethod
    def save_task():
        with open(SAVE_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
        # print("Tasks saved to file")

    @staticmethod
    def show_all_tasks():
        if not tasks:
            print("--- No tasks ---")
            return
        print("\n--- Your Tasks ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['name']} | {t['priority']} | Notify: {t['notify_time']} | {t['created']}")

    @staticmethod
    def notifies_tasks_without_sound():
        print("\n[Notification - No Sound]")
        upgraded_tasks.show_all_tasks()

    @staticmethod
    def notifies_tasks_with_sound():
        print("\n[Notification - WITH SOUND] \a") # \a makes beep sound
        # For Debian Linux, this will make bell sound
        print('\a')
        try:
            os.system('echo -e "\\a"') # extra beep for linux
        except:
            pass
        upgraded_tasks.show_all_tasks()
        print("🔔 Beep! Check your tasks!")

    @staticmethod
    def set_pririty_tasks():
        # This groups tasks by priority
        def normal_priority_tasks():
            print("\n--- NORMAL Priority (eating, daily work) ---")
            found = False
            for t in tasks:
                if "NORMAL" in t['priority']:
                    print(f"- {t['name']}")
                    found = True
            if not found:
                print("No normal tasks")

        def important_priority_tasks():
            print("\n--- IMPORTANT Priority (office work) ---")
            found = False
            for t in tasks:
                if "IMPORTANT" in t['priority']:
                    print(f"- {t['name']}")
                    found = True
            if not found:
                print("No important tasks")

        # call both
        important_priority_tasks()
        normal_priority_tasks()

    @staticmethod
    def auto_notify_checker():
        # This runs in background and checks time
        while True:
            now = datetime.now().strftime("%H:%M")
            for t in tasks:
                if t['notify_time'] == now:
                    print(f"\n\n🔔🔔 REMINDER 🔔🔔 Task: {t['name']} [{t['priority']}]")
                    print('\a')
                    try:
                        os.system('spd-say "Task reminder"') # voice on Debian if installed
                    except:
                        pass
            time.sleep(60) # check every 1 minute

# --- Start background notifier ---
thread = threading.Thread(target=upgraded_tasks.auto_notify_checker, daemon=True)
thread.start()

# --- Main Menu ---
print("Todolist - Upgraded Version")

while True:
    print("\n======== MENU ========")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Upgrade/Edit Task")
    print("4. Show All Tasks")
    print("5. Show by Priority")
    print("6. Notify without sound")
    print("7. Notify with sound")
    print("8. Exit")

    ch = input("Choose 1-8: ")

    if ch == '1':
        upgraded_tasks.add_task()
    elif ch == '2':
        upgraded_tasks.delete_task()
    elif ch == '3':
        upgraded_tasks.upgrade_task()
    elif ch == '4':
        upgraded_tasks.show_all_tasks()
    elif ch == '5':
        upgraded_tasks.set_pririty_tasks()
    elif ch == '6':
        upgraded_tasks.notifies_tasks_without_sound()
    elif ch == '7':
        upgraded_tasks.notifies_tasks_with_sound()
    elif ch == '8':
        print("Bye! Tasks saved.")
        break
    else:
        print("Wrong choice")