"""
    This module contains the logger class.
"""
import logging


class Logger:
    def __int__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

        self.file_handler = logging.FileHandler('logs.log')
        self.file_handler.setFormatter(self.formatter)

        self.logger.addHandler(self.file_handler)

    def log(self, level, message):
        self.logger.log(level, message)
