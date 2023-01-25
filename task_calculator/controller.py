# Модуль объединяющий работу всех модулей кроме main
"""Doc."""
import calculation as calc
import user_interface as ui
import log_generate as lg


def start_nums():
    """Doc."""
    user_nums, nums = ui.get_nums()  # Получение данных от пользователя
    # Запись данных которые ввел пользователь в лог
    lg.write_data(f'Ввод пользователя: {user_nums}')
    result = calc.get_result(nums)  # Решаем пример
    lg.write_data('Итоговый результат: ' + user_nums +
                  ' = ' + result)  # Запись результата в лог
    # Добавляем пустую строку-разделитель в логе между разными примерами
    lg.write_data('')
    # Вывод результата пользователю в терминал
    ui.print_user(user_nums, result)
    print('Содержимое лог-файла:')
    lg.read_log()  # Вывод в консоль содержимого лог-файла
