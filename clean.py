#encoding:UTF-8
import os
import re
import sys
from bs4 import BeautifulSoup
from urllib import request

def getHtml(url):
	htmlDoc = request.urlopen(url).read()
	htmlDoc = htmlDoc.decode('UTF-8')
	return htmlDoc

def removeScript(soup):
	for script in soup.find_all('script'):
		script.decompose()
	return soup

def removeSegmentFaultTag(soup):
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
		if not meta.has_attr('charset'):
			meta.decompose()
	for meta in soup.findAll('link'):
        	meta.decompose()
	return soup

def removeJobboleTag(soup):
	nav_classes = ["menu-nav", "grid-12 menu-nav"]
	for navclass in nav_classes:
		nav = soup.find("nav", {"class": navclass})
		if nav is not None:
			nav.decompose()
	div_classes = ["header-wrapper", "grid-4", "wp_rp_wrap wp_rp_plain",
	"dot-box center-align", "author-bio-info", "navigation margin-20",
	"post-adds", "comments", "entry-meta", "copyright-area", "crayon-toolbar", "crayon-main"]
	for divclass in div_classes:
		for div in soup.findAll("div", {"class": divclass}):
			div.decompose()
	div = soup.find("div", {"id": "full-btm"})
	div.decompose()
	div = soup.find("div", {"id": "full-top"})
	if div is not None:
		div.decompose()
	div = soup.find("div", {"id": "author-bio"})
	if div is not None:
		div.decompose()
	div = soup.find("div", {"id": "rewardbox"})
	if div is not None:
		div.decompose()
	div = soup.find("div", {"id": "breadcrumb"})
	div.decompose()
	div = soup.find("div", {"style": "text-align: left;"})
	div.decompose()
	blockquote = soup.find("blockquote", {"class": "rewards"})
	if blockquote is not None:
		blockquote.decompose()
	footer = soup.find("footer")
	footer.decompose()
	style = soup.find("style")
	style.decompose()
	for textwidget in soup.findAll("div", {"class": "textwidget"}):
		textwidget.decompose()
	for meta in soup.findAll('link'):
		meta.decompose()
	return soup

def removeInfoQCN(soup):
	div_ides = ["topInfo", "header", "contentRatingWidget", "comment_here", "footer",
	"forceUpdate_inline", "replyPopup", "id_geo_banner", "forceProfileUpdateArea", "overlay_comments",
	"editCommentPopup", "messagePopup", "responseContent"]
	for divid in div_ides:
		for div in soup.findAll("div", {"id": divid}):
			div.decompose()
	div_classes = ["related_sponsors visible stacked", "random_links", "clear", "comments",
	"all_comments", "newsletter ", "bottomContent", "login_overlay", "article_page_right",
	"related_sponsors relEdRelRes", "intbt", "related_sponsors wholething"]
	for divclass in div_classes:
		for div in soup.findAll("div", {"class": divclass}):
			div.decompose()
	span = soup.find("span", {"class": "author_general"})
	if span is not None:
		span.decompose()
	a = soup.find("a", {"class": "comments_like"})
	if a is not None:
		a.decompose()
	ul = soup.find("ul", {"class": "sh_t"})
	if ul is not None:
		ul.decompose()
	for meta in soup.findAll('link'):
		meta.decompose()
	return soup

def removeITEBlog(soup):
	div_classes = ["navbar", "banner banner-site", "speedbar", "tongji", "QRcode", "comt-title", "relates",
	"widget widget_text", "no_webshot", "article-social", "related_top", "banner banner-related", "banner banner-comment",
	"announcement", "meta", "no_bullets"
	]
	for divclass in div_classes:
		for div in soup.findAll("div", {"class": divclass}):
			div.decompose()
	div_ides = ["postcomments"]
	for divid in div_ides:
		for div in soup.findAll("div", {"id": divid}):
			div.decompose()
	for header in soup.findAll("header", {"class": "header"}):
		header.decompose()
	aside = soup.find("aside")
	if aside is not None:
		aside.decompose()
	nav = soup.find("nav")
	if nav is not None:
		nav.decompose()
	span = soup.find("span", {"style": "margin-top: 15px; color:red; display:block;text-align:center;"})
	if span is not None:
		span.decompose()
	for footer in soup.findAll("footer"):
		footer.decompose()
	return soup

def removeTag(soup, tagname, attribute_name, atribute_value_array):
	for attribute_value in atribute_value_array:
		for tag in soup.findAll(tagname, {attribute_name : attribute_value}):
			tag.decompose()
	return soup

def removeIBMTag(soup):
	soup = removeTag(soup, "div", "class", 
		["dw-home-band", "ibm-access", "ibm-col-6-2 dw-toc-margin", "dw-footer-columns", "ibm-col-6-2",
	        "ibm-container ibm-alternate ibm-buttons-last", "ibm-common-overlay", "ibm-no-print", "metavalue"])
	soup = removeTag(soup, "div", "id", 
		["dw-masthead-top-row", "ibm-masthead", "ibm-footer-module-dwwrapper", "ibm-footer", "ibm-metrics"])
	soup = removeTag(soup, "ul", "class", ["ibm-portrait-module-list"])
	soup = removeTag(soup, "ul", "id", ["ibm-navigation-trail"])
	soup = removeTag(soup, "h2", "class", ["ibm-alternate-rule ibm-no-print"])
	soup = removeTag(soup, "p", "class", ["ibm-ind-link ibm-back-to-top"])
	return soup

if len(sys.argv) < 2:
    sys.stderr.write('Usage: clean [url] ')
    sys.exit(1)

url = sys.argv[1]
htmlDoc = getHtml(url)
soup = BeautifulSoup(htmlDoc, "lxml")
soup = removeScript(soup)
if "segmentfault.com" in url:
	soup = removeSegmentFaultTag(soup)
elif "jobbole.com" in url:
	soup = removeJobboleTag(soup)
elif "www.infoq.com/cn" in url:
	soup = removeInfoQCN(soup)
elif "iteblog" in url:
	soup = removeITEBlog(soup)
elif "www.ibm.com/developerworks" in url:
	soup = removeIBMTag(soup)

html = soup.prettify("utf-8")

with open("output.html", "wb") as file:
    file.write(html)
