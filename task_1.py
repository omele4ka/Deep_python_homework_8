# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами
# и произведением чисел.
# Напишите функцию, которая создаёт из созданного
# ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


__all__ = ['txt_json']
def txt_json(src_file: str = 'text.txt',
             out_file: str = 'text.json'):
    with open(src_file, 'r') as file:
        names = dict(map(lambda x: tuple(x.split()),
                         file.read().split('\n')))

    with open(out_file, 'w') as file:
        json.dump(names, file, indent=4)

if __name__ == '__main__':
    txt_json('text.txt', 'text.json')
