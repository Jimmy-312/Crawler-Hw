import requests
from bs4 import BeautifulSoup

myCookies = {
    "c_secure_uid" : "MTI5NTI5",
    "c_secure_pass" : "2ab957c73f834607150ab97a7eccb864",
    "c_secure_ssl" : "bm9wZQ==",
    "c_secure_tracker_ssl" : "bm9wZQ==",
    "c_secure_login" : "bm9wZQ=="
    }

name = "Star Wars"

r = requests.get(
    "http://nexushd.org/torrents.php",
    cookies = myCookies,
    params={
        "search" : name
        },
    )

content = r.content.decode("utf-8")

soup = BeautifulSoup(content, "html.parser")
result = soup.find("table", {"class" : "torrents"}).find_all("tr")

print(result[1],result[-1])