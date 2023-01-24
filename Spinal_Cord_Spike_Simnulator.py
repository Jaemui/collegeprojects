#Joshua Tran, joshatra@usc.edu
#ITP 116, Spring 2022
#Final Project
#Dscription:
#This program will accept a CSV containing electrophysiology data (provided alongside the assignment) and graph
#the data based on Recording Area, Current Type, and Tetanicity. The purpose is to determine patterns within areas of
#mice spinal cord and how they respond to various types of current injections. The CSV file (Final Data.csv) containing the data is data
#recorded from an electrophysiology experiment.

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import simpledialog

def readFile(fileName):
    inputFile = open(fileName, "r")
    ephysData = {}
    # if filesize > 0:
    for line in inputFile:
        masterLis = []
        line = line.strip("\t")
        masterLis = line.strip().split(",")
        keyLis = masterLis[0] #makes the cell number and date the key of each dictionary value
        vaLis = masterLis[1:]
        ephysData[str(keyLis)]=vaLis #the rest of the data for the cell is stored under cell number
    inputFile.close()
    return ephysData

def getLongNorm(ephysData): #counts the number of Normal Activity under Long Square currents in the 6 different recording areas and puts them into a list
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbar15p+=1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbar35p+=1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbar55pM+=1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbar75p+=1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][9].strip() == "Normal Activity":
                lumbarIMM += 1
    longNormLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return longNormLis
def getLongNo(ephysData): #repeats the same process as previous function, but with No activity in long square currrents
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][9].strip() == "No Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][9].strip() == "No Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][9].strip() == "No Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][9].strip() == "No Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][9].strip() == "No Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][9].strip() == "No Activity":
                lumbarIMM += 1
    longNoLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return longNoLis

def getLongTet(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][9].strip() == "Tetanic Activity":
                lumbarIMM += 1
    longTetLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return longTetLis

def getShortNorm(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][10].strip() == "Normal Activity":
                lumbarIMM += 1
    shortNormLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return shortNormLis

def getShortNo(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][10].strip() == "No Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][1].strip() == "No Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][10].strip() == "No Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][10] .strip()== "No Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][10].strip() == "No Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][10].strip() == "No Activity":
                lumbarIMM += 1
    shortNoLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return shortNoLis

def getShortTet(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][10].strip() == "Tetanic Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][1].strip() == "Tetanic Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][10].strip() == "Tetanic Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][10].strip() == "Tetanic Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][10].strip() == "Tetanic Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][10].strip() == "Tetanic Activity":
                lumbarIMM += 1
    shortTetLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return shortTetLis

def getRampNorm(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][11].strip() == "Normal Activity":
                lumbarIMM += 1
    rampNormLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return rampNormLis

def getRampNo(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][11].strip() == "No Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][11].strip() == "No Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][11].strip() == "No Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][11].strip() == "No Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][11].strip() == "No Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][11].strip() == "No Activity":
                lumbarIMM += 1
    rampNoLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return rampNoLis


def getRampTet(ephysData):
    lumbar15p = 0
    lumbar35p = 0
    lumbar55pM = 0
    lumbar75p = 0
    lumbar105p = 0
    lumbarIMM = 0
    for key in ephysData:
        if ephysData[key][2].strip() == "Left 15p":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbar15p += 1
        if ephysData[key][2].strip() == "Left 35p":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbar35p += 1
        if ephysData[key][2].strip() == "Left 55pM":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbar55pM += 1
        if ephysData[key][2].strip() == "Left 75p":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbar75p += 1
        if ephysData[key][2].strip() == "Left 105p":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbar105p += 1
        if ephysData[key][2].strip() == "Left IMM/CeCv/105p":
            if ephysData[key][11].strip() == "Tetanic Activity":
                lumbarIMM += 1
    rampTetLis = [lumbar15p, lumbar35p, lumbar55pM, lumbar75p, lumbar105p, lumbarIMM]
    return rampTetLis

def graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,lumbarloc): #graphs specific recording area data
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    no = [longNo[choiceindex],shortNo[choiceindex],rampNo[choiceindex]]
    norm = [longNorm[choiceindex], shortNorm[choiceindex],rampNorm[choiceindex]]
    tet = [longTet[choiceindex],shortTet[choiceindex],rampTet[choiceindex]]
    br1 = np.arange(len(no))
    br2 = [x + barWidth for x in br1]
    br3 = [x+ barWidth for x in br2]
    plt.bar(br1, no, color = "r", width = barWidth,
            edgecolor = "grey", label = "No Activity")
    plt.bar(br2, norm, color="g", width=barWidth,
            edgecolor="grey", label="Normal Activity")
    plt.bar(br3, tet, color="b", width=barWidth,
            edgecolor="grey", label="Tetanic Activity")
    plt.xlabel("Current Type", fontweight = "bold", fontsize = 15) #x-axis = Current Type
    plt.ylabel("Frequency", fontweight = "bold", fontsize = 15)#y-axis = Frequency/how often the cell reacts with No/normal/tetanic activity to each current type
    plt.xticks([r + barWidth for r in range(len(no))],
               ["Long Square","Short Square","Ramp"])
    plt.title(lumbarloc) # ex: left 35p; left 55pM; etc...
    plt.legend()
    plt.show()

