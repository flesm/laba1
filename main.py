def sum_even_digits(x):
    sum1 = 0
    x = [int(i) for i in str(x).replace('-', '')]
    for i in x:
        sum1 += i if i % 2 == 0 else 0

    print(f"Сумма чётных цифр числа равна: {sum1}")


def count_letters(s):
    a, b = 0, 0
    s_copy = s[:]

    a_list, b_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u'] \
        , ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
                         , 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
           'x', 'y', 'z']

    for i in s:
        if i.lower() in a_list:
            a += 1
        elif i.lower() in b_list:
            b += 1

    if a != b:
        print(f"Количество гласных букв: {a}.\nКоличество согласных букв: {b}.")
    elif a == b == 0:
        print(f"Вы не ввели хотя бы одну гасную или согласную букву.")
    else:
        s = "".join([i for i in s if i.lower() in a_list])
        print(f"Количество гласных и согласных букв слова совпали.\nВсе гласные буквы слова: {s}")

    list_to_replace = [',', '.', '!', '?']
    for i in list_to_replace:
        s_copy.replace(i, '')

    print(f"Количество слов в тексте: {len(s_copy.split())}")



def list_operations(lst):
    for i in range(len(lst)):
        sum1 = 0
        if type(lst[i]) == int:
            if lst[i] % 2 == 0:
                for j in str(lst[i]):
                    sum1 += int(j)
                print(f"Сумма цифр числа {lst[i]} равна {sum1}")
            else:
                lst[i] = 1
    print(f"Обновлённый список: {lst}")


def min_elems_dict(my_dict, num=3):
    new_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    print(f"{num} ключа со словаря {my_dict} с самымыми маленькими значениеми: {list(new_dict.keys())[:num]}")


def max_elem_tuple(my_tuple):
    max_el = my_tuple[0]
    index = 0
    for i in range(1, len(my_tuple)):
        if type(my_tuple[i]) != str and my_tuple[i] > max_el:
            index = i

    print(f"Индекс максимального элемента кортежа {my_tuple} равен {index}")


while True:
    print("\n\nМеню заданий:\n"
          "1 - Задание на суммирование чётных цифр числа.\n"
          "2 - Задание на гласные и согласные буквы.\n"
          "3 - Задание на четные и нечетные значения списка\n"
          "4 - Задание со словарём\n"
          '''5 - Программа "Магазин игрушек"\n'''
          "6 - Задание с кортежем\n"
          "Любое другое число - Выход из программы.\n")

    while True:
        try:
            var = int(input("Введите число для выбора задания: "))
            break
        except ValueError:
            print("Введено не число!\nПопробуйте еще раз.")

    if var == 1:
        while True:
            try:
                x = int(input("\n\nВведите некоторое число: "))
                break
            except ValueError:
                print("Введено не число!\nПопробуйте еще раз.")
        sum_even_digits(x)

    elif var == 2:
        s = input("Введите некоторую строку: ")
        count_letters(s)

    elif var == 3:
        lst = [12, 511, 'Python', 311, 122, 'love']
        list_operations(lst)

    elif var == 4:
        my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
        min_elems_dict(my_dict)

    elif var == 5:
        while True:
            toys_dict = {
                "мяч": ["резина", 500, 10],
                "машинка": ["металл", 1200, 7],
                "пазл": ["картон", 600, 20]
            }

            print("\n\nМеню Магазина игрушек:\n"
                  "1 - Просмотр описания: название – описание.\n"
                  "2 - Просмотр цены: название – цена.\n"
                  "3 - Просмотр количества: название – количество\n"
                  "4 - Всю информацию.\n"
                  "5 - Покупка.\n"
                  "Любое другое - До свидания.\n")

            while True:
                try:
                    n = int(input("Введите число для навигации по магазину: "))
                    break
                except ValueError:
                    print("Введено не число!\nПопробуйте еще раз.")

            if n == 1:
                for key, info in toys_dict.items():
                    print(f"Игрушка {key} состоит из {info[0]}.")

            elif n == 2:
                for key, info in toys_dict.items():
                    print(f"Игрушка {key} стоит {info[1]} BYN.")

            elif n == 3:
                for key, info in toys_dict.items():
                    print(f"Колличество игрушки {key}: {info[2]} штук.")

            elif n == 4:
                for key, info in toys_dict.items():
                    print(f"Игрушка {key}: сделана из {info[0]}, стоит {info[1]}, количество {info[2]}.")

            elif n == 5:
                while True:
                    t = input("Введите название игрушки которую хотите купить: ").lower()
                    if t not in toys_dict.keys():
                        print("Такой игрушки в магазине нет.")
                        continue
                    break

                while True:
                    try:
                        num = int(input("Введите количество данной игрушки, которое вы хотите купить: "))
                        if num < 1 or num > toys_dict[t][2]:
                            print("Вы не можете купить такое количество игрушек.\nПопробуйте еще раз.")
                            continue
                        break
                    except ValueError:
                        print("Введено не число!\nПопробуйте еще раз.")

                toys_dict[t][2] = toys_dict[t][2] - num
                print(f"Цена за товары составит: {toys_dict[t][1] * num}")
                print(f"Осталось {toys_dict[t][2]} штук игрушки {t}")

            else:
                break

    elif var == 6:
        my_tuple = (1, 4, 0, -10, 100, 99, 'Python', 'c++', 101, 'me', 103)
        max_elem_tuple(my_tuple)

    else:
        print("До свидания!")
        exit()
