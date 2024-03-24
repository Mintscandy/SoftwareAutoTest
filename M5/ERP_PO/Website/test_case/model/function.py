import csv
from selenium import webdriver


def inser_png(driver, name):
    path = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M5\ERP_PO\Website\test_report\screenshot\\'
    driver.get_screenshot_as_file(path + name)


def get_csv_line(filename, line):
    res = []
    i = 0
    with open(filename, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res[line]


if __name__ == '__main__':
    print(get_csv_line(r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M5\ERP_PO\Website\test_data\test_csv.csv', 1))
