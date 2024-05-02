# DUA TIPE LOG YANG DIGUNAKAN: STREAM DAN FILE
# Stream: log akan ditulis ketika program dijalankan
# File: log akan ditangkap ditulis pada sebuah file 
import logging


class AppLog:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler("error.log")
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.ERROR)

        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        log_format = logging.Formatter(log_format)

        c_handler.setFormatter(log_format)
        f_handler.setFormatter(log_format)

        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def warning(self, message):
        self.logger.warning(f"{message}")

    def error(self, message):
        self.logger.error(f"{message}")