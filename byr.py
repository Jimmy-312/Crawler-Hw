from scraper import scraper

class byr_scraper(scraper):
    def __init__(self,username,password,cookie = None):
        super(byr_scraper,self).__init__(username,password,cookie)
        self.url = 'https://byr.pt/'
    
    def login(self):
        self.login_with_img()
    
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

    def get_page(self,name,page):
        params={
            "search" : name,
            "page" : page
            }

        soup = self.get_raw_data(self.url + "torrents.php",params)
        raw = soup.find("table", {"class" : "torrents"}).find("form").contents
        result = []
        for i in raw:
            if i != "\n":
                result.append(i)
    
        return result[2:]