# -*- coding:utf-8 -*-
# @Author: wym
# @Email : wang-ya-ming@foxmail.com
# @Date  : 2020/11/13 14:21

import datetime, requests, base64
import socket
import os
import sys

def ping_check(ip):  # 测试方法2 直接ping的方法
    return_code = os.system("ping " + ip + " -n 2")
    if return_code:
        return False
    return True

login_url = "http://192.168.10.6/0.htm"  # 校园网地址,字段获取和messge获取方式一样
name = '###'  # 账号 
password = '###'  # 密码

def login(name, password):
    message = {
        'DDDDD': name,
        'upass': password,
        '0MKKey': ' '
    }  # 该字段获取：登陆页面按F12——Network——点击登录
    try:
        result = requests.post(login_url, data=message)
        # print(result.text) # 打印请求结果
        print("[01] {} login success".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # 登陆成功
    except:
        print("[00] {} request error".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

net_status = ping_check("www.baidu.com")
while net_status != True:
    login(name, password)
    net_status = ping_check("www.baidu.com")
else:
    print("login success")

sys.exit(0)#执行完推出程序

#win10开机自启设置 https://blog.csdn.net/qq_38791897/article/details/104219079
#以下是win10自动启动脚本代码，新建txt以后后缀改成bat，讲bat文件放入如下路径 C:\Users\你的Windows账户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
'''
@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
E:
cd E:\00 CodeHub
python login.py
'''

# 后续改进：
# 账号密码加密提高安全性
# 设置开机自动登录网络
# 读取当前ip，写入到frp文件，重启frp
# 重启teamviewer
# 保证暴露到外端的端口不变

