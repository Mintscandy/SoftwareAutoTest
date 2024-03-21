import csv


def readcsv(filename):
    with open(filename, 'r') as f:
        i = 0
        res = []
        for row in csv.reader(f):
            if i != 1:
                res.append(row)
            i = i + 1
    return res
