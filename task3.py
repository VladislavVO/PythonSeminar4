# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

list_students=[]
with open ('task3students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if '5' in line:
            line = line.upper()             
        list_students.append(line.replace('\n',''))


with open('task3studentsnew.txt', 'w', encoding='utf-8') as file:
    for line in list_students:
        file.write(line+'\n')


