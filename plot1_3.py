import matplotlib.pyplot as plt

f = open("twist_trj.dat")
lines = f.readlines()

x, y = [], []

for line in lines:
	x.append(line.split()[0])
	y.append(line.split()[1])

f.close()
plt.plot(x,y,linewidth=0.5)
plt.xlim(0,100)
plt.ylim(0.0,2.0) 
plt.title("Twist Angle", fontsize=16)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("Angle (degree)", fontsize=16)  
plt.grid()
#plt.show()
plt.savefig("twist_HR.png", dpi=400)
