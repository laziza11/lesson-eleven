students = {}
classes = {}
opened_classes = [i for i in range(1, 11)]
closed_classes = []

# Adding a student
def add_student(name, class_number):
    students[name] = class_number
    if class_number in opened_classes:
        opened_classes.remove(class_number)
        closed_classes.append(class_number)

# Deleting a student
def del_student(name):
    if name in students:
        class_number = students[name]
        closed_classes.remove(class_number)
        opened_classes.append(class_number)
        del students[name]
    else:
        print("Такого студента нет!")


def show_students():
    return students

# Viewing available classes
def show_classes():
    return opened_classes

while True:
    choice = input('Введите действие (добавить, выселить, показать, классы, выход): ')

    if choice.lower() == 'добавить':
        st_name = input('Имя студента: ')
        print(f'Доступные классы: {opened_classes}')
        st_class = int(input('Выберите номер класса (от 1 до 10): '))
        if st_class in opened_classes:
            add_student(st_name, st_class)
            print(f'Добавлен студент: {st_name}, класс: {st_class}')
        else:
            print('Класс недоступен!')

    elif choice.lower() == 'выселить':
        st_name = input('Имя студента: ')
        del_student(st_name)
        print(f'Текущий список студентов: {show_students()}')

    elif choice.lower() == 'показать':
        print('Список студентов:', show_students())

    elif choice.lower() == 'классы':
        print('Открытые классы:', show_classes())

    elif choice.lower() == 'выход':
        print('Выход из системы.')
        break
    else:
        print('Ошибка, попробуйте снова!')




