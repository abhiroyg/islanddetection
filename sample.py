#!/usr/bin/python
with open('links.txt') as f:
    link = [[int(x) for x in line.split( )] for line in f ]
with open('buses.txt') as f:
    bus = [[int(x) for x in line.split( )] for line in f ]
import copy
bus1 = copy.deepcopy(bus)
b = [i[2] for i in bus]
u = [i for i,x in enumerate(b) if x>0] #generator bus index
v = [j for j,x in enumerate(b) if x<0] #load bus index
u1 = [i+1 for i in u] #all generator bus numbers
v1 = [i+1 for i in v] #all load bus numbers
gen = [bus[i-1] for i in u] #all generator bus values
load = [bus[i-1] for i in v] #all load bus values
p=[[i+1 for i,x in enumerate (link[j]) if x==1] for j in u] #links to generator buses
import copy
q = copy.deepcopy(p) # q is a copy of p which are links to generator buses
for i,x in enumerate (q): # links to generator buses which are not generators
	for ux in u1:
		try:
			p1=x.index(ux)
			del q[i][p1]
		except:
			pass
j=1
for i in u: # assigning islands to generators and the nearest max loads 
    bus1[i][3]=j #generators are assigned island number
    r=len(q[j-1]) #length of the nodes to be checked 
    m=[bus[q[j-1][k]-1][2] for k in range(r)] #check all the nearby connected load nodes
    bus1[q[m.index(min(m))][j-1]-1][3]=j #island numbers are alloted to the load nodes
    j=j+1
print bus1 #As the initial assignment is over the other would be an optimisation problem where we have to minimise the load-gen imbalance

