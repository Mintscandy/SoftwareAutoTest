from selenium import webdriver
import time
import csv


def inser_img(driver: webdriver.Chrome, filename):
    path = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M3/ERP_PO/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(path)


def get_csv_data(file, line):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader, 0):
            if index == line:
                return row


if __name__ == "__main__":
    fn = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M3/ERP_PO/Website/test_data/test_csv.csv.csv'
    print(get_csv_data(fn, 1))
