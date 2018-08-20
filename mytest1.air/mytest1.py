

__author__ = "build"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""
from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
import sys
sys.path.insert(0, r"C:\Python27\Lib\site-packages\airtest") 
sys.meta_path = []

import airtest


def out_log_name():
    now1 = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    log_path = os.getcwd() + '\\log'
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    return log_path + "\\" + now1 + r"_logcat.log"


def do_case():
    for i in range(1, 20):
        stop_app("com.thebingo.mhtt")
        sleep(2)
        start_app("com.thebingo.mhtt")  # com.thebingo.mhtt/com.thebingo.mhtt.Mhtt
        sleep(1.0)
        touch(Template(r"tpl1521188959375.png", record_pos=(-0.415, -0.228), resolution=(1920, 1080)))
        sleep(7)
        touch(Template(r"tpl1521188974369.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(-0.007, 0.177), resolution=(1920, 1080)))
        touch(assert_exists(Template(r"tpl1521189604597.png", record_pos=(0.001, 0.206), resolution=(1920, 1080)), u'test'))
        sleep(2)

        
# start your script here
connect_device("Android:///28PNW17C29031314")
adb = ADB()
adb.serialno = ADB().devices(state="device")[0][0]
# logcatname = out_log_name()
# handle = subprocess.Popen("adb shell logcat ActivityManager:I  My App:D *:S >> %s" % logcatname, shell=True)
# for i in range(1, 10):
#     do_case()
#     sleep(5)
# subprocess.Popen("taskkill /F /T /PID " + str(handle.pid), shell=True)

a = device()
appname = 'com.thebingo.mhtt'
# subprocess.Popen("adb shell logcat -c")
# a.shell('logcat -c')
do_case()
# logcat_path = out_log_name()
# logcat_path = os.path.join(G.LOGGER.logfile, "..\\logcat.txt")

# if os.path.exists(logcat_path):
#     os.remove(logcat_path)

# try:
#     do_case()
# except:
#     try:
#         # system = platform.system()
#         # if system is "Windows":
#         #     find_util = "findstr "
#         # else:
#         #     find_util = "grep "
#         str = 'ps|grep ' + appname
#         a.shell(str)
#     except:
#         with open(logcat_path, 'wb') as f:
#             for x in a.logcat(grep_str=appname):
#                 f.write(x)
