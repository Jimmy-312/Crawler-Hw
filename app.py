from pt_search.byr import byr_scraper
from pt_search.nexushd import nexushd_scraper
from pt_search.tju import tju_scraper
from flask import Flask, render_template, request

# with open("user.txt","rb") as f:
#     content = f.read().decode("utf-8")
#     content = content.split(",")
#     username,password = content[0],content[1]

# name = "Star Wars"
# cookies = {'c_secure_login': 'bm9wZQ%3D%3D', 'c_secure_pass': 'd6f9a894c9ed69b974c22e6609b547d5', 'c_secure_ssl': 'eWVhaA%3D%3D', 'c_secure_tracker_ssl': 'eWVhaA%3D%3D', 'c_secure_uid': 'MzQ4NzY1'}
# nexushd = nexushd_scraper(username,"@0312aaa")
# nexushd.login()

# result = nexushd.search(name)
# print(result[0])

# byr = byr_scraper(username,password,cookie=cookies)
# # byr.login()
# res = byr.search(name)
# print(res[0])

# tju = tju_scraper(username,password)
# tju.login()
# res = tju.search(name)
# print(res[1])

app = Flask(__name__)

nexushd = nexushd_scraper()
byr = byr_scraper()
tju = tju_scraper()

@app.route("/")
def index():
    url = byr.login_with_img()
    print(url)
    return render_template("index.html",url = url)

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    webtype = request.form.get("type")

    if webtype == "nexushd":
        nexushd.set_user(username,password)
        nexushd.login()
        nexushd.get_userinfo()  
        print(nexushd.userinfo)
    elif webtype == "byr":
        captcha = request.form.get("captcha")
        byr.set_user(username,password)
        byr.login(captcha)
        byr.get_userinfo()
        print(byr.userinfo)
    elif webtype == "tju":
        tju.set_user(username,password)
        tju.login()
        tju.get_userinfo()
        print(tju.userinfo)

    return render_template("index.html")

@app.route("/search")
def search():
    name = request.args.get("name")
    print(name)  
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5555)