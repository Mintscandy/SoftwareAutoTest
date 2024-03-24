from selenium import webdriver
import csv


def inser_img(driver: webdriver.Chrome, name):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4\ERP_PO\Website\test_report\screenshot\\"
    driver.get_screenshot_as_file(path + name)


def get_csv_line(path, line):
    i = 0
    res = []
    with open(path, 'r', encoding='utf-8') as f:
        for row in csv.reader(f):
            if i != 0:
                res.append(row)
            i = i + 1
    return res[line]


if __name__ == '__main__':
    print(get_csv_line(r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4\ERP_PO\Website\test_data\testdata.csv', 0))
