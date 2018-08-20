# -*- encoding=utf8 -*-
__author__ = "build"

from airtest.core.api import *
from airtest.utils.logger import get_logger
import sys
sys.path.insert(0, r"C:\Python27\Lib\site-packages\airtest") 
sys.meta_path = []

auto_setup(__file__)
LOGGING = get_logger(__name__)
# init
a=device()
a.shell('logcat -c')
logcat_path=os.path.join(G.LOGGER.logfile,"..\\logcat.txt")
if os.path.exists(logcat_path):
    os.remove(logcat_path)
appname_ddl = "com.ddl.idolgame.ddl"
appname = "com.thebingo.mhtt"
appname_lw = "com.ddianle.lovedance.chinanet"

# do case 
def do_case():
    for i in range(1,100):
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
    for i in range(1,100):
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
    for i in range(1,100):
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
        assert_exists(Template(r"tpl1534315804267.png", record_pos=(-0.315, -0.215), resolution=(2160, 1080)), "crashed")

        sleep(10)
        if LOGGING is not None:  # may be None atexit
            LOGGING.error("======joyce=====end, times:%s" % i)

            
            
            
try:
    do_case()
    # do_case_ddl()
    # do_case_lw()
except:
    try:
        system = platform.system()
        if system is "Windows":
            find_util = "findstr "
        else:
            find_util = "grep "
        str = 'ps|grep ' + appname
        a.shell(str)
    except:
        with open(logcat_path, 'wb') as f:
            for x in a.logcat(grep_str=appname):
                f.write(x)



