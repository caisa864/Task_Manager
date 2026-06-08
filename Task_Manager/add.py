import tkinter as tk
from tkcalendar import DateEntry
from datetime import date

def add_task():
    # Create new window
    window = tk.Toplevel()
    window.geometry("300x550")

    output = tk.Label(
    window,
    text="",
    justify="left",
    anchor="w"
    )
    output.pack(pady=10)

    # Enter title
    add_label = tk.Label(window, text="Task title:")
    add_label.pack(padx=5, pady=5)
    
    enter_title = tk. Entry(window)
    enter_title.insert(0,"")
    enter_title.pack(padx=5, pady=(5, 15))

    # Enter due date by calendar
    today = date.today()

    due_label = tk.Label(window, text="Due date:", anchor="w")
    due_label.pack(padx=5, pady=5)

    cal = DateEntry(window, date_pattern = "yyyy-mm-dd", mindate=today)
    cal.pack(padx=5, pady=(5, 15))

    # Enter priority by radiobutton
    priority = [1, 2, 3]

    variable = tk.IntVar(window, f"{priority[0]}")

    pri_label = tk.Label(
        window,
        text = "Priority:",
    )
    pri_label.pack(padx=5, pady=5)

    def sel_pri():
        pass
    
    for pr in priority:
        tk.Radiobutton(
            window,
            text = pr,
            variable = variable,
            value = pr,
            command = sel_pri,
        ).pack(padx=5, pady=(5, 15))

    # Enter description
    desc_label = tk.Label(window, text="Description:")
    desc_label.pack(padx=5, pady=5)

    enter_desc = tk. Entry(window)
    enter_desc.insert(0,"")
    enter_desc.bind("<Return>", sel_pri)
    enter_desc.pack(padx=5, pady=(5, 15), fill="y")

    # Save button
    def title_data():
        with open("app_memory.txt", "a+") as file:
            # Save title
            text = enter_title.get()
            file.write(f"Title: {text}\n")

            ## Save due date
            text = cal.get()
            file.write(f"Due Date: {text}\n")

            ## Save priority
            variable = tk.IntVar(window, f"{priority[0]}")
            text = variable.get()
            file.write(f"Priority: {text}\n")

            ## Save description
            text = enter_desc.get()
            file.write(f"Description: {text}\nStatus: Unfinished\n\n")

            saved = tk.Label(window, text = "Data saved")
            saved.pack(padx=5, pady=15)

    save_button = tk.Button(window, text="Save", command=title_data)
    save_button.pack(padx=5, pady=(5, 15))

    def ret_menu():
        (window.destroy())

    return_button = tk.Button(
        window,
        text = "Return to main menu",
        command = ret_menu
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")