"""Doc."""
import json
import modul_controller as mc

path_to_db = 'db.json'


def change_surname():
    """Doc."""
    name = input(
        'Введите имя или фамилию контакта, фамилию которого будем менять:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Surname'] = input('Новая фамилия: ')
            if name not in data:
                print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nФамилия успешно изменена!\n')
    mc.user_choice()
