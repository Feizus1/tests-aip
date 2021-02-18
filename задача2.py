School = {}
for i in range(5):
    School.update({input(f'Название класса №{i + 1}: '): int(input(f'Количество учеников класса №{i + 1}: '))})
print(School)
ClassName = input('Введите название класса: ')
if ClassName in School:
    print(f'Количество учеников в классе {ClassName}: {School[ClassName]}')
else:
    print('Такого класса нет')
for i in range(3):
    School.update({input(f'Название изменяемого класса {i + 1}: '): int(input(f'Количество учеников изменяемого класса {i + 1}: '))})
print(School)
for i in range(2):
    School.update({input(f'Название нового класса {i + 1}: '): int(input(f'Количество учеников нового класса {i + 1}: '))})
print(School)
del School[input(f'Название удаляемого класса: ')]
print(School)
