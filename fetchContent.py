import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import html5lib
import pandas as pd

storyText = []
chapters = []
# name the file with the ID
# dump the text in a text file

def getFanFic():
    df = pd.read_csv('HPSummaryTrim.csv')
    links = df["link"]
    for oglink in links:
        req = requests.get(oglink)
        bsObj = BeautifulSoup(req.content, 'html.parser')
        chapters = bsObj.find("select", {"name":"chapter"})
        options = chapters.findAll("option")
        for option in options:
            option = option.attrs['value']
            chapters.append(option)
        for chapter in chapters:
            partial = ("/%s/") % (chapter)
            link = oglink.replace("/1/", partial)
            req = requests.get(link)
            content = bsObj.find("div", {"class":"storytext xcontrast_txt nocopy"}).get_text()
            storyText.append(content)
        storyID = oglink.replace("https://www.fanfiction.net/s/", "")
        storyID = storyID.split("/")
        storyID = str(storyID[0])
        with open('%s.txt' % storyID, 'w') as outfile:
            outfile.write("\n".join(storyText))



        # https://www.fanfiction.net/s/12611836/1/What-Nobody-Says
        # self.location='/s/12611836/3/What-Nobody-Says'
        # self.location='/s/12611836/4/What-Nobody-Says'

getFanFic()
