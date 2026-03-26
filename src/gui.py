import os
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
import ttkbootstrap.constants

root = ttk.Window(themename="darkly")
# Window Properties
# Two lines from chat gpt
root.resizable(False, False)
root.attributes("-fullscreen", False)
root.geometry("500x300")
root.title("Ai File Organizer")

# Labels
label_files = ttk.Label(root, text="Files: ", bootstyle="inverse-warning", font=("Ariel", 16, "bold"))
label_Folders = ttk.Label(root, text="Folders: ", bootstyle="inverse-warning", font=("Ariel", 16, "bold"))

# To Put The Values Into The Labels
files = []
directories = []

# Open File Explorer To Choose Files And Folders
def Browse(type):
    global files
    if type == "file":
        # Open File Explorers And Allow Multiple PDF Files
        item = filedialog.askopenfilenames(title="Select PDFs", filetypes=[("PDF Files", "*.pdf")])
        if item:
            print(item)
            for file in item:
                files.append(file)
            # Change label Contents
            label_files.config(text=Display("file"))
    else:
        # Open File Explorers To Choose Files
        item = filedialog.askdirectory()
        if item:
            for folder in directories:
                if item == folder:
                    return
            directories.append(item)
            # Add Folders That Are Chosen To The label
            label_Folders.config(text=Display("folder"))

# Display Selected Items On Labels
def Display(type):
    folder_names = ""
    file_names = ""
    if type == "file":
        file_names = "Files: "
        for file in files:
            file_names = file_names + "   " + os.path.basename(file)
        return file_names
    else: 
        folder_names = "Folders: "
        for folder in directories:
            folder_names = folder_names + "   " + os.path.basename(folder)
        return folder_names    

# Clear Chosen Files And Folders To Choose New Ones
def clear():
    # Line Added By copilot
    global files, directories
    files = ""
    directories = []
    label_Folders.config(text="Folders: ")
    label_files.config(text="Files: ")  

folder_names = []
file_names = []

# Confirm And Send Data To Main
def confirm():
    for file in files:
        name_file = os.path.basename(file)
        if name_file not in file_names:
            file_names.append(name_file)
        else:
            return

    for folder in directories:
        folder_name = os.path.basename(folder)
        if folder_name not in folder_names:
            folder_names.append(folder_name)
        else:
            return
    root.destroy()

# To Prevent Main.py From Running After Program Is Closed
def close():
    exit(0)
root.protocol("WM_DELETE_WINDOW", close)

# Text for Options Available On Select Menu
models = ["xlm-roberta-large-xnli (accuracy)", "mDeBERTa-v3-base-mnli-xnli (balance)", "multilingual-MiniLMv2-L6-mnli-xnli (speed)"]
# Selected Option
selected = tk.StringVar(root)
# Default
selected.set("mDeBERTa-v3-base-mnli-xnli (balance)")
# *models is from stack overflow
bots = tk.OptionMenu(root, selected, *models)
bots.pack()

# Buttons On Window
# Lamda Added From Copilot
button_File = ttk.Button(root, text="Browse files", command=lambda: Browse("file"), bootstyle="LIGHT OUTLINE")
button_Folder = ttk.Button(root, text="Browse Folders", command=lambda: Browse("Folder"), bootstyle="LIGHT OUTLINE")
button_clear = ttk.Button(root, text="Clear", command=clear,bootstyle="DANGER")
button_confirm = ttk.Button(root, text="Confirm", command=confirm,bootstyle="SUCCESS")

button_File.pack(side="top", pady=20)
button_Folder.pack(side="top", pady=(0,10))

label_Folders.pack(padx=(10,0))
label_files.pack(padx=(10,0))

button_confirm.pack(side="left", padx=(160, 50))
button_clear.pack(side="right", padx=(0, 160))

root.mainloop()

print(folder_names)
print(file_names)
print(files)
print(directories)
