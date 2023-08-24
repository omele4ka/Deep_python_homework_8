# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle

__all__ = ['reader_csv']


def reader_csv(csv_file_name: str) -> bytes:
    with open(csv_file_name, 'r', encoding='utf-8') as f:
        reader = f.read()
        return pickle.dumps(reader)

if __name__ == '__main__':
    reader_csv('users_1users_1.csv')