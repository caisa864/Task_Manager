import tkinter as tk
from tkcalendar import DateEntry
from datetime import date

def change_date():
    # Create new window
    window = tk.Toplevel()
    window.geometry("500x400")

    # Divide window in 2
    left_frame = tk.Frame(
        window,
        bd=1,
        relief=tk.RIDGE)
    
    left_frame.pack(
        side=tk.LEFT, 
        fill=tk.BOTH, 
        expand=True
    )

    right_frame = tk.Frame(
        window,
        bd=1,
        relief=tk.RIDGE)
    
    right_frame.pack(
        side=tk.RIGHT, 
        fill=tk.BOTH, 
        expand=True
    )

    # Setup Canvas and Scrollbar
    canvas = tk.Canvas(
        left_frame,
        width=200,
        height=300
        )

    scrollbar = tk.Scrollbar(
        left_frame,
        orient=tk.VERTICAL,
        command=canvas.yview
        )
    scrollbar.pack(side="right", fill="y")
    
    scrollable_frame = tk.Frame(canvas)
    
    # Configure scrollable area
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Draw frame in canvas and pack scrollbar
    canvas.create_window((125, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Describe what this page do
    label = tk.Label(
        right_frame,
        text = "Mark the task(s) to change the date for,\nand then choose the new due date."
    )
    label.pack(padx=5, pady=10)

    # Read unfinished tasks
    check_vars = []

    with open("app_memory.txt", "r+", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Title: "):
                title_line = line.replace("Title: ", "").strip("\n")
            elif line.startswith("Due Date: "):
                due_line = line.strip("\n")
            elif line.startswith("Priority: "):
                pri_line = line.strip("\n")
            elif line.startswith("Status: "):
                status_line = line.strip("\n")

                # Print title and checkbox
                done = tk.BooleanVar()

                checkbutton = tk.Checkbutton(
                    scrollable_frame, 
                    text = f"{title_line}".strip("\n"), 
                    variable = done,
                    )
                checkbutton.pack()
                checkbutton.deselect()

                check_vars.append((title_line, done))    

                # Print other info
                label = tk.Label(scrollable_frame,
                    text=f"{due_line}\n{pri_line}\n{status_line}\n",
                    anchor = "center",
                    justify="left")
                label.pack()

    # Enter the new due date
    today = date.today()

    due_label = tk.Label(
        right_frame, 
        text="Enter new due date: ", 
        )
    due_label.pack(padx=5, pady=5)

    cal = DateEntry(
        right_frame, 
        date_pattern = "yyyy-mm-dd", 
        mindate=today,
        )
    cal.pack(padx=5, pady=(5, 15))

    # Save new due date
    def due_data():

        checked_titles = []

        for title, var in check_vars:
            if var.get():
                checked_titles.append(title)
                # 変更されたタスクのタイトルを保存
                all_checked = ", ".join(checked_titles)

        with open("app_memory.txt", "r") as file:
            lines = file.readlines()

            current_title = ""
            new_date = cal.get()

            for i in range(len(lines)):
                if lines[i].startswith("Title: "):
                    current_title = lines[i].replace("Title: ", "").strip()
                elif lines[i].startswith("Due Date: "):
                        if current_title in checked_titles:
                            lines[i] = f"Due Date: {new_date}\n"
                            # 選択されたタスクの期限のみを変更

        with open("app_memory.txt", "w", encoding="UTF-8") as file:
            file.writelines(lines)
        
        message.config(text = f"The due date for {all_checked}\nwas changed to {new_date}.")
        message2.config(text = "Please update the page.")

    button = tk.Button(
        right_frame,
        text = "Save",
        command = due_data,
        anchor = "center",
        justify = "center"
        )
    button.pack(padx=0, pady=(5, 20))

    message = tk.Label(right_frame)
    message.pack(padx=5, pady=15)
    message2 = tk.Label(right_frame)
    message2.pack(padx=5, pady=(0))

    def ret_menu():
        window.destroy()

    return_button = tk.Button(
        right_frame,
        text = "Return to main menu",
        command = ret_menu
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")