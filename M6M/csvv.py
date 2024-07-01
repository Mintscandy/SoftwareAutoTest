import csv
def read_csv(data):
    res = []
    with open(data,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            res.append(row)
    return res
