import config
from al_mail import al_mail
import csv
import datetime



# 当前日期
now_day = datetime.datetime.now()
# 发送信息列表
birthday_data = []
# 将邮箱设置与阿里密钥合并成新字典
al_config = dict(config.mail_config, **config.al_secret)

# 找出今天过生日的人
with open(config.data_file, "r", encoding='utf-8-sig') as data_csv:
    reader = csv.DictReader(data_csv)
    for row in reader:
        birthday = datetime.datetime.strptime(row['birthday'], '%Y/%m/%d')
        if (now_day.month == birthday.month) & (now_day.day == birthday.day):
            birthday_data.append(row)





if birthday_data:
    # 将日期转为英文
    def time_to_en(daytime):
        month_num = daytime.month-1
        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                        'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return (month_list[month_num]+' '+('%02d' % daytime.day))

    # 创建一个
    al_mail = al_mail(al_config)

    with open(config.html_file, "r", encoding="utf-8") as html_txt:
        html_data = html_txt.read()
        for someone in birthday_data:
            mail_body = html_data.replace("{{name}}", someone['name'])
            mail_body = mail_body.replace("{{date}}", time_to_en(now_day))
            # al_mail.send(someone["mail"], "Happy Birthday", mail_body)

else:
    print("今天没有人过生日")




