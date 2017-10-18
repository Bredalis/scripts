#!/bin/sh
# author: Dsamariya
# This script merge all CSV file in one file.
# I am using this script to merge train.csv and text.csv file in one CSV.

#Read all csv file from directory
for i in *.csv
do
	#Print File name to track progress
    echo $i
	#File merge in final.csv
    cat $i >> final.csv
    echo 'Merged. $i to final.csv'
done