import logging

class Loggen:
    @staticmethod
    def mylog():
        logging.basicConfig(filename="C:/Automation_practice_with_pytest/logs/log2.log",level=logging.INFO)
        logger=logging.getLogger()
        return logger
if __name__ == "__main__":
    logger = Loggen.mylog()
    logger.info("This is a test log message.")

