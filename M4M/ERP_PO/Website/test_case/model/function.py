import csv
from selenium import webdriver

def inser_img(driver:webdriver.Chrome,img_name):
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4M\ERP_PO\Website\test_report\screenshot\\" + img_name
    driver.get_screenshot_as_file(path)

def get_csv_line(data,line):
    res = []
    with open(data, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for r in reader:
            res.append(r)
    return res[line]
