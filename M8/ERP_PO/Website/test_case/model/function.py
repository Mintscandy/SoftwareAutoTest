from selenium import webdriver
import csv


def inser_img(driver: webdriver.Chrome, filename):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M8\ERP_PO\Website\test_report\screenshot\\"
    driver.get_screenshot_as_file(path + filename)


def get_csv_line(path, line):
    res = []
    i = 0
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res[line]
