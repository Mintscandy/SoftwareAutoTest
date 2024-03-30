import csv


def read(file):
    res = []
    i = 0
    with open(file, 'r', encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res
