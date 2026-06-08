import tkinter as tk

def change_detail():
# Create new window
    window = tk.Toplevel()
    window.geometry("300x300")

    # 1. Change priority
    from priority import change_pri

    button = tk.Button(
        window,
        text="Change priority",
        command=change_pri,
        width=20,
        height=3,
        font = ("Arial", 10)
    )
    button.pack(padx=(5,5), pady=(15, 15))

    # 2. Change status
    from status import change_status

    button = tk.Button(
        window,
        text="Change status",
        command=change_status,
        width=20,
        height=3,
        font = ("Arial", 10)
    )
    button.pack(padx=(5,5), pady=(5, 15))

    # 3. Change due date
    from date import change_date

    button = tk.Button(
        window,
        text="Change due date",
        command=change_date,
        width=20,
        height=3,
        font = ("Arial", 10)
    )
    button.pack(padx=(5,5), pady=(5, 15))

    def ret_menu():
        window.destroy()

    return_button = tk.Button(
        window,
        text = "Return to main menu",
        command = ret_menu
    )
    return_button.pack(padx=5, pady=(5, 15), side = "bottom")