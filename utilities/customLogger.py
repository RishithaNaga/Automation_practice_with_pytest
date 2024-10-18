import logging

class Loggen:
    @staticmethod
    def mylog():
        logging.basicConfig(filename="C:/Automation_practice_with_pytest/logs/log3.log",level=logging.INFO,format="%(asctime)s:%(levelname)s:%(message)s",datefmt="%m/%d/%y  %I:%M:%S %P")
        logger=logging.getLogger()
        return logger
# if __name__ == "__main__":
#     logger = Loggen.mylog()
#     logger.info("This is a test log message.")

