import threading
import PySimpleGUI as sg
from main import main as main_bot
import os
import sys

try:
    os.chdir(sys._MEIPASS)
except:
    pass

races = ["White", "Black", "Asian", "Indian", "Latino Hispanic", "Middle Eastern"]
checkboxes = [sg.Checkbox(race, default=True, key=race) for race in races]

main_tab = [
    [sg.Text("Tinder Bot", font=("Helvetica", 20))],
    [sg.Text("Number of Likes:"), sg.InputText(key="likes")],
    [sg.Text("Like Ratio (%):"), sg.InputText(key="ratio")],
    [sg.Button("Start Bot"), sg.Button("Exit")],
]

options_tab = [
    [sg.Checkbox("First Login", default=False, key="cookies"), sg.Checkbox("Headless", default=True, key="headless")],
    [sg.Text("Races", font=("Helvetica", 16))],
    checkboxes,
    [sg.Text("List of Names (separated with commas):", font=("Helvetica", 16))],
    [sg.InputText(key="names")],
]

layout = [
    [sg.TabGroup([[sg.Tab('Main', main_tab), sg.Tab('Options', options_tab)]])],
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

        if amount > 0 and 0 <= ratio <= 100:
            sg.popup_quick_message("Bot is running")
            thread = threading.Thread(target=main_bot, args=(amount, ratio, values["cookies"],
                                                             races_list, values["headless"], names))
            thread.start()
        else:
            sg.popup_error("Please enter valid values for likes and ratio.")

window.close()
