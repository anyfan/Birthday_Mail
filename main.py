from tool.db import db
from tool.ZhDate import ZhDate
from datetime import datetime
from tool.al_mail import al_mail
import config

# 连接数据库
users_data = db(config.db_url)

# 今天的时间
luner_date = ZhDate.today()
solar_date = datetime.now()
# 时间转为字符
luner_str = luner_date.chinese()[5: 9]
solar_str = solar_date.strftime('%b')+' '+solar_date.strftime('%d')
# 对应的月，日
l_mon = luner_date.lunar_month
l_day = luner_date.lunar_day
s_mon = solar_date.month
s_day = solar_date.day

# 构造查找表
luner_query = {"lunar_cal": l_mon*100+l_day, "receive_lunar": True}
solar_query = {"solar_cal": s_mon*100+s_day, "receive_solar": True}

send_list_luner = users_data.col_find(
    luner_query, {"_id": 1, "name": 1, "mail": 1})
send_list_solar = users_data.col_find(
    solar_query, {"_id": 1, "name": 1, "mail": 1})

# 阿里云邮件推送
al_config = dict(config.mail_config, **config.al_secret)
al_mail = al_mail(al_config)

# 农历生日发送
with open(config.lunar_mo, "r", encoding="utf-8") as html_txt:
    html_data = html_txt.read()
    for user in send_list_luner:
        print(user["name"])
        mail_body = html_data.replace("{{name}}", user['name'])
        mail_body = mail_body.replace("{{date}}", luner_str)
        mail_body = mail_body.replace(
            "{{url}}", config.user_url+str(user['_id']))
        al_mail.send(user["mail"], "Happy Birthday", mail_body)

html_txt.close()


# 阳历生日发送
with open(config.solar_mo, "r", encoding="utf-8") as html_txt:
    html_data = html_txt.read()
    for user in send_list_solar:
        print(user["name"])
        mail_body = html_data.replace("{{name}}", user['name'])
        mail_body = mail_body.replace("{{date}}", solar_str)
        mail_body = mail_body.replace(
            "{{url}}", config.user_url+str(user['_id']))
        al_mail.send(user["mail"], "Happy Birthday", mail_body)

html_txt.close()


users_data.__del__()
