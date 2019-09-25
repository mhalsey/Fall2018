#!/usr/bin/env python3

#########################
#
# An Attempt Was Made
#
# Version 25.9.19
#########################

#Imports modules that we will need
#Will add to list once bugs are exposed

import os
import sys
import argparse
import Bio
from Bio import SeqIO

print os.getcwd()
#Shows us current directory
#Change directory as needed

#os.chdir(('c:\\Users\\where\\work\\will\be\done'))

#def dir_path():
#    if os.path.isdir():
#        return working_directory
#    else:
#       raise NotADirectoryError(working_directory)

#The idea here is to have the working directory set before parsing arguments.
#Unless we like typing out paths

#Begin parsing arguments
def get_args()"

	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--path", type=dir_path)
	parser.add_argument("-f", "--twoBit_file", type=file, choices=['.2bit'], required=True, help="Where genome file is in .2bit")
	parser.add_argument("-b", "--batch_count", type=int, default=10, help="How many batches are being processed")
	parser.add_argument("-s","--species", required=True, help="Species name")
	parser.add_argument("-l", "--library", type=file, choices=['.fa,.fas'], help="Transposable element library in .fasta file")
	parser.add_argument("-e", "engine", help="Choo! Choo! Kidding. Search engine used, ex. UCSC")
	parser.add_argument("-g" "--genomeDir", type=dir_path, required=True, help="Directory where genome is found")
	#parser.add_argument("-n", "--nolow", help="I have no idea what this does")
	#parser.add_argument("-i", "--inv", help="Not sure what this does either")

	args = parser.parse_args()

	GENOME = args.twoBit_file
	COUNT = args.batch_count
	SPECIES = arg.species
	LIBRARY = args.library
	ENGINE = args.engine
	G_DIRECTORY = args.genomeDir

GENOME, COUNT, SPECIES, LIBRARY, ENGINE, G_DIRECTORY = get_args()

	return = get_args()
		
if args.species:
    print("Processing...")
else:
    print("Please specify species")
