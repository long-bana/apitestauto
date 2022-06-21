# -*- encoding: utf-8 -*-
"""
@File   :   logger.py    
@Time   :   2022/6/21 15:15
@Author :   SunZelong
@Desc   :
"""
import logbook
from app import ata
from app.utils.decorator import SingletonDecorator


@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self, name='ata', filename=ata.config['LOG_NAME']):
        """

        :param name: 业务名称
        :param filename: 文件名称
        """
        logbook.set_datetime_format('local')
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)
