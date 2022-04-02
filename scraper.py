import requests
from bs4 import BeautifulSoup

class scraper:
    def __init__(self,username,password,cookie = None):
        self.cookie = cookie
        self.url = None
        self.login_target = "takelogin.php"
        self.login_home = "login.php"
        self.params = {
            "username" : username,
            "password" : password,
        }

    def simple_login(self):
        r = requests.post(
            self.url + self.login_target,
            data = self.params,
            allow_redirects = False,
            headers = {
                "Content-Type" : "application/x-www-form-urlencoded",
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
            }
        )

        self.cookie = requests.utils.dict_from_cookiejar(r.cookies)

        if self.cookie == None:
            return False
        else:
            return True
    
    def login_with_img(self):
        r = requests.get(self.url + self.login_home)
        soup = BeautifulSoup(r.text,"html.parser")

        img = soup.find("img",{"alt" : "CAPTCHA"}).get("src")
        imghash = img.split("=")[-1]

        print(self.url + img)
        hashcode = input("Please input the hashcode: ")
        self.params["imagestring"] = hashcode
        self.params["imagehash"] = imghash

        self.simple_login()

    
    def search(self,name):
        if self.cookie == None:
            return None
        raw_data = self.search_raw(name)
        data = []
        id = 0
        for i in raw_data:
            content = self.process_raw_data(i)
            content["id"] = id
            id += 1
            data.append(content)
        
        return data
    
    def login(self):
        self.simple_login()