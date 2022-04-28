#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:48:37 2022

@author: hakyungsung
"""

import numpy as np
import re

filePointer = open('101.cha','r') # get the .cha file of interest
fileContent = filePointer.read() # get the contents of the file
wordIDs = {}
curID = 0

fileOutput = open('extractedWords2.txt','w') # we will save to this file
fileLines = fileContent.split('\n') # let's extract the lines into an array

for line in fileLines: # loop through each entry of that array (i.e., each line)
	if len(line)>0 and line[0] == '*': # if first character is an asterisk, then it's a tier we want
		id = line[1:4]
		if id == 'CHI':
			lineContent = line.split('\t')[1] # second element of array, using tab character
			lineWords = lineContent.split(' ') # get all words (split by space)
			for word in lineWords[:-1]: # loop just up to the time stamp (?) => -1 will skip the last entry of the array  
				if word not in wordIDs:
					curID += 1 # increment the identifiers to incorporate this unseen word
					wordIDs[word] = curID # save this word with this ID
					fileOutput.write(id+'\t'+word+'\t'+str(wordIDs[word])+'\n') # print the word to the output file; add a return character
fileOutput.close()



import numpy as np

filePointer = open('101.cha','r') # get the .cha file of interest
fileContent = filePointer.read() # get the contents of the file
sentIDs = {}
curID = 0

fileOutput = open('extractedsent5.txt','w') # we will save to this file
fileLines = fileContent.split('\n') # let's extract the lines into an array

for line in fileLines: # loop through each entry of that array (i.e., each line)
	if len(line)>0 and line[0] == '*': # if first character is an asterisk, then it's a tier we want
		id = line[1:4]
		if id == 'CHI':
			lineContent = line.split('\t')[1] # second element of array, using tab character
			lineContent = lineContent.replace("hm:", "")
			lineContent = lineContent.replace("+...", "")
			lineContent = lineContent.replace(" .", "")
			lineContent = lineContent.replace("xxx", "")
			lineContent = lineContent.replace("+/.", "")
			lineContent = lineContent.replace("&", "")
			lineContent = lineContent.replace("-uh", "")
			lineContent = lineContent.replace("!", "")
			lineContent = lineContent.replace("?", "")
			lineContent = lineContent.replace("+", "")
			lineContent = lineContent.replace("[.*","")
			lineContent = lineContent.replace("0", "")
			lineContent = re.sub('=.*', '', lineContent, re.I|re.S)
			lineSents = lineContent.split(' .') # get all sentences (split by space)
			print(lineSents)
			for sent in lineSents:
				if sent != '' or " ":
					if sent not in sentIDs:
						curID += 1 # increment the identifiers to incorporate this unseen word
						sentIDs[sent] = curID # save this word with this ID
						try: 
							fileOutput.write(id+'\t'+sent+'\t'+str(sentIDs[sent])+'\n') # print the word to the output file; add a return character
						except KeyError:
							pass
fileOutput.close()