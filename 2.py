#!/usr/bin/python
#coding:utf-8
import requests
import base64
import os
import json

username= os.getenv("XIAOBEI_USERNAME")
pd= os.getenv("XIAOBEI_PASSWORD")
password=base64.b64encode(pd.encode())
password=password.decode()
SCKEY = os.getenv("XIAOBEI_SCKEY")

temperature={
    "temperature": "36.3",
    "coordinates": "中国-江西省-鹰潭市-月湖区",
    "location": "117.05768,28.261384",
    "healthState": "1",
    "dangerousRegion": "2",
    "remark": ""
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Host':'xiaobei.yinghuaonline.com',
    'Connection':  'Keep-Alive',
    'Accept-Encoding': 'gzip'
    }
login_url ='https://xiaobei.yinghuaonline.com/prod-api/login'
health_url='https://xiaobei.yinghuaonline.com/prod-api/student/health'
yanzhengma_url='https://xiaobei.yinghuaonline.com/prod-api/captchaImage'
session = requests.Session()
q1=session.get(yanzhengma_url,headers=headers )
code=q1.json()['showCode']
uuid=q1.json()['uuid']

post_data={
    "username":username,
    "password":password,
    "code":code,
    "uuid":uuid
}

q2=session.post(login_url,json = post_data,headers = headers)
token=q2.json()['token']
headers["Authorization"] ='Bearer ' +token

response2 = session.post(health_url,json = temperature,headers = headers)
if response2.status_code == 200:
    message='打卡成功'   
else:
    message='请仔细阅读步骤,或者出现了bug'
print(message)    
#server酱
api = "https://sc.ftqq.com/"+SCKEY+".send"
server_data = {
    "text": '小北同学打卡',
    "desp": message
}
requests.post(api, data = server_data)

