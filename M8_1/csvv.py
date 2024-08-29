import csv


def read_csv(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        # 然后这个方法你可以学一下
        # 直接去掉标题行
        # 我不习惯 我还是喜欢那样写 我都写了快一百遍了啊哈哈哈 啊哈哈哈也可以哒
        next(reader)
        for row in reader:
            result.append(row)
    return result
