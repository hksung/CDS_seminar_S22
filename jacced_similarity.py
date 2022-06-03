#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:59:53 2022

@author: hakyungsung
"""

def jaccad_similarity(sent1, sent2):
	s1 = set(sent1.split())
	s2 = set(sent2.split())
	return float(len(s1.intersection(s2))/len(s1.union(s2)))


filePointer1 = open('ASD_104_a.txt','r') # get the .cha file of interest
fileContent1 = filePointer1.read() # get the contents of the file
fileLines1 = fileContent1.split('\n') # let's extract the lines into an array
print(fileLines1)
filePointer2 = open('ASD_104_b.txt','r') # get the .cha file of interest
fileContent2 = filePointer2.read() # get the contents of the file
fileLines2 = fileContent2.split('\n') # let's extract the lines into an array
print(fileLines2)

def test():
	for line1, line2 in zip(fileLines1, fileLines2):
		sent1 = line1
		sent2 = line2
		a = jaccad_similarity(sent1, sent2)
		print(sent1, sent2, a)
		#print(a)

def cal():
	for line1, line2 in zip(fileLines1, fileLines2):
		sent1 = line1
		sent2 = line2
		a = jaccad_similarity(sent1, sent2)
		print(a)

test()
cal()

