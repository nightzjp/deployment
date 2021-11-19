# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: q.py
@time: 2021/11/18 下午4:43
"""
import time
import random
import threading
from datetime import datetime
from queue import Queue


class SingletonType:
    _instance_lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class WaterFallAlarm(SingletonType):
    """瀑布图报警数据模拟"""
    
    def __init__(self, size=100, timeout=2):
        self.size = size
        self.timeout = timeout
        self.queue = Queue(maxsize=self.size)
    
    @staticmethod
    def get_channel():
        """随机返回一个通道"""
        return random.choice([0, 1])
    
    @staticmethod
    def get_point_list():
        """随机返回1000个点"""
        point_list = list(range(1000))
        random.shuffle(point_list)
        return point_list
    
    @staticmethod
    def get_date_time():
        """返回当前毫秒时间字符串"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
    
    def get_alarm_data(self):
        """产生一条报警数据"""
        alarm_data = {
            "channel": self.get_channel(),
            "data": self.get_point_list(),
            "createAt": self.get_date_time()
        }
        return alarm_data
    
    def put_queue(self, num=0):
        """数据入队"""
        for item in range(num):
            time.sleep(0.2)
            if self.queue.qsize() < self.queue.maxsize:
                print(item)
                self.queue.put(self.get_alarm_data(), block=True, timeout=self.timeout)
            else:
                self.get_queue()
    
    def get_queue(self):
        """数据出队"""
        if self.queue.qsize():
            return self.queue.get(block=True, timeout=self.timeout)
        return None
    
    def run(self):
        """入队+出队"""
        self.put_queue(num=15)
        for item in range(self.queue.qsize()):
            print(self.get_queue())
        print(self.queue.qsize())


alarm = WaterFallAlarm()
