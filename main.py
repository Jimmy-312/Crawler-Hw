from byr import byr_scraper
from nexushd import nexushd_scraper

with open("user.txt","rb") as f:
    content = f.read().decode("utf-8")
    content = content.split(",")
    username,password = content[0],content[1]

name = "Star Wars"
cookies = {'c_secure_login': 'bm9wZQ%3D%3D', 'c_secure_pass': 'd6f9a894c9ed69b974c22e6609b547d5', 'c_secure_ssl': 'eWVhaA%3D%3D', 'c_secure_tracker_ssl': 'eWVhaA%3D%3D', 'c_secure_uid': 'MzQ4NzY1'}
# nexushd = nexushd_scraper(username,"@0312aaa")
# nexushd.login()

# nexushd.get_page(name,0)
# result = nexushd.search(name)
# print(result[0])

byr = byr_scraper(username,password,cookie=cookies)
# byr.login()
res = byr.search(name)
print(res[0])