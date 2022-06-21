# -*- encoding: utf-8 -*-
"""
@File   :   __init__.py.py    
@Time   :   2022/6/21 17:26
@Author :   SunZelong
@Desc   :
"""
from app.models import db
from app.models.user import User

db.create_all()
