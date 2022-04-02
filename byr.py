import requests
from bs4 import BeautifulSoup

from scraper import scraper

class byr_scraper(scraper):
    def __init__(self,username,password,cookie = None):
        super(byr_scraper,self).__init__(username,password,cookie)
        self.url = 'https://byr.pt/'
    
    def login(self):
        self.login_with_img()