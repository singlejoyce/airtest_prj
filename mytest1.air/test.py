from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *


a = ADB()
a.serialno = "28PNW17C29031314"
# print(a.cmd("shell pm list packages"))

a.connect()