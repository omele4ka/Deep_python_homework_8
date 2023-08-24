# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json


__all__ = ['add_usrs_json']
def add_usrs_json(filename: str = 'users.json'):
    while True:
        try:
            with open(filename, 'r') as src:
                data = json.load(src)
        except FileNotFoundError:
            data = {str(i): [] for i in range(1, 8)}

        name = input('Ввведите имя: ')
        user_id = input('Введите ваш id: ')
        level = input('Введите ваш уровень доступа: ')
        data[level].append({'name': name, 'id': user_id})

        with open(filename, 'w') as res:
            json.dump(data, res, indent=4)

if __name__ == 'main':
    add_usrs_json('users.json')
