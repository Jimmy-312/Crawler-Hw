import re
from bs4 import BeautifulSoup
from nexushd import nexushd_scraper
name = "Star Wars"
myCookies = {
            "c_secure_uid" : "MTI5NTI5",
            "c_secure_pass" : "2ab957c73f834607150ab97a7eccb864",
            "c_secure_ssl" : "bm9wZQ==",
            "c_secure_tracker_ssl" : "bm9wZQ==",
            "c_secure_login" : "bm9wZQ=="
            }

nexushd = nexushd_scraper(myCookies)
result = nexushd.search(name)
print(result)
# html = '''<tr class="twouphalfdown_bg">
# <td class="rowfollow nowrap" style="padding: 0px" valign="middle"><a href="?cat=105"><img alt="Anime" class="c_anime" src="pic/cattrans.gif" style="background-image: url(pic/category/nhd/scenetorrents/chs/catsprites.png);" title="Anime"/></a></td>
# <td align="left" class="rowfollow" width="100%"><table class="torrentname" width="100%"><tr class="twouphalfdown_bg"><td class="embedded"><br/>星球大战：幻境 | スター・ウォーズ: ビジョンズ | 日语音轨 简繁英日字幕内封</td><td class="embedded" style="text-align: right; " valign="middle" width="20"><a href="download.php?id=144617"><img alt="download" class="download" src="pic/trans.gif" style="padding-bottom: 2px;" title="下载本种"/></a><br/><a href="javascript: bookmark(144617,0);" id="bookmark0"><img alt="Unbookmarked" class="delbookmark" src="pic/trans.gif" title="收藏"/></a></td>
# </tr></table></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=144617&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2021-09-26 00:06:57">6月<br/>7天</span></td><td class="rowfollow">3.58<br/>GB</td><td align="center" class="rowfollow" title=""><b><a href="details.php?id=144617&amp;hit=1&amp;dllist=1#seeders">2</a></b></td>
# <td class="rowfollow" title=""><b><a href="details.php?id=144617&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
# <td class="rowfollow" title=""><a href="viewsnatches.php?id=144617"><b>12</b></a></td>
# <td class="rowfollow"><i>匿名</i></td>
# </tr>'''

# bp = BeautifulSoup(html,"html.parser")
# print(nexushd.process_raw_data(bp))
