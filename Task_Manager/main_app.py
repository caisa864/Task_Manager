import tkinter as tk
import os

root = tk.Tk()

base_dir = os.path.dirname(__file__)

root.title("Task Manager")
root.geometry("450x400")

title = tk.Label(root, text="Task Manager", font=("Arial", 15))
title.pack(padx=5, pady=15)

# Divide window in 3
left_frame = tk.Frame(
    root,
    bd=0,
    relief=tk.FLAT,
    height = 200
    )

left_frame.pack(
    side= tk.LEFT,
    fill= "both", 
    expand=True
)

right_frame = tk.Frame(
    root,
    bd=1,
    relief=tk.FLAT)

right_frame.pack(
    side=tk.RIGHT,
    fill=tk.BOTH, 
    expand=True
)

bottom_frame = tk.Frame(
    root,
    bd=0,
    relief=tk.FLAT)

bottom_frame.pack(
    side= "bottom"
)

# 1.Show tasks
from tasks import show_tasks

button1 = tk.Button(
    left_frame,
    text="Show tasks",
    command=show_tasks,
    width=20,
    height=3,
    font = ("Arial", 10)
)
button1.pack(padx=(20,5), pady=(5, 15))

# 2.Add task
from add import add_task

button3 = tk.Button(
left_frame,
text = "Add task",
command = add_task,
width=20,
height=3,
font = ("Arial", 10)
)
button3.pack(padx=(20,5), pady=(5, 15))

# 3. Mark task as finished/unfinished
from status import change_status

button = tk.Button(
    right_frame,
    text="Mark tasks as\nfinished/unfinished",
    command=change_status,
    width=20,
    height=3,
    font = ("Arial", 10)
)
button.pack(padx=(5,20), pady=(5, 15))

# 4. Change due date
from date import change_date

button = tk.Button(
    right_frame,
    text="Change due date",
    command=change_date,
    width=20,
    height=3,
    font = ("Arial", 10)
)
button.pack(padx=(5,20), pady=(5, 15))

# 5. Delete task
from delete import delete_task

button = tk.Button(
    right_frame,
    text="Delete task",
    command=delete_task,
    width=20,
    height=3,
    font = ("Arial", 10)
)
button.pack(padx=(5,20), pady=(5, 15))

# 6 Delete all tasks (reset)
def reset_all():
    with open("app_memory.txt", "w", encoding="utf-8") as file:
        file.writelines("")

button = tk.Button(
    bottom_frame,
    text = "Reset",
    command = reset_all,
    font = ("Arial", 5)
)
button.pack(padx=5, pady=5, side="bottom")

# 7. Exit
button = tk.Button(
    bottom_frame,
    text="Exit",
    command=root.destroy,
    width=20,
    height=2,
    font = ("Arial", 10)
)
button.pack(padx=5, pady=(5, 15), side = "bottom")

root.mainloop()