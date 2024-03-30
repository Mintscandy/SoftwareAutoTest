from selenium import webdriver
import csv


def inser_img(driver: webdriver.Chrome, name):
    path = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M7\ERP_PO\Website\test_report\screenshot\\' + name
    driver.get_screenshot_as_file(path)


def read_csv_line(fn):
    res = []
    i = 0
    with open(fn, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res


if __name__ == '__main__':
    read_csv_line("/M7/ERP_PO/Website/test_data/test_csv.csv")
