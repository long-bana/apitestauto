# -*- encoding: utf-8 -*-
"""
@File   :   __init__.py.py    
@Time   :   2022/6/21 14:28
@Author :   SunZelong
@Desc   :
"""
from flask import Flask
from flask_cors import CORS

from config import Config

ata = Flask(__name__)
CORS(ata,supports_credentials=True)

ata.config.from_object(Config)
