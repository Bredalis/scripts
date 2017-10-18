# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:50:20 2017

@author: Dsamariya
"""

import pandas as pd
import numpy as np
import ntpath

#path to the dataset
test = '/Users/apple/Desktop/research/webkb.txt'

# define column names
names = ['classLabel', 'text']

# loading training data
df = pd.read_csv( test, header=None, names=names, delimiter = "\t")

sentences = np.array(df.text)
classLabels = np.array(df.classLabel)
dirPath, fileName = ntpath.split(test)

myset = set(classLabels)

# print(sentences[0])

if fileName.endswith('.txt')== True:
    name = fileName.replace('.txt', '')
    
outputFile = dirPath + "/" + name + ".arff"

output = open(outputFile, "w")

last = len(sentences)

print(last)

print ("Converting to ARFF file.\n")
  
title = str(name)

output.write("@relation " + str(title) + "\n\n")


output.write( "@attribute text string " + "\n\n")
output.write( "@attribute @@class@@ " + str(myset) + "\n")

output.write("@data" + "\n\n")

for i in range (0, last):
    output.write( "\'" + str(sentences[i]) + "\'" + "," + str(classLabels[i]) +  "\n" )

output.flush()
output.close()
