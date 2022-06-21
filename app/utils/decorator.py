# -*- encoding: utf-8 -*-
"""
@File   :   decorator.py    
@Time   :   2022/6/21 15:20
@Author :   SunZelong
@Desc   :   装饰器方法文件
"""


class SingletonDecorator:
    """
    单例装饰器
    """
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance
