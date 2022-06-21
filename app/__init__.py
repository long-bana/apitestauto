# -*- encoding: utf-8 -*-
"""
@File   :   __init__.py.py    
@Time   :   2022/6/21 14:28
@Author :   SunZelong
@Desc   :
"""
from flask import Flask

from config import Config

ata = Flask(__name__)
ata.config.from_object(Config)
