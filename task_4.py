# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции

import json


json.__all__ == ['csv_to_json']
def csv_to_json(src_file: str = 'users.csv',
                out_file: str = 'users_1.json',):
    with open(src_file, 'r') as src:
        data = list(map(lambda x: x.split(','),
                        src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()

        user_id = data[i][0]
        name = data[i][2]
        data[i].append(hash(user_id + name))

    data = data[1::]
    print(data)

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data]

    with open(out_file, 'w') as res:
        json.dump(data, res, indent=4)

if __name__ == 'main':
    csv_to_json('users.csv', 'users_1.json')
