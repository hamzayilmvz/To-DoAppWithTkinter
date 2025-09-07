import tkinter as tk
from asyncio import tasks
from tkinter import messagebox

tasks=[]

def add_task():
    task=entry.get()
    if task !="":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task")

def delete_task():
    try:
        selected_index=listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showerror("Error", "Please select a task")

def clear_task():
    listbox.delete(0, tk.END)
    tasks.clear()


root=tk.Tk()
root.title("To-Do App With Tkinter")
root.geometry("400x400")

entry=tk.Entry(root,width=30)
entry.pack(pady=10)

listbox=tk.Listbox(root,width=40,height=10)
listbox.pack(pady=10)

add_button=tk.Button(root,text="Add To-Do",command=add_task)
add_button.pack(pady=5)

delete_button=tk.Button(root,text="Delete To-Do",command=delete_task)
delete_button.pack(pady=5)

clear_button=tk.Button(root,text="Clear List",command=clear_task)
clear_button.pack(pady=5)


root.mainloop()