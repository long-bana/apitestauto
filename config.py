# -*- encoding: utf-8 -*-
"""
@File   :   config.py    
@Time   :   2022/6/21 14:39
@Author :   SunZelong
@Desc   :   配置文件-基础配置类
"""
import os


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, "logs", "pity.log")
