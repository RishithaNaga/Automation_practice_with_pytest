import configparser

congif_object=configparser.ConfigParser()
congif_object.read("C:\Automation_practice_with_pytest\Configurations\config.ini")

class Config:
    @staticmethod
    def get_url():
        url=congif_object.get("application specific data","url")
        return u