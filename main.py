from byr import byr_scraper
from nexushd import nexushd_scraper

with open("user.txt","rb") as f:
    content = f.read().decode("utf-8")
    content = content.split(",")
    username,password = content[0],content[1]

name = "Star Wars"

# nexushd = nexushd_scraper(username,"@0312aaa")
# nexushd.login()

# result = nexushd.search(name)
# print(result[0])

# byr = byr_scraper(username,password)
# byr.login()