def plural_form(quantity, name1, name2, name3):
    '''
    Функция plural_form служит для согласования окончаний существительных в зависимости от переданного числа. Функция должна принимает 4 параметра:
    :param quantity: - количество объектов
    :param name1: - форма слова 1
    :param name2: - форма слова 2
    :param name3: - форма слова 3
    '''

    name_modifier = quantity % 100

    if name_modifier >=5 and name_modifier <= 20:
        answer = name3

    else:
        name_modifier %= 10

        if name_modifier == 1:
            answer = name1

        elif name_modifier >= 2 and name_modifier <= 4:
            answer = name2

        else:
            answer = name3

    return f'{quantity} {answer}'








# print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
# print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
# print(plural_form(11, 'студент', 'студента', 'студентов'))
# print(plural_form(15, 'студент', 'студента', 'студентов'))
# print(plural_form(3, 'студент', 'студента', 'студентов'))
# print(plural_form(21, 'студент', 'студента', 'студентов'))
# print(plural_form(543, 'студент', 'студента', 'студентов'))
# print(plural_form(148, 'яблоко', 'яблока', 'яблок'))