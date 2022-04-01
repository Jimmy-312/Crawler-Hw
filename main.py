from nexushd import nexushd_scraper

with open("user.txt","rb") as f:
    content = f.read().decode("utf-8")
    content = content.split(",")
    username,password = content[0],content[1]

name = "Star Wars"

nexushd = nexushd_scraper()
nexushd.login(username,password)

result = nexushd.search(name)
print(result[0])