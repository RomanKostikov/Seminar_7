"""Doc."""
import json
import modul_controller


def create_json():
    """Doc."""
    json_data = []
    with open('db.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    modul_controller.user_choice()


def add_to_json():
    """Doc."""
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    json_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w", encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    modul_controller.user_choice()
