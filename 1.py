# чтение таблицы с данными
f = open('astronaut_time.csv', encoding='UTF-8')
a = [x.strip().split(',') for x in f.readlines()[1:]]
f.close()
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
for x in a:
    f.write(actual_time(x))


