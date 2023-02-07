import logging
#
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

