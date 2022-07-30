import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#f = open("rmsd_trj_100ns.dat")
#lines = f.readlines()
#
#x, y = [], []
#
#for line in lines:
#	x.append(line.split()[0])
#	y.append(line.split()[1])
#
#f.close()

df = pd.read_csv("twist_final_trj.dat", sep=" ", names=["Time", "Twist"])

plt.plot(df["Time"], df["Twist"], linewidth=2.0)
plt.xlim(0,100)
plt.ylim(0.0, 1.5)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("Twist (degree)", fontsize=16)  
plt.tick_params(axis="y", labelsize=12)
plt.tick_params(axis="x", labelsize=12)
plt.grid()
#plt.savefig("twist_trj_100ns_HR_CHARMM_rep1.png", dpi=400)
plt.show()
