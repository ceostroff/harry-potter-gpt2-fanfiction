import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import html5lib
import pandas as pd
import os
# name the file with the ID
# dump the text in a text file
# https://www.fanfiction.net/s/13672523/1/The-Slytherin-Prince
def getFanFic():
    df = pd.read_csv('HPSummary.csv')
    for row, data in df.iterrows():
        storyText = []
        link = data["link"]
        link = link.split("/1/")
        firstLink = link[0] + "/"
        lastLink = "/" + link[1]
        chapterTotal = int(data["chapters"]) + 1
        startChapter = 1
        storyID = data["link"].replace("https://www.fanfiction.net/s/", "")
        storyID = storyID.split("/")
        storyID = str(storyID[0])
        for i in range(startChapter, chapterTotal):
            link =  firstLink + str(i) + lastLink
            req = requests.get(link)
            bsObj = BeautifulSoup(req.content, 'html.parser')
            try:
                content = bsObj.find("div", {"class":"storytext xcontrast_txt nocopy"}).get_text()
                storyText.append(content)
            except AttributeError:
                print("Something went wrong with ID: " + storyID)
        rating = data["rating"]
        dirName = rating.lower().replace(": ", "-")
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        with open('%s/%s.txt' % (dirName, storyID), 'w') as outfile:
            outfile.write("\n".join(storyText))
getFanFic()
