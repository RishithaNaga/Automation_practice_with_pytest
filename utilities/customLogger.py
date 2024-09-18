import logging

class Loggen:
    @staticmethod
    def mylog():
        logging.basicConfig(filename="C:\\forlogging\\log1.log",level=logging.INFO,format="%(asctime)s:%(levelname)s:%(message)s",datefmt="%m/%d/%y  %I:%M:%S %P")
        logger=logging.getLogger()
        return logger


