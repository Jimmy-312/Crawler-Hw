from pt_search.byr import byr_scraper
from pt_search.nexushd import nexushd_scraper
from pt_search.tju import tju_scraper
from flask import Flask, jsonify, request
from flask_cors import CORS

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
CORS(app)

nexushd = nexushd_scraper()
byr = byr_scraper()
tju = tju_scraper()

@app.route("/captcha")
def index():
    url = byr.login_with_img()
    return url

@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    webtype = data["type"]
    userinfo = {}

    if webtype == "nexushd":
        nexushd.set_user(username,password)
        if not nexushd.login():
            return "fail"
        nexushd.get_userinfo()  
        userinfo = nexushd.userinfo
    elif webtype == "byr":
        captcha = request.form.get("captcha")
        byr.set_user(username,password)
        if not byr.login(captcha):
            return "fail"
        byr.get_userinfo()
        userinfo = byr.userinfo
    elif webtype == "tju":
        tju.set_user(username,password)
        if not tju.login():
            return "fail"
        tju.get_userinfo()
        userinfo = tju.userinfo

    return userinfo

@app.route("/search")
def search():
    name = request.args.get("name")
    nexushd.search(name) 
    print(nexushd.result)
    return jsonify(nexushd.result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5555)