"""Doc."""

import modul_add_contact as mac
import modul_user_interface as mui
import modul_change_phone_number as mcpn
import modul_change_surname as mcs
import modul_delete_contact as mdc
import modul_view_all_contacts as mvac
import modul_export_in_file as meif
import modul_log_generate as lg


def user_choice():
    """Doc."""
    choice_num = mui.menu()
    lg.write_data('Основное меню ')
    if choice_num < 0 or choice_num > 7:
        lg.write_data(f'Ошибка ввода 001!: {choice_num}')
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        lg.write_data(
            f'Пользователь ввел команду: {choice_num}. '
            'Создать новую книгу или очистить существующую')
        mac.create_json()
    elif choice_num == 1:
        mac.add_to_json()
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Добавить новый контакт')
    elif choice_num == 2:
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Изменить номер телефона')
        mcpn.change_phone_number()
    elif choice_num == 3:
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Изменить фамилию')
        mcs.change_surname()
    elif choice_num == 4:
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Удалить контакт')
        mdc.delete_contact()
    elif choice_num == 5:
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Показать все контакты')
        mvac.view_all_contacts()
    elif choice_num == 6:
        lg.write_data(f'Пользователь ввел команду: {choice_num}. '
                      'Экспортировать контакты в файл')
        meif.export_txt()
    elif choice_num == 7:
        print('\nДо новых встреч!')
        lg.write_data(f'Пользователь ввел команду: {choice_num}. Выход')
        exit()
