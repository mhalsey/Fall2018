#!/usr/env/python
###############################################################
#Python script that takes input from STRUCTURE Q-plot data to create pie charts for publication purposes
#	By: Michaela Halsey
#	Contact : michaela.k.halsey@gmail.com
##############################################################

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.DataFrame(dict(
        Population='Cottle;Hall;Motley;Dickens'.split(';'),
        Q1=[0,0.48,0,0],
        Q2=[0.65,0.47,0.44,0.81],
        Q3=[0.2,0,0.32,0.03],
        Q4=[0.15,0.05,0.24,0.16],
    ))
#Here, we are naming our Populations (1 through 4) and assigning ancestry proportions to each. 

fig, axes = plt.subplots(2,2, figsize=(10, 6))
#This is where we tell the program how many rows and columns we want our figure to have. We have 2 rows and 4 pies here. 

for i, (idx, row) in enumerate(df.set_index('Population').iterrows()):
    ax = axes[i // 2, i % 2]
    row = row[row.gt(row.sum() * .01)]
    ax.pie(row, labels=row.index, startangle=30)
    ax.set_title(idx)
#Fancy bit of code makes the plots.
 
fig.subplots_adjust(wspace=.3)
#Adjusts the spacing between the plots

fig.savefig('pies.png')
