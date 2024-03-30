data = open('astronaut_time.csv', encoding='UTF-8')
data = [x.strip().split(',') for x in data.readlines()[1:]]
f = open('station_max_downtime.csv', 'w', encoding='UTF-8')
new_data = {}
for x in data:
    if x[1] not in new_data:
        new_data[x[1]] = x[-1]
    else:
        new_data[x[1]]+=x[-1]

new_data = list(new_data.items())
for x in new_data:
    if x[1]=='9':
        f.write(' '.join(x)+'\n')
