import os
def add_new_user(name, phone, filename):
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
        lins_count = len(wrtbl.readlines())
        wrtbl.write(f"{lins_count + 1};{name};{phone}\n")

def read_all(filename: str) ->str:
    with open(filename, 'r', encoding='utf-8') as data:
        resolt = data.read()
    return resolt

def search_user(data: str, filename: str) ->str:
    with open(filename, 'r', encoding='utf-8') as content:
        text = content.readlines()
        res = [item for item in text if data.lower() in item.lower()]
    return ''.join(res) if res else 'Вхождений не найдено'

def copy(filename: str):
    with open(filename, 'r', encoding='utf-8') as fr, open(write_file, 'a', encoding='utf-8') as fw:
        for i in fr:
            identify = i.split(";")[0]
            if identify == id:
                fw.write(i)

def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write("")
INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск  
4 - копирование контакта в другой файл
"""
DATASOURCE = 'phone.txt'
write_file = 'newphone.txt'
check_directory(DATASOURCE)
while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input()
        phone = input()
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        search = input()
        print(search_user(search, DATASOURCE))
    elif mode == 4:
        id = input()
        copy(DATASOURCE)