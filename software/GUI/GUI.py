#GUI.py
#THIS WAS A TUTORIAL FROM https://realpython.com/pysimplegui-python/#:~:text=Creating%20a%20simple%20graphical%20user,and%20your%20users%20will%20enjoy! 
#  
# img_viewer.py

import PySimpleGUI as sg
import PIL
from PIL import Image
import io
import base64
import os
import os.path

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

def display_image_window(filename):
   try:
        layout = [[sg.Image(data=convert_to_bytes(filename, IMAGE_SIZE), enable_events=True)]]
      e,v = sg.Window(filename, layout, modal=True, element_padding=(0,0), margins=(0,0)).read(close=True)
    except Exception as e:
      print(f'** Display image error **', e)
        return


# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
            display_image_window(filename)

        except:
            pass

window.close()