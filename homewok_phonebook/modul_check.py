"""Doc."""
import modul_log_generate as lg


def digit_check():
    """Doc."""
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        lg.write_data('Ошибка ввода 002!')
        print('Это должно быть число\n')
        return digit_check()
