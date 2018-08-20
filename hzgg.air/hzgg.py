# -*- encoding=utf8 -*-
__author__ = "Admin-Y"

from airtest.core.api import *

auto_setup(__file__)

import os

def skip_first( time=10 ):    #令妃与皇后打架
    sleep( time )
    touch(Template(r"tpl1529998888354.png", record_pos=(-0.001, 0.153), resolution=(1920, 1080)))
    
def get_user():                     #注册账号
    touch(Template(r"tpl1529998337103.png", record_pos=(-0.091, 0.074), resolution=(1920, 1080)))
    sleep(1)
    touch(Template(r"tpl1529998391601.png", record_pos=(-0.052, -0.034), resolution=(1920, 1080)))
    sleep(1)
    text("qwer05"+str(i+3))           #每次运行需要修改“qwer03”中的内容，防止重复注册失败
    touch(Template(r"tpl1529998516528.png", record_pos=(-0.077, 0.02), resolution=(1920, 1080)))
    sleep(1)
    text("123")
    sleep(1)
    touch(Template(r"tpl1529998554015.png", record_pos=(-0.005, 0.075), resolution=(1920, 1080)))       #注册成功
    sleep(1)
    
def login():                       #登陆已有账号
    touch(Template(r"tpl1530014445162.png", record_pos=(-0.077, -0.034), resolution=(1920, 1080)))
    sleep(1)
    text("qwer01"+str(i))
    touch(Template(r"tpl1530014495615.png", record_pos=(-0.074, 0.02), resolution=(1920, 1080)))
    sleep(1)
    text("123")
    sleep(1)

def skip_dialog(time=10,ischeck=1):           #跳过剧情
    if ischeck:
        sleep(time)    
        touch((100,100))
    sleep(time)
    touch(Template(r"tpl1530081469635.png", record_pos=(0.46, -0.245), resolution=(1920, 1080)))
    
