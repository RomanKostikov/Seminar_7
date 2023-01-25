# Модуль записи логов
"""Doc."""
from datetime import datetime as dt


def write_data(data):
    """Doc."""
    time = dt.now().strftime('%H:%M')
    data = ''.join(map(str, data))
    with open('log.xml', 'a', encoding='utf=8') as file:
        file.write('{}; controller; {}\n'
                   .format(time, data))
