import tkinter as tk

def show_tasks():
    # Create new window
    window = tk.Toplevel()
    window.geometry("500x500")

    # Setup frames
    bottom_frame = tk.Frame(
        window,
        height = 50
        )
    bottom_frame.pack(
        side = "bottom",
        fill = "x"
        )
    
    bottom_frame.pack_propagate(False)
    
    left_frame = tk.Frame(
        window,
        bd=0,
        relief=tk.RIDGE,
        height = 450,
        width = 250
        )
    
    left_frame.pack(side=tk.LEFT)

    right_frame = tk.Frame(
        window,
        bd=0,
        relief=tk.RIDGE,
        height = 450,
        width = 250
        )
    
    right_frame.pack(side=tk.RIGHT)

    # Setup canvas and scrollbar
    canvas_left = tk.Canvas(
        left_frame,
        width=250,
        height=450
        )

    canvas_right = tk.Canvas(
        right_frame,
        width=250,
        height=450
        )
    

    # Setup left scrollbar
    scrollbar_left = tk.Scrollbar(
        left_frame,
        orient=tk.VERTICAL,
        command=canvas_left.yview
        )
    scrollbar_left.pack(side="right", fill="y")
    
    scrollable_left = tk.Frame(canvas_left)

    scrollable_left.bind(
        "<Configure>",
        lambda e: canvas_left.configure(scrollregion=canvas_left.bbox("all"))
    )

    canvas_left.create_window((0, 0), window=scrollable_left, anchor="nw")
    canvas_left.configure(yscrollcommand=scrollbar_left.set)
    canvas_left.pack(side="left", fill="both", expand=True)
    scrollbar_left.pack(side="right", fill="y")

    # Setup right scrollbar

    scrollbar_right = tk.Scrollbar(
        right_frame,
        orient=tk.VERTICAL,
        command=canvas_right.yview
        )
    scrollbar_right.pack(side="right", fill="y")
    
    scrollable_right = tk.Frame(canvas_right)

    scrollable_right.bind(
        "<Configure>",
        lambda e: canvas_right.configure(scrollregion=canvas_right.bbox("all"))
    )

    canvas_right.create_window((0, 0), window=scrollable_right, anchor="nw")
    canvas_right.configure(yscrollcommand=scrollbar_right.set)
    canvas_right.pack(side="right", fill="both", expand=True)
    scrollbar_right.pack(side="right", fill="y")

    # Show unfinished tasks
    unfinished = tk.Label(
        scrollable_left,
        text = "Unfinished Tasks",
        font = ("Arial", 12)
    )
    unfinished.pack(padx = 5, pady = 10)
    
    with open("app_memory.txt", "r", encoding="UTF=8") as file:
        content = file.readlines()
        
        lines = ""

        for i in range(len(content)):
            if content[i].strip() == "Status: Unfinished":
                lines += "".join(content[i-4:i]) + "\n"

    un_text = tk.Label(scrollable_left,
        text = lines,
        anchor = "center",
        justify = "left")
    un_text.pack(padx=5,pady=10)

    # Show on hold tasks
    unfinished = tk.Label(
        scrollable_right,
        text = "On Hold Tasks",
        font = ("Arial", 12)
    )
    unfinished.pack(padx = 5, pady = 10)
    
    with open("app_memory.txt", "r", encoding="UTF=8") as file:
        content = file.readlines()
        
        lines = ""

        for i in range(len(content)):
            if content[i].strip() == "Status: On hold":
                lines += "".join(content[i-4:i]) + "\n"

    hold_text = tk.Label(scrollable_right,
        text = lines,
        anchor = "center",
        justify = "left")
    hold_text.pack(padx=5,pady=10)

    def ret_menu():
        (window.destroy())

    return_button = tk.Button(
        bottom_frame,
        text = "Return to main menu",
        command = ret_menu,
        anchor = "s"
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")