from selenium import webdriver
import csv

def inser_img(driver:webdriver.Chrome,name):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M6M\ERP_PO\Website\test_report\screenshot\\" +name
    driver.get_screenshot_as_file(path)
def get_csv_line(data,line):
    res = []
    with open(data, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            res.append(row)
    return res[line]