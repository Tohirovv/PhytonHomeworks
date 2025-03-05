import csv
column = ["Name","Subject","Grade"]
data = [
    ["Alice","Math",85],
    ["Bob","Science",78],
    ["Carol","Math",92],
    ["Dave","History",74]
]
with open("grades.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(column)
    writer.writerows(data)

with open('grades.csv', 'rt') as file:
    reader = csv.reader(file, delimiter=',')
    columns1 = next(reader)
    rows = []
    dictionary1 = dict()
    count = dict()
    for row in reader:
        rows.append(row)
        if row[1] in dictionary1.keys():
            dictionary1[row[1]] += float(row[2])
            count[row[1]] += 1
        else:
            dictionary1[row[1]] = float(row[2])
            count[row[1]] = 1

    list1 = [["Subject","Average Grade"]]
    for k, v in dictionary1.items():
        list1.append([k, v/count[k]])


    with open("average_grades.csv","w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list1)