from selenium import webdriver
import csv


def inser_img(driver: webdriver.Chrome, fn):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M10\ERP_PO\Website\test_report\screenshot\\"
    driver.get_screenshot_as_file(path + fn)


def get_csv_line(d, line):
    res = []
    i = 0
    with open(d, "r", encoding="utf-8") as f:
        for r in csv.reader(f):
            if i != 0:
                res.append(r)
            i = i + 1
    return res[line]
