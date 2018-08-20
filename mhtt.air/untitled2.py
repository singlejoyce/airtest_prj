from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco = AndroidUiautomationPoco(force_restart=False)
# -*- encoding=utf8 -*-
__author__ = "Admin-Y"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

import threading
import os

def install_app():
    os.system("adb install C://Users//Admin-Y//Desktop//ddl_0607.apk")

def con():
    sleep(30)
    wait(Template(r"tpl1528698212841.png", record_pos=(-0.233, 0.91), resolution=(1080, 2160)),40)
    sleep(1)
    touch(Template(r"tpl1528698212841.png", record_pos=(-0.233, 0.91), resolution=(1080, 2160)))


appname = "com.ddl.idolgame.ddl"

try:
    for x in range (5):
        tn = []
        t1 = threading.Thread(target=install_app)
        tn.append(t1)
        t2 = threading.Thread(target=con)
        tn.append(t2)

        for i in tn:
            i.start()

        for i in tn:
            i.join()        

        start_app(appname)
        sleep(150)
        touch(wait(Template(r"tpl1527753069218.png", record_pos=(0.25, 0.23), resolution=(1920, 1080)),200))

        try:
              while assert_exists(Template(r"tpl1527753069218.png", record_pos=(0.25, 0.23), resolution=(1920, 1080)),10):
                    sleep(1)
                    touch(Template(r"tpl1527753069218.png", record_pos=(0.25, 0.23), resolution=(1920, 1080)))
        except (TargetNotFoundError,AssertionError):
            pass


        wait(Template(r"tpl1527751029491.png", record_pos=(-0.005, 0.179), resolution=(1920, 1080)))
        sleep(1)
        touch(Template(r"tpl1527751029491.png", record_pos=(-0.005, 0.179), resolution=(1920, 1080)))

        sleep(3.0)

        touch(wait(Template(r"tpl1527749786400.png", record_pos=(-0.247, 0.057), resolution=(1920, 1080))))

        try:
              while assert_exists(Template(r"tpl1527753069218.png", record_pos=(0.25, 0.23), resolution=(1920, 1080))):
                    sleep(1)
                    touch(Template(r"tpl1527753069218.png", record_pos=(0.25, 0.23), resolution=(1920, 1080)))
        except (TargetNotFoundError,AssertionError):
            pass

        touch(Template(r"tpl1528698145053.png", record_pos=(-0.076, 0.082), resolution=(2160, 1080)))
        sleep(3)
        touch(wait(Template(r"tpl1527757146177.png", record_pos=(-0.11, 0.067), resolution=(1920, 1080))))
        sleep(3)

        try:
            while assert_exists(Template(r"tpl1527749904155.png", record_pos=(0.002, 0.207), resolution=(1920, 1080))):
                touch(Template(r"tpl1527749904155.png", record_pos=(0.002, 0.207), resolution=(1920, 1080)))
        except (TargetNotFoundError,AssertionError):
            touch(Template(r"tpl1527759774441.png", record_pos=(0.324, -0.252), resolution=(1920, 1080)))


        sleep(20)
        keyevent("back")
        wait(Template(r"tpl1528375534276.png", record_pos=(0.077, 0.04), resolution=(2160, 1080)))
        sleep(1)
        touch(Template(r"tpl1528375534276.png", record_pos=(0.077, 0.04), resolution=(2160, 1080)))
        stop_app(appname)
        uninstall(appname)
except:
    uninstall("com.ddl.idolgame.ddl")


