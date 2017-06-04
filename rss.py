import feedparser
d = feedparser.parse('http://www.boannews.com/media/news_rss.xml')
print (d['feed']['title']) #< python 2.7
print (d['feed']['link'])
print (d.feed.subtitle)
# r = request.get(
#   urllib.urlopen()
#
#print(d)