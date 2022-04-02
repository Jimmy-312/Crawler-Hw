from scraper import scraper

class tju_scraper(scraper):
    def __init__(self,username,password,cookie = None):
        super(tju_scraper,self).__init__(username,password,cookie)
        self.url = 'https://tjupt.org/'
    
    def process_raw_data(self,html):
        embedded = html.find_all("td",{"class" : "embedded"})
        types = html.find("img").get("title")
        full_name = embedded[1].find("a").get("title")
        href = embedded[2].find("a").get("href")
        embedded[1].a.decompose()
        if embedded[1].b != None:
            embedded[1].b.decompose()
        description = embedded[1].get_text()

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
            "href" : self.url + href,
            "detail" : self.url + "details.php?" + href.split("?")[-1] + "&hit=1"
        }

        return content_dict

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