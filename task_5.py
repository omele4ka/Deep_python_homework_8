# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов


import os
import pickle



__all__ = ['search_files']
def search_files(ext: str = '.json', dir_: str = '.') -> None:
    files = (file for file in os.listdir(dir_) if file.endswith(ext))

    for file in files:
        name, _ = os.path.splitext(file)
        with (
            open(file, 'r') as r_file,
            open(name + '.pickle', 'wb') as w_file
        ):
            data = r_file.read()
            pickle.dump(file=w_file, obj=data)

if __name__ == '__main__':
    search_files()

