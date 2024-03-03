import threading
import PySimpleGUI as sg
from main import main as main_bot
from main import handle_first_login
import os
import sys

try:
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    os.chdir(sys._MEIPASS)
except:
    pass

races = ["White", "Black", "Asian", "Indian", "Latino Hispanic", "Middle Eastern"]
checkboxes = [sg.Checkbox(race, default=True, key=race) for race in races]

main_tab = [
    [sg.Text("Tinder Bot", font=("Helvetica", 20))],
    [sg.Text("Number of Likes:"), sg.InputText(key="likes")],
    [sg.Text("Like Ratio (%):"), sg.InputText(key="ratio")],
    [sg.Button("Start Bot"), sg.Button("Exit"), sg.Button("First Login")],
]

options_tab = [
    [sg.Checkbox("Headless", default=True, key="headless")],
    [sg.Text("Races", font=("Helvetica", 16))],
    checkboxes,
    [sg.Text("List of Names (separated with commas):", font=("Helvetica", 16))],
    [sg.InputText(key="names")],
    [sg.Text("List of Keywords in Bio (separated with commas):", font=("Helvetica", 16))],
    [sg.InputText(key="bio")],
    [sg.Text("List of Interests (separated with commas):", font=("Helvetica", 16))],
    [sg.InputText(key="interests")],
]

output = sys.stdout
tab_console = [[sg.Output(size=(72, 10), key="output")]]

layout = [
    [sg.TabGroup([[sg.Tab('Main', main_tab), sg.Tab('Options', options_tab), sg.Tab('Console', tab_console)]])],
]

window = sg.Window("Tinder Bot", layout, icon="./tinder-128.ico", resizable=True)

while True:
    event, values = window.read()

    races_list = [race.lower() for race in races if values[race]]

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    elif event == "Start Bot":
        amount: int = int(values["likes"]) if values["likes"].isdigit() else 0
        ratio: int = int(values["ratio"]) if values["ratio"].isdigit() else 0
        names: list = values["names"].split(",") if values["names"] else []
        bio_keywords: list = values["bio"].split(",") if values["bio"] else []
        interests: list = values["interests"].split(",") if values["interests"] else []

        if amount > 0 and 0 <= ratio <= 100:
            window["Start Bot"].update(disabled=True)

            sg.popup_quick_message("Bot is running")
            thread = threading.Thread(target=main_bot, args=(amount, ratio, races_list,
                                                             values["headless"], names, bio_keywords, interests))
            thread.start()

        else:
            sg.popup_error("Please enter valid values for likes and ratio.")

    elif event == "First Login":
        thread = threading.Thread(target=handle_first_login)
        thread.start()

window.close()
