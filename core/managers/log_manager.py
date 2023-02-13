import logging
import sys
from  logging import handlers
import time
log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(name)s - %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,level=logging.DEBUG)
th = handlers.TimedRotatingFileHandler(filename=f"logs/log-{time.strftime('%m%d%H%M')}.txt",encoding='utf-8')
formatter = logging.Formatter(log_format)
th.setFormatter(formatter)
logging.getLogger().addHandler(th)

class Logger:
    def __init__(self, name: str):
        self.name = name
        
    def log(self, type, msg):
        pass


class LogManager:
    loggers = {}

    def __init__(self):
        pass

    def get_logger(self, logger_name: str):
        if logger_name not in self.loggers.keys():
            self.loggers[logger_name] = Logger(logger_name)

        return self.loggers[logger_name]

