from nexushd import nexushd_scraper
name = "Star Wars"

with open("user.txt","rb") as f:
    content = f.read()
    content = content.split(",")
    username,password = content[0],content[1]

nexushd = nexushd_scraper()
nexushd.login(username,password)

result = nexushd.search(name)
print(result[0])