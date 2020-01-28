import csv
sum = 0

with open('stocks.csv', newline='') as csvfile:
    stockreader = csv.reader(filter(lambda line: line[0] != '#', csvfile))
    for row in stockreader:
        if row:
            if row[5] == 'True':
                sum += float(row[1])*float(row[2])
            else:
                sum -= float(row[1])*float(row[2])


print(sum)