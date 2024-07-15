from tkinter import *
from tkinter import filedialog
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

curListLen = 0
tasks = [] 
tasks_dict = {}
var_dict = {}


def adicionar(): 
    
    curListLen = len(tasks)

    text = texto.get()
    texto.delete(0, END)
    tasks.append(text)
    var_dict[text] = ctk.StringVar(value="off")
    tasks_dict[text] = ctk.CTkCheckBox(frame, text = f"{text}", variable=var_dict[text], onvalue="on", offvalue="off")        
    tasks_dict[text].place(x=15, y=(10+30*curListLen))

    

# funcao para apagar
def apague():
    text_entry = texto.get()
    #destroi tudo
    for widget in frame.winfo_children():
        widget.destroy()
    if text_entry:
        tasks.remove(text_entry)
    #tira da lista tudo o que tiver on ou escrito 
    for item in tasks:
        if var_dict[item].get() == "on":
            tasks.remove(item)
    
    #reseta count e dicionario
    curListLen = 0
    tasks_dict = {}

    for key in tasks:
        tasks_dict[key] = ctk.CTkCheckBox(frame, text = f"{key}", variable=var_dict[key], onvalue="on", offvalue="off")
        tasks_dict[key].place(x=15, y=(10+30*curListLen))
        curListLen += 1
    
    #apaga entrada de texto
    texto.delete(0, END)


def salvar():
    global tasks
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")

def load():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    curListLen = 0

    tasks_dict = {}


    for key in tasks:
        tasks_dict[key] = ctk.CTkCheckBox(frame, text = f"{key}", variable=var_dict[key], onvalue="on", offvalue="off")
        tasks_dict[key].place(x=15, y=(10+30*curListLen))
        curListLen += 1





janela = ctk.CTk()
janela.geometry("500x300")

janela.resizable(False,False)


frame = ctk.CTkFrame(janela, width=335, height=230)
frame.place(x=10, y=25)

texto = ctk.CTkEntry(janela, width=120, height=5)
texto.place(x=360, y=25)
texto.bind('<Return>', lambda event:adicionar())

add = ctk.CTkButton(janela, width=100, command=adicionar, text="Add Task", corner_radius=15)
add.place(x=370, y=75)

apagarB = ctk.CTkButton(janela, width=100, command=apague, text="Delete Task", corner_radius=15)
apagarB.place(x=370, y=125)

saveB = ctk.CTkButton(janela, width=100, command=salvar, text="Save", corner_radius=15)
saveB.place(x=370, y=175)

loadB = ctk.CTkButton(janela, width=100, command=load, text="Load", corner_radius=15)
loadB.place(x=370, y=225)


janela.mainloop()


