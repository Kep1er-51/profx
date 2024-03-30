# чтение таблицы с данными
data = [x.strip().split(',') for x in open('astronaut_time.csv', encoding='UTF-8').readlines()[1:]]

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
    return f'На станции {data[1]} восстановлено время (время остановки: {data[-2]}). Актуальное время: {timeNow}'


while True:
    request = input('введи номер станции: ')
    if request == 'stop':
        break
    else:
        for i in range(len(data)):
            if data[i][1] == request:
                print(actual_time(data[i]))
        else:
            print('На этой станции все хорошо')



