from pt_search.byr import byr_scraper
from pt_search.nexushd import nexushd_scraper
from pt_search.tju import tju_scraper
from flask import Flask, jsonify, request
from flask_cors import CORS
from itertools import chain, zip_longest


app = Flask(__name__)
CORS(app)

nexushd = nexushd_scraper()
byr = byr_scraper()
tju = tju_scraper()

scraper_list = [nexushd,byr,tju]

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
    captcha = data["captcha"]
    userinfo = {}

    if webtype == "nexushd":
        userinfo = get_userinfo(username,password,captcha,nexushd)
    elif webtype == "byr":
        userinfo = get_userinfo(username,password,captcha,byr)
    elif webtype == "tju":
        userinfo = get_userinfo(username,password,captcha,tju)

    return jsonify(userinfo)

def get_userinfo(username,password,captcha,scraper):
    scraper.set_user(username,password)
    if not scraper.login(captcha):
        return "fail"
    
    return scraper.userinfo

@app.route("/search")
def search():
    name = request.args.get("name")
    results = []
    result = []
    for i in scraper_list:
        if i.is_login:
            i.search(name)
            results.append(i.result)
    for i in range(max(len(i) for i in results)):
        for j in results:
            if len(j) - 1 >= i:
                result.append(j[i])

    return jsonify(result)

@app.route("/getusers")
def getuser():
    user_list=[]
    for i in scraper_list:
        if i.is_login:
            user_list.append(i.userinfo)

    return jsonify(user_list)

@app.route("/logout",methods=["POST"])
def loginout():
    data = request.get_json()
    webtype = data["type"]
    if webtype == "NexusHD":
        nexushd.logout()
    elif webtype == "BYRPT":
        byr.logout()
    elif webtype == "TJUPT":
        tju.logout()
    return "success"

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5555)