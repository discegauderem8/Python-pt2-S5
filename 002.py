import os

def file_info (path):
    filename = os.path.basename(path)
    split_name = filename.split(".")

    return (split_name[0], split_name[1], filename)


path = input("введите путь до файла: ")

print(file_info(path))