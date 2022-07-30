import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce


df1 = pd.read_csv("contact_protofilament1.dat", sep=" ", names=['Time', 'Interchain_protofilament1'])
df2 = pd.read_csv("contact_protofilament2.dat", sep=" ", names=['Time', 'Interchain_protofilament2'])
df3 = pd.read_csv("contact_interprotofilament.dat", sep=" ", names=['Time', 'Inter-protofilament'])
df4 = pd.read_csv("intrachain_prot1_contact.dat", sep=" ", names=['Time', 'Intrachain_protofilament1'])
df5 = pd.read_csv("intrachain_prot2_contact.dat", sep=" ", names=['Time', 'Intrachain_protofilament2'])


dataframes = [df1, df2, df3, df4, df5]

df = reduce(lambda left,right: pd.merge(left,right, on=['Time']), dataframes)

df['Protofilament 1'] = df['Interchain_protofilament1']+df['Intrachain_protofilament1']
df['Protofilament 2'] = df['Interchain_protofilament2']+df['Intrachain_protofilament2']


df['Total'] = df['Protofilament 1']+df['Protofilament 2']+df['Inter-protofilament']
#print df


plt.plot(df['Time'], df['Protofilament 1'], color='red', linewidth=1.0, label='Protofilament 1')
plt.plot(df['Time'], df['Protofilament 2'], color='blue', linewidth=1.0, label='Protofilament 2')
plt.plot(df['Time'], df['Inter-protofilament'], color='green', linewidth=1.0, label='Inter-protofilament')
plt.plot(df['Time'], df['Total'], color='black', linewidth=1.0, label='Total')
plt.xlim(0,100)
plt.ylim(0,25000)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("No. of Contacts", fontsize=16)
plt.title("Heavy Atom Contacts in Fibril", fontsize=16)  
leg=plt.legend(bbox_to_anchor=(0.6, 0.6), frameon=False)

for line in leg.get_lines():
    line.set_linewidth(2)

plt.grid()
#plt.show()

plt.savefig("interchain_contact_100ns_a_HR_final.png", dpi=400)
