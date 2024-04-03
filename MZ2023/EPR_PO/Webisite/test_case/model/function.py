from selenium import webdriver
import csv


def inser_img(driver: webdriver.Chrome, name):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\MZ2023\EPR_PO\Webisite\test_report\screenshot\\" + name
    driver.get_screenshot_as_file(path)


def get_csv_line(data, line):
    res = []
    i = 0
    with open(data, "r", encoding="utf-8") as f:
        for r in csv.reader(f):
            if i != 0:
                res.append(r)
            i = i + 1
    return res[line]
