from pt_search.scraper import scraper

class nexushd_scraper(scraper):
    def __init__(self,username = None,password = None,cookie = None):
        super(nexushd_scraper,self).__init__(username,password,cookie)
        self.url = 'http://nexushd.org/'

    def process_raw_data(self,html):
        title = html.find("td",{"class" : "embedded"})
        types = html.find("img").get("title")
        css_type = html.find("img").get("class")[0]
        if css_type not in self.type_list:
            css_type = 'c_other'
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
            "source" : "NexusHD",
            "type" : types,
            "csstype" : css_type,
            "name" : full_name,
            "description" : description,
            "time" : time,
            "size" : size,
            "upload" : upload,
            "download" : download,
            "detail" : self.url + href,
            "href" : self.url + "download.php?" + href.split("?")[-1].split("&")[0]
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
    
    def process_raw_userinfo(self,block):
        name = block[1]
        credit = block[14][3:]
        ratio = block[20]
        upload = block[22]
        download = block[24]
        
        self.userinfo = {
            "Name" : name,
            "Credit" : credit,
            "Ratio" : ratio,
            "Upload" : upload,
            "Download" : download,
            "Type" : "NexusHD"
        }




