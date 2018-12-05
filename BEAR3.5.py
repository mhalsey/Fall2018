#!/usr/bin/env python

import os
import subprocess
from subprocess import Popen, PIPE
from Bio import SeqIO 
from Bio.Blast.Applications import NcbiblastnCommandline

#User provided input
print("Please provide the species code")
SP = input()
print("Working with %s" % SP)

#Makes new directory
os.mkdir(SP) 

#Loads blast module
subprocess.check_call('ml intel rmblast', shell=True)

#Makes blast database
subprocess.check_call('makeblastdb -in "/lustre/work/daray/extractAlign_assignment/%s.fa.gz" % SP, -dbtype nucl -out "/lustre/home/mhalsey/%s" % SP',shell=True)

#Calls blastn
blastCline = NcbiblastnCommandline(query="/home/mhalsey/starting_library.fas", db="/home/mhalsey/cPer_rn.fa", out="/home/mhalsey/%s/%s.txt" % (SP, SP), outfmt=6)
stout, stderr = blastCline()

#Sets variables for ExtractAlign
genome = cPer_rn.fa
blast = cPer_rn.txt
consTEs = starting_library.fas
seqBuffer = 1000 
seqNum = 20 

#Runs ExtractAlign
BEAR = subprocess.Popen(["perl", "/home/mhalsey/extractAlignTEs.pl", genome, blast, consTEs, seqBuffer, seqNum], stdout=subprocess.PIPE)