def skip_levelup():                 #跳过升级
    exists(Template(r"tpl1530244681358.png", record_pos=(-0.232, -0.195), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1530067095149.png", record_pos=(-0.232, -0.195), resolution=(1920, 1080)))
    
def select_role():                  #根据次数选择职业
    if i==0:
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("一")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==1:
        touch(Template(r"tpl1530015477610.png", record_pos=(0.167, -0.164), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("二")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==2:
        touch(Template(r"tpl1530015557403.png", record_pos=(0.28, -0.16), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("三")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==3:
        touch(Template(r"tpl1530015587745.png", record_pos=(0.389, -0.158), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("四")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==4:
        touch(Template(r"tpl1530015628385.png", record_pos=(0.302, 0.165), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("五")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==5:
        touch(Template(r"tpl1530015628385.png", record_pos=(0.302, 0.165), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015675671.png", record_pos=(0.167, -0.165), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("六")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==6:
        touch(Template(r"tpl1530015628385.png", record_pos=(0.302, 0.165), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015745760.png", record_pos=(0.281, -0.161), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("七")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    elif i==7:
        touch(Template(r"tpl1530015628385.png", record_pos=(0.302, 0.165), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015774636.png", record_pos=(0.391, -0.162), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015082592.png", record_pos=(0.18, 0.21), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("八")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)
    else:
        touch(Template(r"tpl1530015247392.png", record_pos=(0.153, 0.209), resolution=(1920, 1080)))
        os.system('adb shell "input keyevent 67"')
        text("零")
        touch(Template(r"tpl1530264187930.png", record_pos=(-0.423, 0.172), resolution=(1920, 1080)))
        touch(Template(r"tpl1530015337153.png", record_pos=(0.419, 0.198), resolution=(1920, 1080)))
        sleep(1)

        
    
appname="com.miaoyu.The9"

for i in range(8):

    os.system('adb install "C://Users//Admin-Y//Desktop//gggl_60.apk"')
    start_app(appname)
    try:
        wait(Template(r"tpl1530240670527.png", record_pos=(0.243, 0.227), resolution=(1920, 1080)),timeout=5)
        touch(Template(r"tpl1530240670527.png", record_pos=(0.243, 0.227), resolution=(1920, 1080)))
    except:
        pass
    sleep(5)                   #解压时间
    exists(Template(r"tpl1530086442739.png", record_pos=(0.38, -0.066), resolution=(1920, 1080)))       #断言是否在登陆界面

    get_user()                 #注册账号
    #login()                   #登陆已有账号
    
    touch(Template(r"tpl1529998629663.png", record_pos=(0.091, 0.077), resolution=(1920, 1080)))
    sleep(3)
    touch(Template(r"tpl1529998762646.png", record_pos=(0.001, 0.081), resolution=(1920, 1080)))
    sleep(40)                   #进入剧情
    assert_exists(Template(r"tpl1529999847913.png", record_pos=(0.461, -0.247), resolution=(1920, 1080)), "跳过剧情按钮出现")

    skip_dialog(time=3)

    skip_first()

    skip_first()

    skip_first()

    skip_first()

    skip_first()

    skip_first(time=14)

    skip_first(time=20)

    skip_first()

    skip_dialog()

    skip_dialog(time=3,ischeck=0)
    sleep(2)
    touch(Template(r"tpl1529999103596.png", record_pos=(-0.351, -0.07), resolution=(1920, 1080)))
    touch(Template(r"tpl1529999135767.png", record_pos=(-0.273, -0.169), resolution=(1920, 1080)))
    skip_dialog(ischeck=0)
    sleep(2)
    select_role()
    skip_dialog()
    sleep(3)
    touch(Template(r"tpl1530016893478.png", record_pos=(-0.23, -0.056), resolution=(1920, 1080)))
    sleep(2)
    touch(Template(r"tpl1530016914561.png", record_pos=(0.173, 0.064), resolution=(1920, 1080)))
    sleep(2)
    touch(Template(r"tpl1530016972944.png", record_pos=(0.205, 0.245), resolution=(1920, 1080)))
    sleep(2)
    swipe(Template(r"tpl1530066241374.png", record_pos=(0.156, -0.113), resolution=(1920, 1080)), vector=[-0.4157, -0.0491],duration=1)
    sleep(2)
    touch(Template(r"tpl1530074208021.png", record_pos=(0.396, -0.098), resolution=(1920, 1080)))
    sleep(2)
    swipe(Template(r"tpl1530066346374.png", record_pos=(0.152, -0.119), resolution=(1920, 1080)), vector=[-0.4277, -0.0242],duration=1)
    sleep(2)
    touch(Template(r"tpl1530072119273.png", record_pos=(0.4, 0.01), resolution=(1920, 1080)))
    sleep(2)
    swipe(Template(r"tpl1530066445573.png", record_pos=(0.153, -0.118), resolution=(1920, 1080)), vector=[-0.4131, 0.0009],duration=1)
    sleep(1)
    touch(Template(r"tpl1530066465034.png", record_pos=(-0.074, 0.127), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1530066483328.png", record_pos=(0.156, -0.17), resolution=(1920, 1080)))
    sleep(5)
    touch((1888,39))
    skip_levelup()
    sleep(10)
    touch(Template(r"tpl1530066597881.png", record_pos=(-0.089, -0.067), resolution=(1920, 1080)))
    skip_dialog(time=5,ischeck=0)
    touch(Template(r"tpl1530066672840.png", record_pos=(-0.001, 0.082), resolution=(1920, 1080)),times=16)
    touch((1,1))
    skip_dialog(time=5)
    sleep(10)
    touch(Template(r"tpl1530066757315.png", record_pos=(-0.015, 0.179), resolution=(1920, 1080)))
    sleep(5)
    touch((1,1))
    skip_levelup()
    sleep(1)
    touch(Template(r"tpl1530066962680.png", record_pos=(-0.084, -0.027), resolution=(1920, 1080)))
    touch(Template(r"tpl1530066982461.png", record_pos=(-0.012, -0.11), resolution=(1920, 1080)))
    sleep(5)
    touch((1847,74))
    touch(Template(r"tpl1530067023582.png", record_pos=(0.265, -0.115), resolution=(1920, 1080)))
    sleep(5)
    touch((1850,70))
    touch(Template(r"tpl1530067071881.png", record_pos=(0.465, -0.251), resolution=(1920, 1080)))
    skip_levelup()
    touch(Template(r"tpl1530067200729.png", record_pos=(-0.001, 0.005), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1530067200729.png", record_pos=(-0.001, 0.005), resolution=(1920, 1080)))
    sleep(3)
    touch(Template(r"tpl1530067232893.png", record_pos=(-0.059, -0.24), resolution=(1920, 1080)))
    sleep(4)
    swipe(Template(r"tpl1530076881966.png", record_pos=(-0.443, -0.102), resolution=(1920, 1080)), vector=[0.679, -0.0754],duration=1)
    sleep(2)
    swipe(Template(r"tpl1530077701860.png", record_pos=(-0.445, -0.008), resolution=(1920, 1080)), vector=[0.5941, 0.078],duration=1)
    sleep(2)
    touch(Template(r"tpl1530067372868.png", record_pos=(0.468, -0.254), resolution=(1920, 1080)))
    skip_levelup()
    skip_dialog(time=5)
    sleep(18)
    touch(Template(r"tpl1530067456288.png", record_pos=(-0.236, 0.209), resolution=(1920, 1080)))
    sleep(10)
    skip_levelup()
    skip_dialog(time=5)
    sleep(10)
    stop_app(appname)
    uninstall(appname)
