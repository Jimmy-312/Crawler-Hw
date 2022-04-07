import requests
from bs4 import BeautifulSoup

class scraper:
    def __init__(self,username = None,password = None,cookie = None):
        self.cookie = cookie
        self.url = None
        self.is_login = False
        self.login_target = "takelogin.php"
        self.login_home = "login.php"
        self.params = {
            "username" : username,
            "password" : password,
        }
        self.userinfo = {}
        self.result = []
        self.type_list = ['c_anime','c_doc','c_elearning','c_games','c_hqaudio','c_movies','c_mv','c_sports','c_tvseries']

    def set_user(self,username,password):
        self.params["username"] = username
        self.params["password"] = password

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
            try:
                self.get_userinfo()
                self.is_login = True
                return True
            except:
                return False
            
    
    def login_with_img(self):
        r = requests.get(self.url + self.login_home)
        soup = BeautifulSoup(r.text,"html.parser")

        img = soup.find("img",{"alt" : "CAPTCHA"}).get("src")
        self.imghash = img.split("=")[-1]

        return self.url + "image.php?action=regimage&imagehash=" + self.imghash
    
    def search(self,name):
        if self.cookie == None:
            return None
        raw_data = self.search_raw(name)
        if raw_data == None:
            return []
        data = []
        id = 0
        for i in raw_data:
            content = self.process_raw_data(i)
            content["id"] = id
            id += 1
            data.append(content)
        
        self.result = data
        
        return data
    
    def login(self,captcha = None):
        return self.simple_login()

    def get_raw_data(self,url,params):
        r = requests.get(
            url,
            cookies = self.cookie,
            params = params,
            headers = {
                "Content-Type" : "application/x-www-form-urlencoded",
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
            }
            )

        content = r.content.decode("utf-8")
        soup = BeautifulSoup(content, "html.parser")

        return soup
    
    def search_raw(self,name):
        torrents = []
        page = 0

        while True:
            try:
                result = self.get_page(name,page)
                if len(result) == 0:
                    break
                torrents += result
                page += 1
            except:
                return None
            
        
        return torrents
    
    def get_userinfo(self):
        r = requests.get(
            self.url + 'index.php',
            cookies = self.cookie,
            headers = {
                "Content-Type" : "application/x-www-form-urlencoded",
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
            }
        )

        soup = BeautifulSoup(r.text,"html.parser")
        block = list(soup.find("table",{"id" : "info_block"}).stripped_strings)
        self.process_raw_userinfo(block)

    def process_raw_userinfo(self):
        pass
    
    def logout(self):
        self.is_login = False