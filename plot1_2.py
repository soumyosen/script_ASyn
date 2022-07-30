import matplotlib.pyplot as plt

f = open("rmsf_final1a_100ns.dat")
lines = f.readlines()

x, y = [], []

for line in lines:
	x.append(line.split()[0])
	y.append(line.split()[1])

f.close()
plt.plot(x,y,linewidth=2.0)
plt.xlim(29,104)
plt.ylim(0.0, 5.0)
plt.title("RMSF of Heavy Atoms", fontsize=16)
plt.xlabel("Residue", fontsize=16)
plt.ylabel("RMSF ($\AA$)", fontsize=16)  
plt.tick_params(axis="y", labelsize=12)
plt.tick_params(axis="x", labelsize=12)
plt.grid()
#plt.show()
plt.savefig("RMSF_100ns_HR.png", dpi=400)
