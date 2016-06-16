import os
import re
from bs4 import BeautifulSoup


htmlDoc = open('index.html',"r+")
soup = BeautifulSoup(htmlDoc, "lxml")
for script in soup.find_all('script'):
    script.decompose()

div = soup.find("div", {"class": "col-md-4"})
div.decompose()
div = soup.find("div", {"class": "clearfix mt10"})
div.decompose()
div = soup.find("div", {"class": "widget-box"})
div.decompose()
div = soup.find("div", {"class": "recommend-post"})
div.decompose()
div = soup.find("div", {"class": "text-center mt10"})
div.decompose()
div = soup.find("div", {"class": "global-navTags"})
div.decompose()
div = soup.find("div", {"class": "post-topheader custom-"})
div.decompose()
div = soup.find("div", {"class": "global-nav sf-header"})
div.decompose()
div = soup.find("div", {"class": "app-promotion-bar"})
div.decompose()
div = soup.find("div", {"id": "fixedTools"})
div.decompose()
div = soup.find("div", {"class": "widget-comments hidden"})
div.decompose()
div = soup.find("div", {"class": "modal"})
div.decompose()
div = soup.find("div", {"class": "hidden widget-register widget-welcome-question mt20 hidden-xs widget-welcome widget-register-slideUp"})
div.decompose()
div = soup.find("div", {"class": "modal widget-911"})
div.decompose()
div = soup.find("div", {"class": "col-xs-12 col-md-3 side"})
div.decompose()
footer = soup.find("footer", {"id": "footer"})
footer.decompose()
img = soup.find('img', {'id' : 'icon4weChat'})
img.decompose()
img = soup.find('img', {'id' : 'icon4weChat'})
img.decompose()
discuss = soup.find('h2', {'class' : 'h4 post-comment-title'})
discuss.decompose()
for meta in soup.findAll('meta'):
	meta.decompose()
for meta in soup.findAll('link'):
        meta.decompose()
html = soup.prettify("utf-8")

with open("output.html", "wb") as file:
    file.write(html)
