"""Doc."""
import json
import modul_controller as mc
path_to_db = 'db.json'


def export_txt():
    """Doc."""
    # name = input('Введите имя или фамилию контакта, для экспорта в файл:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            #    if name == data[i]['Name'] or name == data[i]['Surname']:

            with open('Export_contact.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                    data[i]['Surname']) + ' ' + "".join(data[i]['Phone number'
                                                                ]) + ' ' + ""
                    .join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    mc.user_choice()
