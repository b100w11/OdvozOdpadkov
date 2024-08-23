#!/bin/sh
file=$1
year="2024"
months="januar februar marec april maj junij julij avgust september oktober november december"

sed  "s/\.\ januar/\-1\-${year}/g" $file | sed  "s/\.\ februar/\-2\-${year}/g" | sed  "s/\.\ marec/\-3\-${year}/g" | sed  "s/\.\ april/\-4\-${year}/g" | sed  "s/\.\ maj/\-5\-${year}/g" | sed  "s/\.\ junij/\-6\-${year}/g" | sed  "s/\.\ julij/\-7\-${year}/g" | sed  "s/\.\ avgust/\-8\-${year}/g" | sed  "s/\.\ september/\-9\-${year}/g" | sed  "s/\.\ oktober/\-10\-${year}/g" | sed  "s/\.\ november/\-11\-${year}/g" | sed  "s/\.\ december/\-12\-${year}/g"  
