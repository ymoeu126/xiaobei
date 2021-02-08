#!/usr/bin/python
#coding:utf-8
import requests
import base64
import os
import json
import sys
import time
from datetime import datetime, timezone, timedelta

username= os.getenv("XIAOBEI_USERNAME")
pd= os.getenv("XIAOBEI_PASSWORD")
password=base64.b64encode(pd.encode())
password=password.decode()
SCKEY = os.getenv("XIAOBEI_SCKEY")
#健康打卡提交的信息
temperature={
    "temperature": "36.3",
    "coordinates": "中国-江西省-鹰潭市-月湖区",
    "location": "117.022953,28.238663",
    "healthState": "1",
    "dangerousRegion": "2",
    "dangerousRegionRemark": "",
    "contactSituation": "2",
    "goOut": "1",
    "goOutRemark": "",
    "remark": "",
    "familySituation": "1"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Host':'xiaobei.yinghuaonline.com',
    'Connection':  'Keep-Alive',
    'Accept-Encoding': 'gzip'
    }

#一系列的url
login_url ='https://xiaobei.yinghuaonline.com/prod-api/login'
health_url='https://xiaobei.yinghuaonline.com/prod-api/student/health'
captchaImage_url='https://xiaobei.yinghuaonline.com/prod-api/captchaImage'

session = requests.Session()
def captchaImage_session(_captchaImage_url):
    #获取滑动验证码的code和uuid传给post_data进行登录验证
    _captchaImage_session=session.get(captchaImage_url,headers=headers,verify=False )
    return json.loads(_captchaImage_session.text)
def login_session(_captchaImage_session,_username,_password):
    code=_captchaImage_session['showCode']
    uuid=_captchaImage_session['uuid']
    post_data={
        "username":username,
        "password":password,
        "code":code,
        "uuid":uuid
    }

    #登录小北同学得到token并且传给headers中的Authorization发送请求头中
    _login_session=session.post(login_url,json = post_data,headers = headers,verify=False)
    return json.loads(_login_session.text)

def get_token(_login_session):
    try:
        token=_login_session['token']
        headers["Authorization"] ='Bearer ' +token
        post_health()
    except Exception as e:
        notify('账号或者密码错误')

def post_health():
    _post_health=session.post(health_url,json = temperature,headers = headers,verify=False)
    return json.loads(_post_health.text)

def get_today_date():
    _tz = timezone(+timedelta(hours=8))
    return datetime.now(_tz).strftime("%Y.%m.%d,%A,%H时")

def notify(_title, _message=None):
    if not _message:
        _message = _title
    
    _data = get_today_date()
    _test =_title+_data
    print(_test)
    weixin_response = requests.post(f"https://sc.ftqq.com/{SCKEY}.send", {"text": _title, "desp": _test},verify=False)
    qq_response = requests.post("https://qmsg.zendee.cn/send/c5d807f21ef662b4d61833bc3045d537", {"msg": _test},verify=False)
if __name__ == "__main__":
    if not username or not password:
        notify("用户名或账号为空，请仔细阅读配置步骤！")
        sys.exit()
    _captchaImage_session=captchaImage_session(captchaImage_url)
    _login_session=login_session(_captchaImage_session,username,password)
    get_token(_login_session)
    try:
        response=post_health()
        if response['code'] == 200:
            notify("小北同学打卡成功")
        else:
            notify("打卡失败，请手动打卡", response.text)
    except Exception as e:
        notify("打卡失败，请手动打卡", str(e))

    
    
    
    
    
    
    

