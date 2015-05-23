from bs4 import BeautifulSoup
from sets import Set
import urllib2
import re

# Function to crawl the WebSite
def crawlWeb(url,limit):
	# Getting Global Variable
	global visited_list
	# Checking For Depth Limit
	if limit==0 :
		notvisited_list.add(url)			# Storing the non visited URLs
		return
	if url not in visited_list :				# Checking whether the link is already visited
		visited_list.add(url)				# Add URL to visited Set
		try:
			print "Extracting URL : "+url
			content = urllib2.urlopen(url)		# Retrive the Content of the URL
    			soup = BeautifulSoup(content)		# Creating BeautifulSoup Object with the URL content
			for link in soup.findAll('a'):		# Retriving all the anchor tag and checking each tag for URL
				hiperLink = link.get('href')	# Retriving the href location url from anchor tag
				if hiperLink and hiperLink[0] != '#' and hiperLink[0]!='/':	# Checking for URL which are self referencing
					if re.match( r'http[s]?://.*', hiperLink , re.I) :	# Constructing the proper URL from href link
						crawlWeb(hiperLink,limit-1)
					else :
						crawlWeb(url+hiperLink,limit-1)
		except urllib2.URLError, e:		# In case the URL content can't be fetched
    			print "Error while opening this link "+url

						
visited_list = Set()		#Set which holds visited URLs
notvisited_list = Set()		#Set which holds not visited URLs

# Calling crawler Function which takes 2 values
# First Variable : URL to be crawled
# Second Variable: Depth Limit (Enter -1 for Full Crawling)

crawlWeb(raw_input("Enter the URL : "),int(raw_input("Enter the Depth Limit :")))


# Below Code Displays all Collected URLs
"""
for url in visited_list :
	print url
for url in notvisited_list :
	print url
"""
