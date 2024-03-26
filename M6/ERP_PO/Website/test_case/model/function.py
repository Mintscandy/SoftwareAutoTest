import csv
from time import sleep
from selenium import webdriver
import os


def inser_img(driver: webdriver.Chrome, filename):
    path = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M6\ERP_PO\Website\test_report\screenshot\\'

    print(os.path.join(path, filename))
    driver.get_screenshot_as_file(os.path.join(path + filename))


def read_csv(filename):
    i = 0
    res = []
    with open(filename, 'r', encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res
