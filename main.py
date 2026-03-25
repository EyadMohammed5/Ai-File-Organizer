from classify import classify, init
from readPDF import readPDF
import gui
import shutil
import os
import pymsgbox


# Folders That Files Will Be Sorted To
Folders = gui.directories
Folders_name = gui.folder_names

# Files To Be Put Into
Files = gui.files

if not (Folders_name and Folders):
    pymsgbox.alert("Please choose folders to store files")
    exit(0)

elif not Files:
    pymsgbox.alert("Please choose files to be put into folders")
    exit(0)

Folders_Paths = {}
# Copilot Told Me To Use range() Here
for i in range(len(Folders)):
    Folders_Paths[Folders_name[i]] = Folders[i]
print(Folders_Paths)

# Text Extracted From All Selected Files
files_contents = []

for file in Files:
    # Extract The PDF Contents
    content = readPDF(file)
    if content:
        # Add Content To files_contents
        files_contents.append(content)

# Dictionary Of File Path, Folders
fileslabelled = {}
print("User is using: " + str(gui.selected.get()))

index = 0
# Initialize The Chosen Bot
init(gui.selected.get())

for content in files_contents:
    if content:
        # Ai Classifies File Contents To Folders Name
        label = classify(content, Folders_name)
        # Store Result In Dictionary Of (file path -> folder path)
        fileslabelled[Files[index]] = Folders_Paths[label['labels'][0]]
        index += 1

print(fileslabelled)


if fileslabelled:
    # Got this line from copilot
    for file_path, destination in fileslabelled.items():
        try:
            shutil.move(file_path, destination)
        except shutil.Error:
            print("already there")
            continue
        except:
            pymsgbox.alert("An error have happened in transfering " + file_path + " to: " + destination)
            continue

        print(f"moved: {file_path} to: {destination}")
    pymsgbox.alert("Successfully Organized (AI can make mistakes in organizing so check Your files)", "Successful!")
else:
    pymsgbox.alert("An Error has occured")
