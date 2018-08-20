# -*- coding: utf-8 -*-

__author__ = "joyce"
import re
import os


class FindDevices(object):
    def __init__(self, logger):
        self.mylogger = logger

    def find_devices(self):
        """
        获得连接的设备（包括真机和虚拟机，原则上可以多台机器同时测试）
        devices_list = find_devices()
        """
        devices = re.findall(r'(.*?)\s+device', os.popen('adb devices').read())
        if len(devices) > 1:
            deviceids = devices[1:]
            self.mylogger.info('共找到 %s 个设备，设备列表 = %s' % (len(deviceids), deviceids))
            return deviceids
        else:
            self.mylogger.error('未找到设备，请重新检查!')
            return
