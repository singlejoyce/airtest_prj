# _*_ coding: utf-8 _*_

__author__ = "joyce"

import logging  
import time
import os


class Logger(object):
  
    def __init__(self, logger, log_name):

        now1 = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        log_path = os.getcwd() + '\\Logs'
        if not os.path.isdir(log_path):
            os.mkdir(log_path)
        log_name = log_path + "\\" + now1 + r"_" + log_name + r".log"

        """ 
        指定保存日志的文件路径，日志级别，以及调用文件 
            将日志存入到指定的文件中 
        :param logger: 
        """  
        # 创建一个logger  
        self.logger = logging.getLogger(logger)  
        self.logger.setLevel(logging.DEBUG)  
  
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)  
  
        # 再创建一个handler，用于输出到控制台  
        ch = logging.StreamHandler()  
        ch.setLevel(logging.INFO)  
  
        # 定义handler的输出格式  
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
        fh.setFormatter(formatter)  
        ch.setFormatter(formatter)  
  
        # 给logger添加handler  
        self.logger.addHandler(fh)  
        self.logger.addHandler(ch)  
  
    def getlog(self):
        return self.logger

