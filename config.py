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
    JSON_AS_ASCII = False

    # mysql 连接信息
    MYSQL_HOST = "146.56.200.224"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "long0216"
    DATABASE_NAME = "apitestauto"

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST,
                                                                             MYSQL_PORT, DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
