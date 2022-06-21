# -*- encoding: utf-8 -*-
"""
@File   :   __init__.py.py    
@Time   :   2022/6/21 17:07
@Author :   SunZelong
@Desc   :
"""
from flask_sqlalchemy import SQLAlchemy

from app import ata

db = SQLAlchemy(ata)
