import tkinter as tk
import os

root = tk.Tk()

base_dir = os.path.dirname(__file__)

root.title("Task Manager")
root.geometry("450x300")

title = tk.Label(root, text="Task Manager", font=("Arial", 15))
title.pack(padx=5, pady=15)

# Divide window in 3
bottom_frame = tk.Frame(
    root,
    bd=0,
    relief=tk.FLAT)

bottom_frame.pack(
    side= "bottom"
)

left_frame = tk.Frame(
    root,
    bd=0,
    relief=tk.FLAT
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

# 1.Show tasks
from tasks import show_tasks

button = tk.Button(
    left_frame,
    text="Show tasks",
    command=show_tasks,
    width=20,
    height=3,
    font = ("Arial", 10)
)
button.pack(padx=(20,5), pady=(5, 15))

# 2.Add task
from add import add_task

button = tk.Button(
left_frame,
text = "Add task",
command = add_task,
width=20,
height=3,
font = ("Arial", 10)
)
button.pack(padx=(20,5), pady=(5, 15))

# 3. Change details
from change import change_detail

button = tk.Button(
right_frame,
text = "Change details",
command = change_detail,
width=20,
height=3,
font = ("Arial", 10)
)
button.pack(padx=(5,20), pady=(5, 15))


# 4. Delete task
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

# 5 Delete all tasks (reset)
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

# 6. Exit
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