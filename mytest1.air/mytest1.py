from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
import os
import sys
from airtest.utils.logger import get_logger

sys.path.insert(0, r"C:\Python27\Lib\site-packages\airtest")
sys.meta_path = []


def out_log_name():
    now1 = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    log_path = os.getcwd() + '\\log'
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    return log_path + "\\" + now1 + r"_logcat.log"


# start your script here
connect_device("Android:///6c7768940704")
adb = ADB()
adb.serialno = ADB().devices(state="device")[0][0]
a = device()
a.shell('logcat -c')
# logcat_path = os.path.join(G.LOGGER.logfile, "..\\logcat.txt")
logcat_path = out_log_name()
if os.path.exists(logcat_path):
    os.remove(logcat_path)
appname_ddl = "com.ddl.idolgame.ddl"
appname = "com.thebingo.mhtt"
appname_lw = "com.ddianle.lovedance.chinanet"


# do case
def do_case():
    for i in range(1, 50):
        stop_app(appname)
        sleep(2)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====start, times:%s" % i)
        sleep(2)
        start_app(appname)
        sleep(15)
        touch(Template(r"tpl1534226504833.png", record_pos=(-0.426, -0.183), resolution=(2160, 1080)))

        sleep(5)
        touch(Template(r"tpl1534226988607.png", record_pos=(-0.057, 0.156), resolution=(2160, 1080)))
        sleep(5)
        touch(Template(r"tpl1533281372348.png", record_pos=(-0.009, 0.205), resolution=(1920, 1080)))

        sleep(8)
        assert_exists(Template(r"tpl1533547812398.png", record_pos=(0.147, -0.101), resolution=(2160, 1080)), u"crash")
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====end, times:%s" % i)


# ddl sdk apk use
def do_case_ddl():
    for i in range(1, 50):
        sleep(2)
        stop_app(appname_ddl)
        sleep(2)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====start, times:%s" % i)
        start_app(appname_ddl)
        sleep(15)
        touch(Template(r"tpl1534226988607.png", record_pos=(-0.057, 0.156), resolution=(2160, 1080)))
        sleep(8)
        touch(Template(r"tpl1533281372348.png", record_pos=(-0.009, 0.205), resolution=(1920, 1080)))
        sleep(10)
        # assert_exists(Template(r"tpl1533799217514.png", record_pos=(0.286, -0.225), resolution=(2160, 1080)), u"crash")
        assert_exists(Template(r"tpl1533547812398.png", record_pos=(0.147, -0.101), resolution=(2160, 1080)), u"crash")
        sleep(5)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====end, times:%s" % i)


# lw
def do_case_lw():
    for i in range(1, 100):
        sleep(2)
        stop_app(appname_lw)
        sleep(2)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====start, times:%s" % i)
        start_app(appname_lw)
        sleep(15)
        touch(Template(r"tpl1534315736224.png", record_pos=(0.318, 0.087), resolution=(2160, 1080)))
        sleep(5)
        touch(Template(r"tpl1534315759751.png", record_pos=(-0.037, 0.11), resolution=(2160, 1080)))

        sleep(10)
        assert_exists(Template(r"tpl1534315804267.png", record_pos=(-0.315, -0.215), resolution=(2160, 1080)),
                      "crashed")

        sleep(10)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====end, times:%s" % i)


try:
    # do_case()
	do_case_ddl()
except:
    try:
        system = platform.system()
        if system is "Windows":
            find_util = "findstr "
        else:
            find_util = "grep "
        cmdstr = 'ps|grep ' + appname
        a.shell(cmdstr)
    except:
        # with open(logcat_path, 'wb') as f:
        #     for x in a.logcat():
        #         f.write(x)
        handle = subprocess.Popen("adb shell logcat >> %s" % logcat_path, shell=True)
        sleep(30)
        subprocess.Popen("taskkill /pid %s -t -f " % str(handle.pid), shell=True)
