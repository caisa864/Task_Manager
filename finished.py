import tkinter as tk

def show_finished():
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

    # Show finished tasks
    finished = tk.Label(
        scrollable_frame,
        text = "Finished Tasks",
        font = ("Arial", 12)
    )
    finished.pack(padx = 5, pady = 10)
    
    with open("app_memory.txt", "r", encoding="UTF=8") as file:
        content = file.readlines()
        
        fin_lines = ""

        for i in range(len(content)):
            if content[i].strip() == "Status: Finished":
                fin_lines += "".join(content[i-4:i]) + "\n"

    fin_text = tk.Label(
        scrollable_frame,
        text = fin_lines,
        anchor = "center",
        justify = "left")
    fin_text.pack(padx=5,pady=10)

    def ret_menu():
        window.destroy()

    return_button = tk.Button(
        right_frame,
        text = "Return",
        command = ret_menu
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")