import csv


def rf(filename):
    res = []
    i = 0
    with open(filename) as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res
