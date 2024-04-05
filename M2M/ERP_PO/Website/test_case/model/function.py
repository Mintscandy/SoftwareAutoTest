from selenium import webdriver
import time
import csv


def inser_img(driver: webdriver.Chrome, filename):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M2M\ERP_PO\Website\test_report\screenshot\\" + filename
    driver.get_screenshot_as_file(path)


def get_csv_line(data, line):
    res = []
    with open(data, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for r in reader:
            res.append(r)
    return res[line]
