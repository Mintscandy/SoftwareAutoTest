import csv


def read_csv(data):
    res = []
    with open(data, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for r in reader:
            res.append(r)
    return res
