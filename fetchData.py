import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import html5lib
import requests
summaryData = []
links = []
# csv with all the data
def getLinks():
    for i in range(1, 19785):
        print(i)
        time.sleep(1)
        url = "https://www.fanfiction.net/book/Harry-Potter/?&srt=1&lan=1&r=103&p=" + str(i)
        req = requests.get(url)
        bsObj = BeautifulSoup(req.content, 'html.parser')
        posts = bsObj.findAll("div", {"class":"z-list zhover zpointer"})
        for post in posts:
            title = post.find("a", {"class":"stitle"})
            partLink = title.get('href')
            link = "https://www.fanfiction.net/book/Harry-Potter" + partLink
            links.append(link)
            # print(link)
            summary = post.find("div", {"class":"z-indent z-padtop"}).get_text()
            infobulk = post.find("div", {"class":"z-padtop2 xgray"}).get_text()
            info = infobulk.split(" - ")
            try:
                rating = info[0]
            except:
                rating = ""
            try:
                language = info[1]
            except:
                language = ""
            try:
                genre = info[2]
            except:
                genre = ""
            try:
                chapters = info[3]
            except:
                chapters = ""
            try:
                words = info[4]
            except:
                words = ""
            try:
                reviews = info[5]
            except:
                reviews = ""
            try:
                favs = info[6]
            except:
                favs = ""
            try:
                follows = info[7]
            except:
                follows = ""
            dates = post.find("div", {"class":"z-padtop2 xgray"}).findAll("span")
            updated = dates[0].attrs['data-xutime']
            try:
                published = dates[1].attrs['data-xutime']
            except:
                published = ""
            data = {
                'title': title.get_text().strip(),
                'link': link.strip(),
                'summary': summary.strip(),
                'rating': rating.strip(),
                'language': language.strip(),
                'genre': genre.strip(),
                'chapters': chapters.strip(),
                'words': words.strip(),
                'reviews': reviews.strip(),
                'favs': favs.strip(),
                'follows': follows.strip(),
                'updated': updated.strip(),
                'published': published.strip()
            }
            # print(data)
            summaryData.append(data)


def saveData(summaryData):
    filename = 'HPSummary.csv'
    #open your new csv file with a 'w' so you can write to it
    with open(filename, 'w') as output_file:
        #make headers for you columns. these must match up with the keys you set in your python dictionary, inamte
        fieldnames = [	'title',
                      'link',
                      'summary',
                      'rating',
                      'language',
                      'genre',
                      'chapters',
                      'words',
                      'reviews',
                      'favs',
                      'follows',
                      'updated',
                      'published'
                     ]
        #write these into a csv, the headers being fieldnames and the rows your list of inmates
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summaryData)
getLinks()
saveData(summaryData)