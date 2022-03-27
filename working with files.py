import os


# чтение исходных данных и создание словаря для задачи 2
def file_reader(file_path):
    with open(file_path, encoding='utf-8') as file:
        cook_book = dict()
        while True:
            dish = file.readline()
            cook_book[dish[:-1]] = []
            for i in range(int(file.readline().strip())):
                ingredients = file.readline().strip().split(sep=' | ')
                cook_book[dish[:-1]].append(
                    {'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]}
                )
            if file.readline() == '\n':
                continue
            else:
                break
    return cook_book


# построение актуального пути к файлу
def path_builder(name_file):
    path_base = os.getcwd()
    file_path = os.path.join(path_base, name_file)
    return file_path


# получение словаря необходимого формата с использованием результата задачи 1
def get_shop_list(dishes, person_count):
    shop_list = dict()
    cook_book = file_reader(path_builder('recipes.txt'))
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'], 'quantity': ingredient['quantity']*person_count
                }
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
    return shop_list


result = get_shop_list(['Запеченный картофель', 'Омлет'], 2)
for key, value in result.items():
    print(key, value, sep=': ')


