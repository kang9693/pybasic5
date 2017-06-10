#!/usr/bin/python
from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib
import requests
import threading

def step2():
	file = open('output.html', 'w+')
	file.close()
	# links already added
	visited = set()
	visited_emails = set()
	scrape_page(visited, visited_emails, 'https://www.google.com', 2)

	print('Webpages \n')
	for w in visited:
		print(w)

	print('Emails \n')
	for e in visited_emails:
		print(e)

# Run recursively
def scrape_page(visited, visited_emails, url, depth):

	if depth == 0:
		return

	#website = urllib.urlopen(url)
	r = requests.get("http://www.google.com")
	website = r.text 
	#soup = BeautifulSoup(website, parseOnlyThese=SoupStrainer('a', email=False))
	soup = BeautifulSoup(website,'lxml')
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", str(website))
	#print(emails)
		
	first = str(website).split('mailto:')
	for i in range(1, len(first)):
		print(first.split('>')[0])

	for email in emails:
		if email not in visited_emails:
			print('- got email ' + email)
			visited_emails.add(email)


	for link in soup:
		if link.has_attr('href'):
			if link['href'] not in visited:
				if link['href'].startswith('https://www.google.com'):
					visited.add(link['href'])
					scrape_page(visited, visited_emails, link['href'], depth - 1)

def main():
	step2()

main()
