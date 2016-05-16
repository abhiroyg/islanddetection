#!/usr/bin/python
with open('links.txt') as f:
    link = [[int(x) for x in line.split( )] for line in f ]
#linking matrix has been uploaded
#positive for
with open('buses.txt') as f:
    bus = [[int(x) for x in line.split( )] for line in f ]
b = [i[2] for i in bus]
#c=b[:]
#c.sort(reverse=True) #ordering based on weights
u = [i for i,x in enumerate(b) if x>0] #generator bus index
v = [j for j,x in enumerate(b) if x<0] #load bus index
u1 = [i+1 for i in u] #all generator bus numbers
v1 = [i+1 for i in v] #all load bus numbers
gen = [bus[i-1] for i in u] #all generator bus values
load = [bus[i-1] for i in v] #all load bus values
p=[[i+1 for i,x in enumerate (link[j]) if x==1] for j in u] #links to generator buses
for i,x in enumerate (p): #finding out buses which are connected to the generator bus but arent generators
	for ux in u1:
		try:
			p1=x.index(ux)
			del p[i][p1]
		except:
			pass