def graphRampType(ephysData): #graphs all frequencies of Ramp currents. X-axis: Recording locations (Left 15p, Left 35p, etc...) Y-ais: Frequency of No/normal/tetanic activity occuring for ramp type currents
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    no = [rampNo[0],rampNo[1],rampNo[2],rampNo[3],rampNo[4],rampNo[5]]
    norm = [rampNorm[0],rampNorm[1],rampNorm[2],rampNorm[3],rampNorm[4],rampNorm[5]]
    tet = [rampTet[0],rampTet[1],rampTet[2],rampTet[3],rampTet[4],rampTet[5]]
    br1 = np.arange(len(no))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    plt.bar(br1, no, color="r", width=barWidth,
            edgecolor="grey", label="No Activity")
    plt.bar(br2, norm, color="g", width=barWidth,
            edgecolor="grey", label="Normal Activity")
    plt.bar(br3, tet, color="b", width=barWidth,
            edgecolor="grey", label="Tetanic Activity")
    plt.xlabel("Recording Location", fontweight="bold", fontsize=15)
    plt.ylabel("Frequency", fontweight="bold", fontsize=15)
    plt.xticks([r + barWidth for r in range(len(no))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Ramp Current")
    plt.legend()
    plt.show()

def graphLongType(ephysData): #similar to graphRampType but with Long Square
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    no = [longNo[0],longNo[1],longNo[2],longNo[3],longNo[4],longNo[5]]
    norm = [longNorm[0],longNorm[1],longNorm[2],longNorm[3],longNorm[4],longNorm[5]]
    tet = [longTet[0],longTet[1],longTet[2],longTet[3],longTet[4],longTet[5]]
    br1 = np.arange(len(no))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    plt.bar(br1, no, color="r", width=barWidth,
            edgecolor="grey", label="No Activity")
    plt.bar(br2, norm, color="g", width=barWidth,
            edgecolor="grey", label="Normal Activity")
    plt.bar(br3, tet, color="b", width=barWidth,
            edgecolor="grey", label="Tetanic Activity")
    plt.xlabel("Recording Location", fontweight="bold", fontsize=15)
    plt.ylabel("Frequency", fontweight="bold", fontsize=15)
    plt.xticks([r + barWidth for r in range(len(no))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Long Square Current")
    plt.legend()
    plt.show()

def graphShortType(ephysData): #similar to graphRampType but with Short Sqaure
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    no = [shortNo[0],shortNo[1],shortNo[2],shortNo[3],shortNo[4],shortNo[5]]
    norm = [shortNorm[0],shortNorm[1],shortNorm[2],shortNorm[3],shortNorm[4],shortNorm[5]]
    tet = [shortTet[0],shortTet[1],shortTet[2],shortTet[3],shortTet[4],shortTet[5]]
    br1 = np.arange(len(no))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    plt.bar(br1, no, color="r", width=barWidth,
            edgecolor="grey", label="No Activity")
    plt.bar(br2, norm, color="g", width=barWidth,
            edgecolor="grey", label="Normal Activity")
    plt.bar(br3, tet, color="b", width=barWidth,
            edgecolor="grey", label="Tetanic Activity")
    plt.xlabel("Recording Location", fontweight="bold", fontsize=15)
    plt.ylabel("Frequency", fontweight="bold", fontsize=15)
    plt.xticks([r + barWidth for r in range(len(no))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Short Square Current")
    plt.legend()
    plt.show()

def graphLeft35p(ephysData): #general function that calls back the graphRecordingArea function. Used in main function
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 1
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left 35p"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)

def graphLeft15p(ephysData):
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 0
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left 15p"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)

def graphLeft55pM(ephysData):
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 2
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left 55pM"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)

def graphLeft75p(ephysData):
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 3
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left 75p"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)
def graphLeft105p(ephysData):
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 4
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left 105p"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)
def graphLeftIMM(ephysData):
    # fileName = "ephys Data.csv"
    # ephysData = readFile(fileName)
    choiceindex = 5
    longNorm = getLongNorm(ephysData)
    longNo = getLongNo(ephysData)
    longTet = getLongTet(ephysData)
    shortNorm = getShortNorm(ephysData)
    shortNo = getShortNo(ephysData)
    shortTet = getShortTet(ephysData)
    rampNorm = getRampNorm(ephysData)
    rampNo = getRampNo(ephysData)
    rampTet = getRampTet(ephysData)
    lumbarloc = "Lumbar Left IMM/CeCV/105p"
    graphRecordingArea(longNorm, longNo, longTet, shortNorm, shortNo, shortTet, rampNorm, rampNo, rampTet, choiceindex,
                       lumbarloc)
def graphNoAcivity(ephysData): #graphs the frequency of no activity against each Rcording Area. Accounts for each type of current.
    longNo = getLongNo(ephysData)
    shortNo = getShortNo(ephysData)
    rampNo = getRampNo(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    long = [longNo[0],longNo[1],longNo[2],longNo[3],longNo[4],longNo[5]]
    short = [shortNo[0],shortNo[1],shortNo[2],shortNo[3],shortNo[4],shortNo[5]]
    ramp = [rampNo[0],rampNo[1],rampNo[2],rampNo[3],rampNo[4],rampNo[5]]
    br1 = np.arange(len(long))
    br2 = [x + barWidth for x in br1]
    br3 = [x+ barWidth for x in br2]
    plt.bar(br1, long, color = "r", width = barWidth,
            edgecolor = "grey", label = "Long Square")
    plt.bar(br2, short, color="g", width=barWidth,
            edgecolor="grey", label="Short Square")
    plt.bar(br3, ramp, color="b", width=barWidth,
            edgecolor="grey", label="Ramp")
    plt.xlabel("Recording Area", fontweight = "bold", fontsize = 15)
    plt.ylabel("Frequency", fontweight = "bold", fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(long))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("No Activity")
    plt.legend()
    plt.show()

def graphNormAcivity(ephysData):
    longNorm = getLongNorm(ephysData)
    shortNorm = getShortNorm(ephysData)
    rampNorm = getRampNorm(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    long = [longNorm[0],longNorm[1],longNorm[2],longNorm[3],longNorm[4],longNorm[5]]
    short = [shortNorm[0],shortNorm[1],shortNorm[2],shortNorm[3],shortNorm[4],shortNorm[5]]
    ramp = [rampNorm[0],rampNorm[1],rampNorm[2],rampNorm[3],rampNorm[4],rampNorm[5]]
    br1 = np.arange(len(long))
    br2 = [x + barWidth for x in br1]
    br3 = [x+ barWidth for x in br2]
    plt.bar(br1, long, color = "r", width = barWidth,
            edgecolor = "grey", label = "Long Square")
    plt.bar(br2, short, color="g", width=barWidth,
            edgecolor="grey", label="Short Square")
    plt.bar(br3, ramp, color="b", width=barWidth,
            edgecolor="grey", label="Ramp")
    plt.xlabel("Current Type", fontweight = "bold", fontsize = 15)
    plt.ylabel("Frequency", fontweight = "bold", fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(long))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Normal Activity")
    plt.legend()
    plt.show()

def graphTetAcivity(ephysData):
    longTet = getLongTet(ephysData)
    shortTet = getShortTet(ephysData)
    rampTet = getRampTet(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    long = [longTet[0],longTet[1],longTet[2],longTet[3],longTet[4],longTet[5]]
    short = [shortTet[0],shortTet[1],shortTet[2],shortTet[3],shortTet[4],shortTet[5]]
    ramp = [rampTet[0],rampTet[1],rampTet[2],rampTet[3],rampTet[4],rampTet[5]]
    br1 = np.arange(len(long))
    br2 = [x + barWidth for x in br1]
    br3 = [x+ barWidth for x in br2]
    plt.bar(br1, long, color = "r", width = barWidth,
            edgecolor = "grey", label = "Long Square")
    plt.bar(br2, short, color="g", width=barWidth,
            edgecolor="grey", label="Short Square")
    plt.bar(br3, ramp, color="b", width=barWidth,
            edgecolor="grey", label="Ramp")
    plt.xlabel("Current Type", fontweight = "bold", fontsize = 15)
    plt.ylabel("Frequency", fontweight = "bold", fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(long))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Tetanic Activity")
    plt.legend()
    plt.show()

def graphNormAcivity(ephysData):
    longNorm = getLongNorm(ephysData)
    shortNorm = getShortNorm(ephysData)
    rampNorm = getRampNorm(ephysData)
    barWidth = 0.25
    # fig = plt.subplot(figsize = (12,8))
    long = [longNorm[0],longNorm[1],longNorm[2],longNorm[3],longNorm[4],longNorm[5]]
    short = [shortNorm[0],shortNorm[1],shortNorm[2],shortNorm[3],shortNorm[4],shortNorm[5]]
    ramp = [rampNorm[0],rampNorm[1],rampNorm[2],rampNorm[3],rampNorm[4],rampNorm[5]]
    br1 = np.arange(len(long))
    br2 = [x + barWidth for x in br1]
    br3 = [x+ barWidth for x in br2]
    plt.bar(br1, long, color = "r", width = barWidth,
            edgecolor = "grey", label = "Long Square")
    plt.bar(br2, short, color="g", width=barWidth,
            edgecolor="grey", label="Short Square")
    plt.bar(br3, ramp, color="b", width=barWidth,
            edgecolor="grey", label="Ramp")
    plt.xlabel("Current Type", fontweight = "bold", fontsize = 15)
    plt.ylabel("Frequency", fontweight = "bold", fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(long))],
               ["Left 15p", "Left 35p", "Left 55pM", "Left 75p", "Left 105p", "Left IMM/CeCv/105p"])
    plt.title("Normal Activity")
    plt.legend()
    plt.show()

def close(root2):
   #root.destroy()
   root2.quit()


def main():
    root = Tk()
    root.withdraw()
    fileName = simpledialog.askstring(title = "File input", prompt = "What's the name of your file?:") #type in Final Data.csv
    ephysData = readFile(fileName)
    root2 = Tk()
    root2.title("Ephys Data Grapher")
    root2.geometry("900x200")
    myFrame = Frame(root2)
    myFrame.grid()
    title1 = Label(myFrame, text = "What data would you like to graph?")
    title1.config(font="Times 14 bold", fg="white", justify = CENTER)
    title1.grid(row=1, column=3)
    mb = Menubutton(root2, text="Recording Area")
    mb.menu = Menu(mb)
    mb["menu"]=mb.menu
    mb.menu.add_command(label='Lumbar Left 15p', command = lambda: graphLeft15p(ephysData))
    mb.menu.add_command(label="Lumbar Left 35p", command = lambda: graphLeft35p(ephysData))
    mb.menu.add_command(label="Lumbar Left 55pM", command = lambda: graphLeft55pM(ephysData))
    mb.menu.add_command(label="Lumbar Left 75p", command = lambda: graphLeft75p(ephysData))
    mb.menu.add_command(label="Lumbar Left 105p", command = lambda: graphLeft105p(ephysData))
    mb.menu.add_command(label="Lumbar Left IMM/CeCV/105p", command = lambda: graphLeftIMM(ephysData))
    mb.grid(row =3, column = 1 )
    mb2 = Menubutton(root2, text = "Current Type")
    mb2.menu = Menu(mb2)
    mb2["menu"]=mb2.menu
    mb2.menu.add_command(label='Long Square', command=lambda: graphLongType(ephysData))
    mb2.menu.add_command(label="Short Square", command=lambda: graphShortType(ephysData))
    mb2.menu.add_command(label="Ramp", command=lambda: graphRampType(ephysData))
    mb2.grid(row = 3, column = 3)
    mb3 = Menubutton(root2, text="Tetanicity")
    mb3.menu = Menu(mb3)
    mb3["menu"] = mb3.menu
    mb3.menu.add_command(label='No Activity', command=lambda: graphNoAcivity(ephysData))
    mb3.menu.add_command(label="Normal Activity", command=lambda: graphNormAcivity(ephysData))
    mb3.menu.add_command(label="Tetanic Activity", command=lambda: graphTetAcivity(ephysData))
    mb3.grid(row=3, column=5)
    exit = Button(root2, text="exit", font=("Calibri", 14, "bold"), command=lambda:close(root2))
    exit.grid(row=5, column = 3)
    root2.mainloop()


main()

