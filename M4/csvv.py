import csv


def readfile(filename):
    res = []
    i = 0
    with open(filename, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res


if __name__ == '__main__':
    print(readfile("testdata.csv"))
