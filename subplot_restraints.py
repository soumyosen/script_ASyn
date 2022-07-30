import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

restraint_list = ["38CG_77CA", "38CG_76CB", "38CG_78CB", "41C_68CA", "42CA_68C", "42CA_69CA",
		  "65CG_70CB", "73CA_94CD", "72CB_94CD", "79CD_88CD", "79CD_88CB", "77CG1_88CG2",
	          "77CG1_88CD", "80NZ_35CD", "87CB_91CA", "87CB_89CB"]


NMR_dist = [5.381, 4.028, 3.987, 6.976, 5.355, 5.374, 4.743, 3.329, 5.894, 3.029, 5.374, 4.598, 
	    5.35, 3.799, 4.645, 3.329]

step = range(2500)
colvector = np.array([step]).T
df = pd.DataFrame(colvector, columns=['Step'])
df['Time'] = df["Step"]*0.04
#print df

for i in restraint_list:
	df_temp = pd.read_csv("avg_closest_%s.dat" % i, sep=" ", names=['Time', '%s' % i])
	df['%s' % i] = df_temp['%s' % i]

#print df	

fig, axs = plt.subplots(nrows=8, ncols=2, sharex=True,)
fig.subplots_adjust(hspace =.2, wspace=.2)
axs = axs.ravel()

for f,j in zip(range(16), restraint_list):
        axs[f].plot(df['Time'], df['%s' % j], color='green', linewidth=0.8, label=restraint_list[f])
        axs[f].set_ylim(2, 8)
        axs[f].set_xlim(0, 100)
        axs[f].tick_params(axis="y", labelsize=12)
        axs[f].tick_params(axis="x", labelsize=12)
        #axs[f].grid()
	#axs[f].legend(loc=1)
	axs[f].text(60, 6.8, restraint_list[f], fontsize=12, color='red')	
	axs[f].text(60, 3, "%s $\AA$" % NMR_dist[f], fontsize=12, color='blue')

for k in range(14):
	axs[k].text(20, 6.8, "Intra_filament", fontsize=12)

for k in range(14,16):
	axs[k].text(20, 6.8, "Inter_filament", fontsize=12)

for k in [14, 15]:
        axs[k].set_xlabel("Time (ns)", fontsize=16)

for k in [0, 4, 8, 12]:
        axs[k].set_ylabel("Distance ($\AA$)", fontsize=16)



fig.set_size_inches(10, 10)
#plt.show()

plt.savefig("restraint.png", dpi=400)
