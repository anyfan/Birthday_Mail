import datetime
import hmac
import base64
import requests
import hashlib
from urllib.parse import quote

# 阿里云邮件推送的封装
class al_mail:
    api_config = {
        "url": "https://dm.aliyuncs.com/",
        "version": "2015-11-23",
        "region": "cn-hangzhou"
    }

    def __init__(self, al_config):
        self.config = al_config
        # Employee.empCount += 1

    def url_encode_str(self,all_params):
        # url编码
        def str_encode(str_encode):
            encode_str = quote(str(str_encode))
            encode_str = encode_str.replace('/', '%2F')
            return encode_str
        sort_all_params = list()
        for key, value in all_params.items():
            params = str_encode(key) + '=' + str_encode(value)
            sort_all_params.append(params)
        # 对参数进行升序排序
        sort_all_params.sort()
        return sort_all_params

    def get_signature(self,param, http_method, AccesskeySecret):
        str_to_sign = ''
        sort_all_params = self.url_encode_str(param)
        for i in range(len(sort_all_params)):
            str_to_sign = str_to_sign + sort_all_params[i] + '&'
        # 将最后一位&给截取掉
        str_to_sign = http_method + '&%2F&' + quote(str_to_sign[:-1])
        # print(str_to_sign)
        key = AccesskeySecret+'&'
        signature = hmac.new(key.encode(
            'utf-8'), str_to_sign.encode('utf-8'), digestmod=hashlib.sha1)
        signature = base64.b64encode(signature.digest())
        # bytes -> str 转换
        signature = signature.decode('utf-8')
        return signature

    def send(self, to, subject, body):
        send_data = {
            "Action": "SingleSendMail",  # 操作接口名
            "ClickTrace": "1",  # 打开数据跟踪功能
            "AccountName": self.config["sendadress"],  # 发件地址
            "ReplyToAddress": "true",  # 回信地址
            "AddressType": 1,  # 地址类型
            "ToAddress": to,  # 收件地址
            "FromAlias": self.config["sendname"],  # 发件人名称
            "Subject": subject,  # 邮件标题
            "HtmlBody": body,  # 邮件内容
            "Format": "JSON",  # 返回JSON
            "Version": self.api_config["version"],  # API版本号
            "AccessKeyId": self.config["accessid"],  # Access Key ID
            "SignatureMethod": "HMAC-SHA1",  # 签名方式
            "Timestamp": datetime.datetime.utcnow().isoformat(),  # 请求时间
            "SignatureVersion": "1.0",  # 签名算法版本
            "SignatureNonce": datetime.datetime.now().timestamp(),  # 唯一随机数
            "RegionId": self.api_config["region"]  # 机房信息
        }
        send_data['Signature'] = self.get_signature(
            send_data, 'POST', self.config["AccesskeySecret"])

        res = requests.post(url=self.api_config["url"], data=send_data)
        print(res.text)
