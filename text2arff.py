# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:50:20 2017

@author: Durgesh Samariya
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import ntpath  # Module for handling file paths

# Path to the dataset
test = 'C:\\Users\\Dsamariya\\Desktop\\Data\\r8.txt'

# Define column names for the DataFrame
names = ['classLabel', 'text']

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(test, header=None, names=names, delimiter="\t")

# Extract text and class labels from the DataFrame
sentences = np.array(df.text)  # Extract text data
classLabels = np.array(df.classLabel)  # Extract class labels

# Get directory path and file name from the provided path
dirPath, fileName = ntpath.split(test)

# Check if the file name ends with '.txt' extension and replace it with an empty string
if fileName.endswith('.txt') == True:
    name = fileName.replace('.txt', '')

# Create the output ARFF file path and name
outputFile = dirPath + "/" + name + ".arff"

# Open the output ARFF file in write mode
output = open(outputFile, "w")

# Determine the title for the ARFF file (using the name extracted from the file path)
title = str(name)

# Write ARFF file headers and attributes
output.write("@relation " + str(title) + "\n\n")
output.write("@attribute text string " + "\n")
output.write("@attribute @@class@@ " + "{" + ",".join(set(classLabels)) + "}" + "\n\n")
output.write("@data" + "\n")

# Write data instances (text and corresponding class labels) to the ARFF file
last = len(sentences)
for i in range(0, last):
    output.write("\'" + str(sentences[i]) + "\'" + "," + str(classLabels[i]) + "\n")

# Flush and close the output file
output.flush()
output.close()
