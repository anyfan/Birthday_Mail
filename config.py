import os

lunar_mo = 'luner.html'
solar_mo = 'solar.html'

user_url = "https://docs.anyfan.top/#/unsubscribe?user="

db_url = os.environ['mongodb_url']

mail_config = {
    "sendname": "小东西",
    "sendadress": "site@msg.anyfan.top"
}

al_secret = {
    "accessid": os.environ['al_accessid'],
    "AccesskeySecret": os.environ['al_AccesskeySecret']
}