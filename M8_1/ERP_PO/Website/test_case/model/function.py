from selenium import webdriver
import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(sender, receiver, filename):
    local_host = 'smtp.qq.com'
    username = 'candysly@qq.com'
    password = 'vvmhelpyyglrdhca'
    smtp = smtplib.SMTP_SSL(local_host, 465)
    smtp.helo(local_host)
    smtp.ehlo(local_host)
    smtp.login(username, password)

    f = open(filename, 'rb')
    mail_content = f.read()
    f.close()

    msg = MIMEText(mail_content,'html','utf-8')
    msg["Subject"] = Header("自动化测试报告",'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()



def inser_img(driver: webdriver.Chrome, filename):
    # 这个地方找了一个“/”，没有放进目录里面，自己注意哦
    # 这个我是真的没注意 啊哈哈哈哈 所以我好多错误图片都不保存 哈哈哈 我看你左边目录screenshot里面没看到图片我就知道了
    # 谢谢欣欣
    driver.get_screenshot_as_file(r'M8_1/ERP_PO/Website/test_report/screenshot//' + filename)


def read_csv_line(datafile, line):
    result = []
    with open(datafile, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            result.append(row)
    return result[line]

if __name__ == '__main__':
    send_email("candysly@qq.com", "q3199608937@gmail.com",
               r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M8\ERP_PO\Website\test_report\12_55_05.html')
