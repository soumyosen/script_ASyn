import matplotlib.pyplot as plt

f = open("rmsd_trj_100ns.dat")
lines = f.readlines()

x, y = [], []

for line in lines:
	x.append(line.split()[0])
	y.append(line.split()[1])

f.close()
plt.plot(x,y,linewidth=2.0)
plt.xlim(0,100)
plt.ylim(0.0, 6.0)
#plt.title("Backbone Heavy Atoms RMSD of residue 35 to 46 and 62 to 96", fontsize=16)
plt.title("RMSD of residue 35 to 46 and 62 to 96", fontsize=16)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("RMSD ($\AA$)", fontsize=16)  
plt.tick_params(axis="y", labelsize=12)
plt.tick_params(axis="x", labelsize=12)
plt.grid()
plt.savefig("RMSD_trj_100ns_HR.png", dpi=400)
#plt.show()
