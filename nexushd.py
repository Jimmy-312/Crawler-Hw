import requests
from bs4 import BeautifulSoup

class nexushd_scraper:
    def __init__(self,cookie = None):
        self.cookie = cookie
        self.url = 'http://nexushd.org/'
    
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

    def process_raw_data(self,html):
        title = html.find("td",{"class" : "embedded"})
        types = html.find("img").get("title")
        full_name = title.find("a").get("title")
        href = title.find("a").get("href")
        title.a.decompose()
        if title.b != None:
            title.b.decompose()
        description = title.get_text()

        raw_loc = html.find("table",{"class" : "torrentname"}).parent.next_sibling.next_sibling
        time = raw_loc.find("span").get("title")

        raw_loc = raw_loc.next_sibling
        size = raw_loc.text

        raw_loc = raw_loc.next_sibling
        upload = raw_loc.text

        raw_loc = raw_loc.next_sibling.next_sibling
        download = raw_loc.text

        content_dict = {
            "type" : types,
            "name" : full_name,
            "description" : description,
            "time" : time,
            "size" : size,
            "upload" : upload,
            "download" : download,
            "href" : self.url + href
        }

        return content_dict
    
    def search_raw(self,name):
        torrents = []
        page = 0

        while True:
            result = self.get_page(name,page)
            if len(result) == 0:
                break
            torrents += result
            page += 1
        
        return torrents

    def get_page(self,name,page):
        params={
            "search" : name,
            "page" : page
            }

        soup = self.get_raw_data(self.url + "torrents.php",params)
        raw = soup.find("table", {"class" : "torrents"}).contents
        result = []
        for i in raw:
            if i != "\n":
                result.append(i)
    
        return result[1:]

    def get_raw_data(self,url,params):
        r = requests.get(
            url,
            cookies = self.cookie,
            params = params
            )

        content = r.content.decode("utf-8")
        soup = BeautifulSoup(content, "html.parser")

        return soup

    def login(self,username,password):
        params = {
            "username" : username,
            "password" : password
        }

        r = requests.post(
            self.url + "takelogin.php",
            params = params,
            cookies = self.cookie,
            allow_redirects = False
            )

        self.cookie = requests.utils.dict_from_cookiejar(r.cookies)
        
        if self.cookie == None:
            return False
        else:
            return True

