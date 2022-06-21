# -*- encoding: utf-8 -*-
"""
@File   :   Jwt.py    
@Time   :   2022/6/21 17:38
@Author :   SunZelong
@Desc   :
"""
import hashlib
from datetime import datetime, timedelta

import jwt
from jwt import ExpiredSignatureError

EXPIRED_HOUR = 3


class UserToken(object):
    key = "ataToken"
    salt = "ata"

    @staticmethod
    def get_token(data):
        new_data = dict({"exp": datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)}, **data)
        return jwt.encode(new_data, key=UserToken.key).decode()

    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception("token已过期，请重新登录")

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        bt = f"{password}{UserToken.salt}".encode("utf-8")
        m.update(bt)
        return m.hexdigest()
