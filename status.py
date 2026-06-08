import tkinter as tk

def change_status():
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
        width=150,
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

    check_vars = []

    # Describe what this page do
    label = tk.Label(
    right_frame,
    text = "Mark the task(s) to change the\n status of, and then choose the\nnew status from down below."
    )
    label.pack(padx=5, pady=10)

    # Read textfile
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
                    anchor = "center",
                    justify = "left"
                    )
                checkbutton.pack()
                checkbutton.deselect()

                check_vars.append((title_line, done))    

                # Print other info
                label = tk.Label(scrollable_frame,
                    text=f"{due_line}\n{pri_line}\n{status_line}\n",
                    anchor = "w",
                    justify = "left")
                label.pack()

            # Mark task as finished
            def mark_finished():
                checked_titles = []

                for title, var in check_vars:
                    if var.get():
                        checked_titles.append(title)
                    all_checked = ", ".join(checked_titles)

                with open("app_memory.txt", "r") as file:
                    lines = file.readlines()

                    current_title = ""

                    for i in range(len(lines)):
                        if lines[i].startswith("Title: "):
                            current_title = lines[i].replace("Title: ", "").strip()
                        elif lines[i].startswith("Status: "):
                                if current_title in checked_titles:
                                    lines[i] = "Status: Finished\n"

                with open("app_memory.txt", "w", encoding="UTF-8") as file:
                    file.writelines(lines)

                message.config(text = f"{all_checked} changed to finished.")
                message2.config(text = "Please update the page.")

            # Mark task as finished
            def mark_unfinished():
                checked_titles = []

                for title, var in check_vars:
                    if var.get():
                        checked_titles.append(title)
                    all_checked = ", ".join(checked_titles)

                with open("app_memory.txt", "r") as file:
                    lines = file.readlines()

                    current_title = ""

                    for i in range(len(lines)):
                        if lines[i].startswith("Title: "):
                            current_title = lines[i].replace("Title: ", "").strip()
                        elif lines[i].startswith("Status: "):
                                if current_title in checked_titles:
                                    lines[i] = "Status: Unfinished\n"

                with open("app_memory.txt", "w", encoding="UTF-8") as file:
                    file.writelines(lines)

                message.config(text = f"{all_checked} changed to unfinished.")
                message2.config(text = "Please update the page.")

            # Mark task as on hold
            def mark_hold():
                checked_titles = []

                for title, var in check_vars:
                    if var.get():
                        checked_titles.append(title)
                    all_checked = ", ".join(checked_titles)

                with open("app_memory.txt", "r") as file:
                    lines = file.readlines()

                    current_title = ""

                    for i in range(len(lines)):
                        if lines[i].startswith("Title: "):
                            current_title = lines[i].replace("Title: ", "").strip()
                        elif lines[i].startswith("Status: "):
                                if current_title in checked_titles:
                                    lines[i] = "Status: On hold\n"

                with open("app_memory.txt", "w", encoding="UTF-8") as file:
                    file.writelines(lines)

                message.config(text = f"{all_checked} changed to on hold.")
                message2.config(text = "Please update the page.")

    button = tk.Button(
        right_frame,
        text = "Mark as finished",
        command = mark_finished
        )
    button.pack(padx=0, pady=(5, 20))

    button2 = tk.Button(
        right_frame,
        text = "Mark as unfinished",
        command = mark_unfinished
    )
    button2.pack(padx=0, pady=(5, 20))

    button3 = tk.Button(
        right_frame,
        text = "Mark as on hold",
        command = mark_hold
    )
    button3.pack(padx=0, pady=(5, 20))

    message = tk.Label(right_frame)
    message.pack(padx=5, pady=15)
    message2 = tk.Label(right_frame)
    message2.pack(padx=5, pady=0)
    message3 = tk.Label(right_frame)
    message3.pack(padx=5, pady=0)

    def ret_menu():
        window.destroy()

    return_button = tk.Button(
        right_frame,
        text = "Return",
        command = ret_menu
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")