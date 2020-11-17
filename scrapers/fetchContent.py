# import libraries
import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import html5lib
import pandas as pd
import os

def getFanFic():
    # open the csv with the summary data, which includes links to each post and its number of chapters
    df = pd.read_csv('HPSummary.csv')
    for row, data in df.iterrows():
        storyText = []
        link = data["link"]
        # get the link for each row
        link = link.split("/1/")
        firstLink = link[0] + "/"
        lastLink = "/" + link[1]
        chapterTotal = int(data["chapters"]) + 1
        # add on the number of chapters
        startChapter = 1
        storyID = data["link"].replace("https://www.fanfiction.net/s/", "")
        storyID = storyID.split("/")
        storyID = str(storyID[0])
        # for all of the chapters
        for i in range(startChapter, chapterTotal):
            link =  firstLink + str(i) + lastLink
            # open the link
            req = requests.get(link)
            bsObj = BeautifulSoup(req.content, 'html.parser')
            try:
                # try to get the text of the fanfiction
                content = bsObj.find("div", {"class":"storytext xcontrast_txt nocopy"}).get_text()
                storyText.append(content)
            except AttributeError:
                print("Something went wrong with ID: " + storyID)
        rating = data["rating"]
        dirName = rating.lower().replace(": ", "-")
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        # create a local text file saved under the story rating and the story id
        with open('%s/%s.txt' % (dirName, storyID), 'w') as outfile:
            outfile.write("\n".join(storyText))
# run the function
getFanFic()
