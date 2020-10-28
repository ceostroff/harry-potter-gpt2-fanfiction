import os
import glob


# <|endoftext|>
newtext = []

def getData1():
    for file in os.listdir("rated-t"):
        i = 0
        i = i + 1
        if (i < 10000) &(file.endswith(".txt")):
            path = os.path.join("rated-t", file)
            f = open(path, "r")
            text = f.read()
            text = (text + "\n " + "<|endoftext|>" + "\n ")
            newtext.append(text)

def getData2():
    for file in os.listdir("rated-k"):
        k = 0
        k = k + 1
        if (k < 10000) &(file.endswith(".txt")):
            path = os.path.join("rated-k", file)
            f = open(path, "r")
            text = f.read()
            text = (text + "\n " + "<|endoftext|>" + "\n ")
            newtext.append(text)

def combineData(newtext):
    with open('testdata2.txt', 'w') as outfile:
        outfile.write("\n".join(newtext))

getData1()
getData2()
combineData(newtext)
