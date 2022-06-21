# -*- encoding: utf-8 -*-
"""
@File   :   run.py    
@Time   :   2022/6/21 14:31
@Author :   SunZelong
@Desc   :
"""
from datetime import datetime

from app import ata
from app.controllers.auth.user import auth
from app.utils.logger import Log

from app import dao

# 注册蓝图
ata.register_blueprint(auth)


@ata.route("/")
def hello_world():
    log = Log("hello world 专用")
    log.info("有人访问你的网站了")
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    print(now)
    return now


if __name__ == '__main__':
    ata.run("0.0.0.0", threaded=True, port=7777)
