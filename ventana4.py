#!/usr/bin/python

from Bio import SeqIO
from Bio import SeqUtils
from Bio.SeqUtils import GC
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


genome = []
for record in SeqIO.parse("Heliconius_cydno_alithea.fna", "fasta"):
	genome.append(record)

print ("Genome locked")
print (len(genome))
#Imports genome and tells us how big it is

scaffolds = [] 
for record in genome:
	if len(record.seq) > 29999:
		scaffolds.append(record.seq)

#Finds scaffolds of suitable size 
print("Found %i scaffolds of suitable size" % len(scaffolds))

print ("Scaffolds of suitable size loaded")

#Defines our sliding window iterator, called the ventana
def ventana (input,size): 

#Re-verify inputs
#	if step > size:
#			raise Exception("Error: step must not be larger than size.")
#	if size > len(input):
#			raise Exception("Error: size must not be larger than genome.")

#Proceed with sliding ventana
	global chunk
	chunk = []
	for i in range(0,size):
		chunk.append(input[i:])
#		yield input[i:i+size]
	return;

def GCC(list):
#Calculates GC content for each window
	global GCCounter
	GCCounter = []
	for sequence in list:
		GC(sequence)
		GCCounter.append(sequence)	
	return;

print ("Initializing the ventana")
ventana(input=scaffolds, size=10000)
print("Calculating GC content")
#calc = ' '.join(str(z) for z in chunk)
GCC(chunk)
plot = ' '.join(str(a) for a in GCCounter)
print("Plotting...")

#Ideally, plots each window's GC content
fig = plt.hist(plot, density=True)
plt.ylabel('GC Content')
num_bins = len(scaffolds)
plt.savefig('ventana.pdf')
