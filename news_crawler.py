#-*- coding: utf-8 -*-   
import feedparser
import os
import time
import sqlite3 as sqlite
#import urllib2
# import pdb;pdb.set_trace()  <== python debug method 
import logging
import configparser

import feedparser
from urllib.request import urlopen
##import logfile

DATA_PATH = 'data'

class RSSRobot:
	def __init__(self, rssfile, savedir):
		self.rssfile = rssfile
		self.savedir = savedir
		self.CrawedUrls = 'd:\document\\test\\CrawedUrls.log'
		self.pubDate = ' '
		
		#assert os.path.exists(savedir), "save directory is not exists!"
		if not os.path.exists(savedir):
			os.makedirs(savedir)
		self.err = open(os.path.join(self.savedir, "error.log"), "a+")		
		self.news_db   = os.path.join(DATA_PATH, 'news.db')
		self.crawlurl_db   = os.path.join(self.savedir, 'crawlurl.db')
	
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
		#self.pubDate =item.published
		if item.has_key("created"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.created_parsed)
		elif item.has_key("published"): article["created"] = time.strftime("%Y-%m-%d %H:%M:%S", item.published_parsed)
		else: article["created"] = ""

		if item.has_key("updated") and (item.updated_parsed != None):
			article["updated"] = time.strftime("%Y-%m-%d %H:%M:%S", item.updated_parsed)
		article["title"] = item.title
		if item.has_key("summary"): article["summary"] = item.summary
		else: article["summary"] = ""
		return article
		
	def __readlogfile(self,CrawedUrls):   ## 로그 기록 함수
		f = open(CrawedUrls)
		logfile = f.readlines()
		f.close()
		return logfile 
		

		
		

	def __readFeeds(self):
		articles = []

		feedlist = self.__getFeeds()
		count = 1
		#urls = logfile.LogFile(os.path.join(self.savedir, "CrawedUrls.log"))
		#urls = self.__readlogfile(self.CrawedUrls)
		#print ( "urls" ,urls )
		
		
		for feed in feedlist:
			url = feed.rstrip()
			print(u"피드 파싱 중... %s(%d / %d)" %(url, count, len(feedlist)))
			try:
				f = feedparser.parse(url)
				
			except:
				self.__addError("feed parsing error - %s" %url)
			else:
				for e in f.entries:
					article = self.__feedItem(e)
					
					#print ( "article : ", article) 
					#print ( "url", url )						
					
					urls = self.CrwedurlsCheck_(article["link"])

					#urldeff(self, u, link)
					# 전에 수집한 url은 다시 수집하지 않는다.
					## 수집한 기록이 있는 url은 수집하지 않는다.
					if ( urls >= 1 ): break;     
					articles.append(article)
					
					# 수집한 url을 기록한다.
					### url.add(article["link"])
					
					## 수집한 url을 sqlite db에 insert 한다. 
					self.Crwedurls_(article["link"])
					
					#sql = self.CrwedurlsCheck_(article["link"])
					#print(sql )
					filename=self.CrawedUrls
					f = open(filename, "a")
					f.write("%s\n" %(article["link"]))
					f.close()
					#try:					
					#except:
					

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
		#savepath = "%s\\%s" %(self.savedir, time.strftime("%Y%m%d\\%H%M"))		
		#savepath = "%s\\%s" %(self.savedir, time.strftime("%Y%m%d\\%H%M"))			
		#self.__makeDir(savepath)
		#self.__makeDir(savepath)
		count = 1 
		#filename = "%s\\%d.html" % (savepath, count)	
		filename= "%s\\%s.html" % (self.savedir,time.strftime("%Y%m%d_%H%M"))
		issue =' ' 
		issue1 =' '
		for article in articles:
			count += 1
			print("%s (%d)" %(article["link"], count))		
			#print("%s" % self.pubDate)
			issue += issue1 
			issue1 = '<td style=\'width: 50%; text-align: right;\'><span id=\'p_date\'>'+ time.strftime("%Y-%m-%d %H:%M:%S")  + '</span></td></tr>    '
			issue1 = issue1 + '<tr><td colspan=\'2\' id=\'article\'>	        <A HREF=\'' + article["link"]  + '\' TARGET=\'_NewsWin1\'>' 
			issue1 = issue1 + '<STRONG>  \"' + article["title"] +'\" </STRONG></A>' # ' % (item["title"]) 
			issue1 = issue1 + '<BR>'+ article["summary"] + '(하략)</td></tr>' 
			#issue1 = issue1 + '<BR>'+ article["summary"] + '(하략)</td></tr>' 
			
			#% (item["summary"]) )										
			#print ( issue )#self.__html(article, filename, savepath)
		
		#print ( filename)
		#print(savepath,self.savedirs)
		self.__saveItemhtml(filename, issue)			
		print(u"수집종료... %s" %time.strftime("%Y-%m-%d %H:%M:%S"))
		t2 = time.time()
		print(u"소요시간... %s초" %str(t2 - t1))
		print (u"파일명 : %s" % filename)
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
		
	def Crwedurls_(self,urls):
		#self.crawlurl_db
		#no='1'
		curl=urls
		title='test'
		#conn = sqlite.connect(self.crawlurl_db)
		c = conn.cursor()
        ## sqlite db create 
		'''sqls = ('create table if not exists CrawedUrls (ID INT PRIMARY KEY NOT NULL AUTOINCREMENT , curl, title, primary key(no));'  +
				'create index if not exists CrawedUrls_code on CrawedUrls(no)')				
					
			sqls = ('CREATE TABLE  CrawedUrls(no INTEGER PRIMARY KEY AUTOINCREMENT,curl STRING');


		c.executescript(sqls)'''
		
		'''conn = sqlite3.connect(':memory:')
		c = conn.cursor()
		#c.execute(''' ##CREATE TABLE stocks
		#		(date text, trans text, symbol text, qty real, price real)''')
		'''c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',150,35.2)")
		c.execute("INSERT INTO stocks VALUES ('2006-01-06','BUY','RHAT',170,35.17)")
		conn.commit()'''
		#rows = (no, curl)
		
		sql = 'insert into CrawedUrls (curl) values (\'' + curl +'\');'
		c.execute(sql)
		conn.commit()
		conn.close()
		
	def CrwedurlsCheck_(self,urls):
		#self.crawlurl_db
		#no='1'
		curl=urls
		title='test'
		conn = sqlite.connect(self.crawlurl_db)
		c = conn.cursor()
		sql = 'select count(*) from CrawedUrls where  curl =\'' + urls + '\' ' + 'Order by no asc limit 1;' 
		c.execute(sql)
		for row in c:
			c = row 
		urls=c[0]
		conn.commit()
		conn.close()
		
		
		return urls
		
if __name__ == "__main__":
	robot = RSSRobot("d:\document\\test\\blog.txt", "d:\document\\test")
	robot.html()
	#robot.CrwedurlsCheck_('http://www.boannews.com/media/view.asp?idx=50437&kind=&sub_kind=')	
	#robot.Crwedurls_(1)	
	#robot.urldeff('http://www.etnews.com/20160427000076')

