#!/usr/bin/env python

import os
from subprocess import Popen, PIPE
from Bio import SeqIO 
#from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline

print("Please provide the species code")
SP = input()
print("Working with %s" % SP)

os.mkdir(SP) 

blastCline = NcbiblastnCommandline(query="/home/mhalsey/starting_library.fas", db="/home/mhalsey/cPer_rn.fa", out="/home/mhalsey/%s/%s.txt" % (SP, SP), outfmt=6)
stout, stderr = blastCline()

genome = cPer_rn.fa.gz
blast = cPer_rn.txt
consTEs = starting_library.fas
seqBuffer = 1000 
seqNum = 20 

BEAR = subprocess.Popen(["perl", "/home/mhalsey/extractAlignTEs.pl", genome, blast, consTEs, seqBuffer, seqNum], stdout=subprocess.PIPE)
