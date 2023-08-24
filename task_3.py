# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV
import json

__all__ = ['json_to_csv']
def json_to_csv(src_file: str = 'users.json',
                out_file: str = 'users.csv'):
    with open(src_file, 'r') as src:
        data = json.load(src)

    with open(out_file, 'w') as res:
        res.write('id,level,name')
        for level, users_lst in data.items():
            for user in users_lst:
                res.write(f'\n{user["id"]},{level},{user["name"]}')

if __name__== '__main__':
    json_to_csv('users.json', 'users.csv')