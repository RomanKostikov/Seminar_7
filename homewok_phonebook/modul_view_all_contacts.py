"""Doc."""

import json
import modul_controller as mc


path_to_db = 'db.json'


def view_all_contacts():
    """Doc."""
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    mc.user_choice()
