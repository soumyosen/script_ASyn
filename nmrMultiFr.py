import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

chains = ['C','D','E','F','G','H','I','J']
df1 = pd.DataFrame(columns='CHAIN NUM RES ATOMNAME SHIFT'.split())

for i in range(0, 100):
	df = pd.read_csv("frm%d.pdb.cs"%i) 
	for f in chains:
		df1 = df1.append(df[df['CHAIN']==f], ignore_index=True)


df2=df1.groupby(['NUM','RES','ATOMNAME'])['SHIFT'].mean()
print df2

df3=df1.groupby(['NUM','RES','ATOMNAME']).mean()
print df3


#df2.to_csv('NMRdataMultiFR.dat', sep='\t')     


