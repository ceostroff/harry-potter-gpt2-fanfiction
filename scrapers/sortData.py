import os
import glob

testData = []
trainingData = []

def getTestData():
    for file in os.listdir("rated-t"):
        i = 0
        i = i + 1
        if (i < 20) &(file.endswith(".txt")):
            path = os.path.join("rated-t", file)
            f = open(path, "r")
            text = f.read()
            text = (text + "\n " + "<|endoftext|>" + "\n ")
            testData.append(text)

def getTrainingData():
    for file in os.listdir("rated-k"):
        k = 0
        k = k + 1
        if (k < 100) &(file.endswith(".txt")):
            path = os.path.join("rated-k", file)
            f = open(path, "r")
            text = f.read()
            text = (text + "\n " + "<|endoftext|>" + "\n ")
            trainingData.append(text)

def combineTestData(testData):
    with open('test.txt', 'w') as outfile:
        outfile.write("\n".join(testData))

def combineTrainingData(trainingData):
    with open('training.txt', 'w') as outfile:
        outfile.write("\n".join(trainingData))

getTestData()
getTrainingData()
combineTestData(testData)
combineTrainingData(trainingData)
