import csv
from selenium import webdriver


def inser_img(driver: webdriver.Chrome, name):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M3M\ERP_PO\Website\test_report\screenshot\\"

    driver.get_screenshot_as_file(path + name)


def get_csv_line(data, line):
    res = []
    with open(data, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for r in reader:
            res.append(r)
    return res[line]
