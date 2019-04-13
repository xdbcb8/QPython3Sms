#coding=utf-8

import sys
import re
import time
from androidhelper import Android

def waitTime(min):
    """
    等待时间
    """
    print("")
    second = min * 60
    while True:
        time.sleep(1)
        second -= 1
        m = int(second / 60)
        s = second%60
        if m > 0:
            sys.stdout.write("\r剩余{}分{}秒发送查询短信...".format(m,s))
        else:
            sys.stdout.write(u"\r剩余{}秒发送查询短信...".format(s))
        sys.stdout.write("\r")
        sys.stdout.flush()
        if second < 0:
            sys.stdout.flush()
            print("移动流量查询短信发送中...")
            break

def sendSms():
    """
    发送短信
    """
    d = Android()
    # 创建一个安卓运用实例
    
    d.smsSend("10086", "113")
    # 给10086发送短信查询代码
    
    time.sleep(5)
    # 暂停5秒，给手机一个发送时间
    
    sms_data=d.smsGetMessages(False, "inbox")
    # 读取短信
    
    latest_sms = sms_data.result[0]["body"]
    # 取得短信内容
    
    patterns = re.compile(r"；已使用移动数据流量为(.*?)；")
    flow = re.findall(patterns, latest_sms)
    # 只要流量部分
    
    if flow:
    # 要是匹配到表明查询成功，输出结果
        ydFlow = flow[0]
        print("已使用" + ydFlow)

if __name__ == "__main__":
    minute = int(input("请输入多少分钟查询一次："))
    while True:
        waitTime(minute)
        sendSms()
        
