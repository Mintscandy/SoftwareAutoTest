import csv


def readfile(filename):
    res = []
    i = 0
    with open(filename, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)

    return res
