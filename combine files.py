import os


# подсчет строк в файле
def string_counter(file):
    count = 0
    with open(file, encoding='utf-8') as doc:
        for line in doc:
            count += 1
    return count


# составление словаря с данными вида {'имя_файла': [число строк в файле, содержание файла]}
def files_reader(data_dir_name):
    path_dir = os.path.join(os.getcwd(), data_dir_name)
    files = os.listdir(path_dir)
    data = dict()
    for file in files:
        with open(path_builder(file, data_dir_name), encoding='utf-8') as f:
            res = list()
            res.append(string_counter(path_builder(file, data_dir_name)))
            res.append(f.read())
        data[file] = res
    result = sort_data(data)
    return result


# построение актуального пути к файлу
def path_builder(name_file, data_dir_name):
    path_base = os.getcwd()
    file_path = os.path.join(path_base, data_dir_name, name_file)
    return file_path


# сортировка словаря с данными по возрастанию количества строк в файле
def sort_data(data):
    sorted_data = {}
    sorted_keys = sorted(data, key=data.get)
    for i in sorted_keys:
        sorted_data[i] = data[i]
    return sorted_data


# запись в файл в нужном формате
def file_writer(data):
    with open('result_file.txt', 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.writelines(f'{key}\n{value[0]}\n{value[1]}\n')


# главная функция, которая создает файл в данной директории, принимая название директории с исходными данными
# и записывает в него данные в нужном порядке
def main_func(directory_with_files):
    data_dict = files_reader(directory_with_files)
    file_writer(data_dict)
    print('File "result_file" was written!')

main_func('data')
