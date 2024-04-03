import csv
import re


def readcsv(filename):
    res = []
    i = 0
    with open(filename,"r",encoding="utf-8") as f:
        for r in csv.reader(f):
            if i!=0:
                res.append(r)
            i = i + 1
    return res
