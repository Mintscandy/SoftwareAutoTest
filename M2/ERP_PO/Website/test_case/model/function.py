import os
import csv
from selenium import webdriver


def inser_img(driver, filename):
    fp = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M2/ERP_PO/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(fp)


def get_csv_file(filename, line):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader, 0):
            if index == line:
                return row


if __name__ == '__main__':
    print(get_csv_file('/Users/zhudichuan/PycharmProjects/2024ERP_TR/M2/ERP_PO/Website/test_data/test_csv.csv.csv', 1))
