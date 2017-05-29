#-*- coding: utf-8 -*-
import feedparser
import os
import time
import sqlite3 as sqlite
#import urllib2

import feedparser
from urllib.request import urlopen
#import logfile

DATA_PATH = 'data'

class RSSRobot:
	def __init__(self, rssfile, savedir):
		self.rssfile = rssfile
		self.savedir = savedir
		#assert os.path.exists(savedir), "save directory is not exists!"
		if not os.path.exists(savedir):
			os.makedirs(savedir)
		self.err = open(os.path.join(self.savedir, "error.log"), "a+")		
		self.news_db   = os.path.join(DATA_PATH, 'news.db')
	
	def __del__(self):
		self.err.close()
		
	    # 에외가 발생하면 예외가 발생한 link를 로그에 기록한다.
	def __addError(self, msg):
		self.err.write("[%s]%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S"), msg))
		
	# 파일에서 피드 url 목록을 받아온다.
	def __getFeeds(self):
		f = open(self.rssfile)
		feeds = f.readlines()
		f.close()
		return feeds
		
	def __feedItem(self, item):
		article = {}
		article["link"] = item.link		
		#article["published"] = item.published
		if item.has_key("created"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.created_parsed)
		elif item.has_key("published"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.published_parsed)
		else: article["created"] = ""

		if item.has_key("updated") and (item.updated_parsed != None):
			article["updated"] = time.strftime("%Y-%m-%d %H:%M:%S", item.updated_parsed)
		article["title"] = item.title
		if item.has_key("summary"): article["summary"] = item.summary
		else: article["summary"] = ""
		return article

	def __readFeeds(self):
		articles = []

		feedlist = self.__getFeeds()
		count = 1
		urls = logfile.LogFile(os.path.join(self.savedir, "CrawedUrls.log"))
		
		for feed in feedlist:
			url = feed.rstrip()
			print(u"피드 파싱 중... %s(%d / %d)" %(url, count, len(feedlist)))
			try:
				f = feedparser.parse(url)
				#print(f[feed][title]) 
			except:
				self.__addError("feed parsing error - %s" %url)
			else:
				for e in f.entries:
					article = self.__feedItem(e)
					#print ( "article : ", article) 
					# 전에 수집한 url은 다시 수집하지 않는다.
					#if url.isExists(article["link"]): break
					articles.append(article)
					# 수집한 url을 기록한다.
					#url.add(article["link"])

			count += 1

		return articles

    # url의 내용을 받아온다.
	def __getURLContent(self, url):
		time.sleep(self.delay)
		try:
			content = urllib.urlopen(url).read()
			return content
		except:
			self.__addError("__getURLContent error - %s" %url)
			return ""
			
	def __news_data(self):
		print( test )

    ## 피드 아이템 정보를 파일로 저장한다.
	def __saveItem(self, item, filename):
		f = open(filename, "w")
		try:
			f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
			f.write("<Document>\n")
			f.write("<Document.URL> %s </Document.URL>\n" %(item["link"]))
			print (item["link"])
			f.write("<Document.Date> %s </Document.Date>\n" %(item["created"]))
			#f.write("<Document.Title> %s </Document.Title>\n" %(self.__encode(item["title"])))
			f.write("<Document.Title> %s </Document.Title>\n" %(item["title"]))
			print ( item["title"])
			f.write("<Document.Summary> %s </Document.Summary>\n" %(item["summary"]))
			print ( item["summary"])
			content = self.__getURLContent(item["link"])
			f.write("<Document.Contents> %s </Document.Contents>\n" %(content))
			f.write("</Document>")			
		except:
			print(item["link"])
			self.__addError(item["link"])
		f.close()
	
	def __saveItemhtml(self, filename, issue):
		f = open(filename, "w")
		try:
			f.write('<html><head>\n')
			f.write('<meta http-equiv=\'Content-Type\' content=\'text/html;\'><title>정보보호 뉴스 클리핑</title>')
			f.write('<style type=\'text/css\'>')
			f.write('<!--			body, table, input, textarea {			font:12px NanumGothic, Tahoma;			color:#555;			margin:0px;	')
			f.write('line-height:150%;			}			a:link, a:visited { color : #000000; text-decoration: none; }')
			f.write('a:hover { color : #369;	text-decoration: underline;	}						#main {			overflow:hidden;	')
			f.write('border: 1px solid #CCCCCC;			position: relative;			z-index: auto;			}					')
			f.write('#contents {			width:680px;			float:left;			}						#mainShadow {		')
			f.write('background-color: #F0F0F0;			}			#p_date {			font:10px NanumGothic, Verdana;		')
			f.write('letter-spacing:-1px;			padding-right:10px;			color: #FFFFFF;			margin-top: -21px;	')
			f.write('text-align: right;			}			#p_info {			font:11px/120% NanumGothic, 돋움;		')
			f.write('color:#777;			margin-left: 8px;			padding-top: 6px;			margin-top: 5px;		')
			f.write('text-align: right;			}						#mainInsideBox {			padding: 16px;		')
			f.write('border: 1px solid #FFFFFF;			border:0 !important;			}						#head_title {	')
			f.write('color:#FFFFFF;			word-spacing:4px;			background-color:#cc3300;			padding: 4px 100px 3px 8px;	')
			f.write('margin-bottom: 4px;			font:14px NanumGothic, 돋움체;			}						#writer {		')
			f.write('color: #FFFFFF;			text-align: right;			}			#article {		')
			f.write('line-height:180%;			padding:20px 10px;			word-break:break-all;	')
			f.write('text-align: justify;			clear: both;			margin-top: 4px;			overflow: hidden;	')
			f.write('width:600px;			}						#article blockquote {			border-left: 7px double #ccc;		')
			f.write('margin: 10px 10px 10px 20px;			padding-left: 10px;			word-break:break-all;				}		')
			f.write('#article a:link, .article a:visited {			color:#0066CC;			border-bottom: 1px dashed;			')
			f.write('}							#article a:hover {			color:#FF0000;			text-decoration:none;			}		')
			f.write('#p_body {			margin-left:20px;			margin-top:20px;} --></style>')
			f.write('</head>')
			f.write('</head>')
			
			f.write('<body id=\'p_body\'><table id=\'contents\' cellpadding=\'0\' cellspacing=\'0\'><tr><td><table id=\'mainShadow\' cellpadding=\'0\' cellspacing=\'0\'><tr><td>')  
			f.write('<table id=\'main\' cellpadding=\'0\' cellspacing=\'0\'><tr><td><table id=\'mainInsideBox\' cellpadding=\'0\' cellspacing=\'0\'><tr><td>')
			f.write('<table cellpadding=\'0\' cellspacing=\'0\'><tbody>')
			f.write('<tr style=\'background: #cc3300; height: 30px;\'><td style=\'width: 50%; text-align: left;\'>')
			f.write('<span id=\'head_title\'><STRONG>정보보호 뉴스클리핑</STRONG></span></td>')
			#f.write('<td style=\'width: 50%; text-align: right;\'><span id=\'p_date\'> 2016-04-22 03:43:21</span></td></tr>    ')
			#f.write('<tr><td colspan=\'2\' id=\'article\'>	        <A HREF=\' %s \' TARGET=\'_NewsWin1\'>	' % (item["link"]) )
			#f.write('<STRONG>  "%s"  </STRONG></A>	      ' % (item["title"]))
			#f.write('<BR>  %s (하략)</td></tr>     	' % (item["summary"]) )		
			f.write(issue)
			f.write('</tbody></table></td></tr></table>')    
			f.write('</td></tr></table></td></tr></table></td></tr>')
			f.write('</table>')			
			f.write("</html>")					
			
		except:
			print(item["link"])
			self.__addError(item["link"])
		f.close()
		
	def html(self, delay=1):
		#f = open(filename, "w")
		#articles = self.__readFeeds() 
		self.delay = delay
		print(u"수집시작... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t1 = time.time()
		articles = self.__readFeeds()
		count = 0
		savepath = "%s\\%s" %(self.savedir, time.strftime("%Y%m%d\\%H%M"))
		self.__makeDir(savepath)
		#self.__makeDir(savepath)
		count = 1 
		filename = "%s\\%d.html" %(savepath, count)	
		issue =' ' 
		issue1 =' '
		for article in articles:
			count += 1
			print("%s (%d)" %(article["link"], count))								
			issue += issue1 
			issue1 = '<td style=\'width: 50%; text-align: right;\'><span id=\'p_date\'>'+ 'test' + '</span></td></tr>    '
			issue1 = issue1 + '<tr><td colspan=\'2\' id=\'article\'>	        <A HREF=\'' + article["link"]  + '\' TARGET=\'_NewsWin1\'>' 
			issue1 = issue1 + '<STRONG>  \"' + article["title"] +'\"  </STRONG></A>' # ' % (item["title"]) 
			issue1 = issue1 + '<BR>'+ article["summary"] + '(하략)</td></tr>     	' #% (item["summary"]) )							
			
			print ( issue )#self.__html(article, filename, savepath)
			
		self.__saveItemhtml(filename, issue)			
		print(u"수집종료... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t2 = time.time()
		print(u"소요시간... %s초" %str(t2 - t1))
		#issue 
		
		
	
	def __encode(self, text):
		return text.encode('utf8')		

    ## RSS 문서를 저장할 디렉토리(yyyymmdd\hhmm)를 생성한다.
	def __makeDir(self, dir):
		if not os.path.exists(dir):
			os.makedirs(dir)

	def execute(self, delay=1):
		self.delay = delay
		print(u"수집시작... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t1 = time.time()
		articles = self.__readFeeds()
		count = 0
		savepath = "%s\\%s" %(self.savedir, time.strftime("%Y%m%d\\%H%M"))
		self.__makeDir(savepath)
		for article in articles:
			count += 1
			print("%s (%d)" %(article["link"], count))
			filename = "%s\\%d.xml" %(savepath, count)
			self.__saveItem(article, filename)
			self.__html(article,filename)
			
			
		print(u"수집종료... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t2 = time.time()
		print(u"소요시간... %s초" %str(t2 - t1))
		
	def executehtml(self, delay=1):
		self.delay = delay
		print(u"수집시작... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t1 = time.time()
		articles = self.__readFeeds()
		count = 0
		savepath = "%s\\%s" %(self.savedir, time.strftime("%Y%m%d\\%H%M"))
		self.__makeDir(savepath)
		for article in articles:
			count += 1
			print("%s (%d)" %(article["link"], count))
			filename = "%s\\%d.html" %(savepath, count)			
			#self.__html(article, filename, savepath)			
			issue = '<td style=\'width: 50%; text-align: right;\'><span id=\'p_date\'>' + self.item["pubDate"] + '</span></td></tr>    '
			issue = issue + '<tr><td colspan=\'2\' id=\'article\'>	        <A HREF=\'' + self.item["link"]  + '\' TARGET=\'_NewsWin1\'>' 
			issue = issue + '<STRONG>  \"' + self.item["title"] +'\"  </STRONG></A>' # ' % (item["title"]) 
			issue = issue + '<BR>'+ self.item["summary"] + '(하략)</td></tr>     	' #% (item["summary"]) )		
			#print ( issue )
		
		self.__saveItemhtml(self, filename, issue)
		print(u"수집종료... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t2 = time.time()
		print(u"소요시간... %s초" %str(t2 - t1))
		
		
if __name__ == "__main__":
	robot = RSSRobot("d:\document\\test\\blog.txt", "d:\document\\test")
	robot.html()


'''for i in range(0,count):
	#print ( d[i]['feed']['subtitle'])
	print ( i )
	print ( d['feed']['subtitle'] )
	print ( d.feed.subtitle )
	'''
'''
class RSSRobot:
	def __init__(self, rssfile, savedir):
		#self.rssfile = rssfile
		self.savedir = savedir
		#assert os.path.exists(savedir), "save directory is not exists!"
		if not os.path.exists(savedir):
			os.makedirs(savedir)
		self.err = open(os.path.join(self.savedir, "error.log"), "a+")

	def __del__(self):
		self.err.close()

    # 에외가 발생하면 예외가 발생한 link를 로그에 기록한다.
	def __addError(self, msg):
		self.err.write("[%s]%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S"), msg))

    # 파일에서 피드 url 목록을 받아온다.
	def __getFeeds(self):
		f = open(self.rssfile)
		feeds = f.readlines()
		f.close()
		return feeds

    # 피드의 아이템 정보를 사전 형식으로 돌려준다.
	def __feedItem(self, item):
		article = {}
		article["link"] = item.link
		if item.has_key("created"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.created_parsed)
		elif item.has_key("published"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.published_parsed)
		else: article["created"] = ""

		if item.has_key("updated") and (item.updated_parsed != None):
			article["updated"] = time.strftime("%Y-%m-%d %H:%M:%S", item.updated_parsed)
		article["title"] = item.title
		if item.has_key("summary"): article["summary"] = item.summary
		else: article["summary"] = ""
		return article



if __name__ == "__main__":
	robot = RSSRobot("d:\document\\test\\blog.txt", "d:\document\\test")
	robot.execute()   '''