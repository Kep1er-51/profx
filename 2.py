# чтение таблицы с данными
f = open('astronaut_time.csv', encoding='UTF-8')
a = [x.strip().split(',') for x in f.readlines()[1:]]
f.close()

def sort_data(data):
    """Описание функции sort_data.
    сортирует список по 3 буквам из номера кают
	Описание аргументов:
	data – список, содержащий данные о номере часов; номере станции; номере каюты астронавта; времени остановки часов(ЧЧ:ММ:СС); кол-во часов простоя(целое число)


    :param data:
    :return:
    """
    alph = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
    for i in range(1, len(data)):
        name_now = data[i][2][3:]
        name_old = data[i - 1][2][3:]
        if alph.index(name_now[0]) < alph.index(name_old[0]):
            a[i], a[i - 1] = a[i - 1], a[i]
        elif alph.index(name_now[0]) == alph.index(name_old[0]):
            if alph.index(name_now[1]) < alph.index(name_old[1]):
                a[i], a[i - 1] = a[i - 1], a[i]
            elif alph.index(name_now[1]) < alph.index(name_old[1]):
                if alph.index(name_now[2]) < alph.index(name_old[2]):
                    a[i], a[i - 1] = a[i - 1], a[i]
    return data

def actual_time(data):
    """Описание функции actual_time.
    восстанавливает актуальное время
	Описание аргументов:
	data – список, содержащий данные о номере часов; номере станции; номере каюты астронавта; времени остановки часов(ЧЧ:ММ:СС); кол-во часов простоя(целое число)
    :param data: list
    :return: str
    """
    timeStop = list(map(int, str(data[-2]).split(':')))
    count = int(data[-1])
    timeNow = ':'.join(list(map(str, [(timeStop[0] + count) % 24, timeStop[1], timeStop[2]])))
    return f'На станции {data[1]} в каюте {data[2]} восстановлено время. Актуальное время: {timeNow}\n'


# создание таблицы с актуальными данными
f = open('new_time.txt', 'w', encoding='UTF-8')
for x in sort_data(a):
    f.write(actual_time(x))
f.close()
