# Birthday_Mail

### 运行`mian.py`，与birthday日期匹配。读取邮件模板，发送邮件到匹配者的邮箱。

### 你还需要创建一个新文件`config.py`,这里存放着你的配置信息。
#### 你可以参考如下配置
```python
# 查找数据文件
data_file = 'a.csv'
# 邮件模板文件
html_file = 'b.html'

mail_config = {
    # 邮件发送者名称
    "sendname": "小东西",
    # 邮件发送地址
    "sendadress": "site@msg.anyfan.top"
}

# 阿里云密钥
al_secret = {
    "accessid": "********************",
    "AccesskeySecret": "************************************"
}
```