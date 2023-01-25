"""Doc."""
import json
import modul_controller as mc


path_to_db = 'db.json'


def change_phone_number():
    """Doc."""
    name = input('Введите имя или фамилию контакта, чей номер будем менять:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый телефон: ')
            if name not in data:
                print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер успешно изменён!\n')
    mc.user_choice()
