import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import html5lib
import pandas as pd
import os

storyText = []
chapters = []
# name the file with the ID
# dump the text in a text file
# https://www.fanfiction.net/s/13672523/1/The-Slytherin-Prince
def getFanFic():
    df = pd.read_csv('HPSummary.csv')
    for row, data in df.iterrows():
        link = data["link"]
        link = link.split("/1/")
        firstLink = link[0] + "/"
        lastLink = "/" + link[1]
        chapterTotal = int(data["chapters"]) + 1
        print(chapterTotal)
        startChapter = 1
        storyID = data["link"].replace("https://www.fanfiction.net/s/", "")
        storyID = storyID.split("/")
        storyID = str(storyID[0])
        for i in range(startChapter, chapterTotal):
            link =  firstLink + str(i) + lastLink
            print(link)
            req = requests.get(link)
            bsObj = BeautifulSoup(req.content, 'html.parser')
            content = bsObj.find("div", {"class":"storytext xcontrast_txt nocopy"}).get_text()
            storyText.append(content)
        rating = data["rating"]
        dirName = rating
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        with open('dirName/%s.txt' % storyID, 'w') as outfile:
            outfile.write("\n".join(storyText))
getFanFic()
