# Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех
# вложенных файлов и директорий.

import os
import json
import csv
import pickle

__all__ = ['transform_and_save']


def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def transform_and_save(directory_path, output_folder):
    data = []

    for dirpath, dirnames, filenames in os.walk(directory_path):
        dir_size = get_directory_size(dirpath)
        relative_dirpath = os.path.relpath(dirpath, directory_path)

        if relative_dirpath == '.':
            relative_dirpath = ''

        data.append({
            'path': relative_dirpath,
            'type': 'directory',
            'size': dir_size
        })

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            relative_file_path = os.path.join(relative_dirpath, filename)

            data.append({
                'path': relative_file_path,
                'type': 'file',
                'size': file_size
            })

    # Сохранение данных в JSON
    json_file_path = os.path.join(output_folder, 'data.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    #  Сохранение данных в CSV
    csv_file_path = os.path.join(output_folder, 'data.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size'])
        csv_writer.writeheader()
        csv_writer.writerows(data)

    # Сохранение данных в Pickle
    pickle_file_path = os.path.join(output_folder, 'data.pickle')
    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == '__main__':
    input_directory = 'PycharmProjects'
    output_directory = 'PycharmProjects\dp_homework_8'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    transform_and_save(input_directory, output_directory)
