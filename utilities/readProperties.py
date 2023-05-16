
from selenium import webdriver
import configparser
config = configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL(self):
        url = self.config.get('common info', 'baseURL')
        return url

