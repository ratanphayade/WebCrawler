import re, urllib
from sets import Set
myurl = "http://localhost/pro/CityCenter/"
MAXCOUNT = 10
count = 0
URLpattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
def crawl_function (url, maxlevel, pattern):
    if (maxlevel == 0):
        return
    results = []
    for i in re.findall(pattern, urllib.urlopen(url).read(), re.I):
        if (len(results) > MAXCOUNT):
            for j in results:
                print j
            return
        results.append(i)
    for i in results:
        crawl_function (i, maxlevel - 1, pattern)
crawl_function(myurl, 2, URLpattern)