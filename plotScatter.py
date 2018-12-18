import matplotlib.pyplot as plt
import pandas as pd

df  = pd.read_csv("data.csv")
values = df.values
nData = values[:,0]
primsData = values[:,1]
otherData = values[:,2]
kruskalsData = values[:,3]

primsPlt = plt.scatter(nData,primsData,alpha=0.5,color='#66DDAA')
#otherPlt = plt.scatter(nData,otherData,alpha=1,color='#FF6600')
#kruskalsPlt = plt.scatter(nData,kruskalsData,alpha=1,color='#FFAADD')
kruskalsPlt = plt.scatter(nData,kruskalsData,alpha=0.5,color='#FF6600')

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

plt.legend((primsPlt,kruskalsPlt),('Prims','Kruskals'))
plt.xlabel(r"Nodes in network")
plt.ylabel(r"Total defending days")
plt.show()
plt.savefig('./Images/primsVsKruskals.png')
