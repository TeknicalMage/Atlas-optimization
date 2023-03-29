#!/bin/bash

echo "Start!"


File="urllist.txt"
Lines=$(cat $File)

for Line in $Lines
do
    python3 Test.py -f $Line & 
    
done

