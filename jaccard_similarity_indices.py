#!/usr/bi/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:59:53 2022

@author: hakyungsung
"""


def jaccad_similarity(sent1, sent2):
	s1 = set(sent1.split())
	s2 = set(sent2.split())
	return float(len(s1.intersection(s2))/len(s1.union(s2)))


def jaccad_similarity_mod(sent1, sent2):
	s1 = set(sent1.split())
	s2 = set(sent2.split())
	try: 
		return float(len(s1)/len(s1.intersection(s2)))
	except ZeroDivisionError:
		return 0

def n_gram (sent1, sent2):
	s1 = set(sent1.split())
	s2 = set(sent2.split())
	return len(s1.intersection(s2))

filePointer1 = open('ASD_132_child.txt','r') # get the .cha file of interest
fileContent1 = filePointer1.read() # get the contents of the file
fileLines1 = fileContent1.split('\n') # let's extract the lines into an array
print(fileLines1)
filePointer2 = open('ASD_132_child.txt','r') # get the .cha file of interest
fileContent2 = filePointer2.read() # get the contents of the file
fileLines2 = fileContent2.split('\n') # let's extract the lines into an array
print(fileLines2)

filePointer3 = open('data.txt','r')
fileContent3 = filePointer3.read()
fileLines3 = fileContent3.split('\n')
print(fileLines3)


def test(filename):
	output = open(filename+'.txt','w')
	for line1, line2 in zip(fileLines1, fileLines2):
		sent1 = line1
		sent2 = line2
		a = jaccad_similarity(sent1, sent2)
		output.write(sent1+'\t'+sent2+'\t'+str(a)+'\n') # print the word to the output file; add a return character
	output.flush()
	output.close()


def test_mod(filename):
	output = open(filename+'.txt','w')
	for line1, line2 in zip(fileLines1, fileLines2):
		sent1 = line1
		sent2 = line2
		a = jaccad_similarity_mod(sent1, sent2)
		output.write(sent1+'\t'+sent2+'\t'+str(a)+'\n') # print the word to the output file; add a return character
	output.flush()
	output.close()

def test_sum(filename):
	output = open(filename+'.txt','w')
	for line1 in fileLines1:
		for line2 in fileLines2:
			sent1=line1
			sent2=line2
			a = jaccad_similarity(sent1, sent2)
			b = jaccad_similarity_mod(sent1, sent2)
			output.write(sent1+'\t'+sent2+'\t'+str(a)+'\t'+str(b)+'\n') # print the word to the output file; add a return character
			if sent1 == sent2:
				break
	output.flush()
	output.close()
	
def quick_analysis(filename):
	output = open(filename+'.txt','w')
	for line3 in fileLines3:
		sent3=line3
		c = len(sent3.split())
		d = len(set(sent3.split()))
		print(c,d)
		output.write(sent3+'\t'+str(c)+'\t'+str(d)+'\n')
	output.flush()
	output.close()	
	
def n_gram_cal(filename):
	output = open(filename+'.txt','w')
	for line1, line2 in zip(fileLines1, fileLines2):
		sent1 = line1
		sent2 = line2
		e = n_gram(sent1, sent2)
		output.write(sent1+'\t'+sent2+'\t'+str(e)+'\n') # print the word to the output file; add a return character
	output.flush()
	output.close()
	
	
test('result_ASD_0603_a')
test_mod('result_ASD_0603_b')
test_sum('test_ASD_132_2')
quick_analysis('quick2')

n_gram_cal('result_ASD_n_gram')
n_gram_cal('result_TD_n_gram')
