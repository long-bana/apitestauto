# -*- encoding: utf-8 -*-
"""
@File   :   run.py    
@Time   :   2022/6/21 14:31
@Author :   SunZelong
@Desc   :
"""
from app import ata


@ata.route("/")
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    ata.run("0.0.0.0", threaded=True, port=7777)
