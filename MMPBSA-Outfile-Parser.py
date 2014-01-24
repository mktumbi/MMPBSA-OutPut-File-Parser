#!/usr/bin/python
import argparse

__author__ = 'Tumbi Mohammed Khaled'

parser = argparse.ArgumentParser(description='This is the script is to extract energy values from MMPBSA.DAT file.')
parser.add_argument('-j', '--jobname', help='Enter your job name and it will appear as first coloumn in the result file', required=True)
parser.add_argument('-i', '--input', help='Filename of MMPBSA.py outfut file (eg.FINAL_MMPBSA.dat).', required=True)
parser.add_argument('-o', '--output', help='Output filename. It will be in append mode.', required=True)
args = parser.parse_args()

fin = open (args.input, "r")
all = fin.read().split('\n')

VDWAALS =  all[83].split()[1]  #Will extract 
EEL =  all[84].split()[1]
EGB =  all[85].split()[1]
ESURF =  all[86].split()[1]
GBTOT =  all[92].split()[4]
EPB =  all[147].split()[1]
ECAVITY =  all[148].split()[1]
PBTOT =  all[154].split()[4]

print args.jobname, "\t", VDWAALS, "\t", EEL, "\t",EGB, "\t",ESURF, "\t",GBTOT, "\t",EPB, "\t",ECAVITY, "\t",PBTOT
fout = open (args.output, "a") 

fout.write(args.jobname)
fout.write('\t')
fout.write(VDWAALS)
fout.write('\t')
fout.write(EEL)
fout.write('\t')
fout.write(EGB)
fout.write('\t')
fout.write(ESURF)
fout.write('\t')
fout.write(GBTOT)
fout.write('\t')
fout.write(EPB)
fout.write('\t')
fout.write(ECAVITY)
fout.write('\t')
fout.write(PBTOT)
fout.write('\n')
fout.close()
fin.close()
