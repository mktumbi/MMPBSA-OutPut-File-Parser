#!/bin/sh
/*

find  -type f -name "FINAL_MMPBSA.dat" | while read line; do
	echo $line
	$AMBERHOME/bin/MMPBSA-Result-Parser.py -j $line -i $line -o /home/amber12/xvz/testing.xls
	
done
 
