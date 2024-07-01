from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from customtkinter import *

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class TodoListApp:
    def __init__(self, root):
        self.root = CTk()
        self.root.title("To-Do List App")
        self.root.geometry("500x300")
        self.tasks = []

        self.task_entry = CTkEntry(root, width=120, height=5)
        self.task_entry.place(x=360, y=25)
        self.task_entry.bind('Return', lambda event:self.add_task)

        add_button = CTkButton(root, width=100, command=self.add_task, text="Add Task", corner_radius=15)   
        add_button.place(x=370, y=75)

        self.task_listbox = CTkListBox(root, width=335, height=230)
        self.task_listbox.place(x=10, y=25)

        remove_button = CTkButton(root, width=100, command=self.remove_task, text="Delete Task", corner_radius=15)
        remove_button.place(x=370, y=125)

        #complete_button = CTkButton(root, text="Complete Task", command=self.complete_task, font=('Arial', 12), bg="#f39c12", fg="#ecf0f1")  # Set button colors
        #complete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.complete_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            self.tasks.append(completed_task)
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    root = CTk()
    root.geometry("500x300")
    app = TodoListApp(root)
    root.mainloop()
