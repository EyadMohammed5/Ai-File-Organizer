# Ai PDF Organizer
#### Video Demo: https://youtu.be/p0brYt9Wlw4
#### Description: 
## General Description
### Ai PDF Organizer is a file organizer that reads the pdfs given by the user into text then uses that text with an Ai (Transformers library from hugging face) and the user has the ability to choose his model to use either he want faster Ai or more accurate Ai or a balance between both. 

## How the program works (simplified)  
 ### The program works as mentioned above by reading PDF files into text using the readPDF.py then returns the text to main where main uses that text with classify.py which uses a model (the user chooses which model) then we get a dictionary of file paths and folder paths at the end the program uses shutil library to move each file from the dictionary to it's corresponding folder.

## Gui
 ### In gui.py user gets a gui interface to interact with the program in it he chooses which files he wants to be organized then he chooses which folders he want these files to go in (in choosing files user may choose multiple files at once but when choosing folders user must individually choose a folder submit it then choose another) the gui also has two text labels one to display the chosen files and other for chosen folders also gui.py has two buttons at the end one to clear all what has been chosen other for confirming. Upon confirming entered data reaches main.py to start the program. Also in the gui top drop down menu is so the user chooses his model based on what he exactly needs from speed and accuracy.
 
## Classify.py and files actually being moved
 ### In classify.py the chosen model is run in the init function so it initializes once. If the files are moved to folder that Ai figured out you get a success message box but if a file is already in the folder Ai chooses it prints already there and nothing appears to user but if any other errors happen user gets a message box that the   specific file failed to move to the specific folder and in both cases the program continues to the other files.

## program's accuracy and needed libraries
 ### The program may not be that accurate since we are using a local Ai in all the models even accurate one the accuracy may not be as user expected sadly so user is asked to check if file is in correct folders. First run of the program may take time since it needs to download the Ai locally first time but when running it after first time it works faster. I tried to fix as many bugs as i found i think user mistakes are all taken care of. to run this program user needs to download pytorch and hugging face transformers and some libraries like shutil pymsgbox os tkinter ttkbootstrap and Ppypdf. Personally to keep testing and developing this program i used an anaconda environment. I think that's all the details i could think of so Thanks!