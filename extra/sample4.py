#!/usr/bin/python
with open('links.txt') as f:
    link = [[int(x) for x in line.split( )] for line in f ]
with open('buses1.txt') as f:
    bus = [[int(x) for x in line.split( )] for line in f ]
import copy
bus1 = copy.deepcopy(bus) #deep copy is to be used as it is a copy of list of lists, else bus1=bus[:] would suffice
u = [i for i,x in enumerate([i[1] for i in bus]) if x==1] #generator bus index
v = [j for j,x in enumerate([i[1] for i in bus]) if x==2] #load bus index
p=[[i+1 for i,x in enumerate (link[j]) if x==1] for j in u] #links to generator buses
u1 = [i+1 for i in u] #all generator bus numbers
import copy
q = copy.deepcopy(p) # q is a copy of p which are links to generator buses
for i,x in enumerate (q): # links to generator buses which are not generators, there might be a scenario where a single generator is connected to another generator, which we want to remove that scenario. The values are stored in q.
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
island_number=[i[3] for i in bus1] #we store all the island numbers in the 4th coloumn of the bus1, we dont touch bus 
max_islands=max(island_number) #for using it later
island_all=[] #To sort all islands are in the order
for l in range(1,max_islands+1,1): #we want only the island assigned 1 or 2 or 3, no need for 0(unconnected nodes)
    island=[i for i,x in enumerate(i[3] for i in bus1) if x==l]
    island_all +=[island] #this list has all the islands in order
output=[]
sort_imbal=[] 
sort_node=[]
for j in range(1,max_islands+1,1):
    imbalance_array=[bus[i][2] for i,x in enumerate(k[3] for k in bus1) if x==j]
    output+=[imbalance_array]
island_imbalance=[sum(output[i]) for i in range(max_islands)]
island_index=[i for i in range(max_islands)]
unconn_nodes=[i for i,x in enumerate(i[3] for i in bus1) if x==0]
for i in range(max_islands):
    sort_imbal.append([i,island_imbalance[i]])
az = sorted(sort_imbal, key=lambda x: x[1], reverse=True)
assign_order=[i[0] for i in az]
for i in unconn_nodes:
    sort_node.append([i,bus[i][2]])
nz = sorted(sort_node, key=lambda x: x[1])
nodes_order=[i[0] for i in nz]
while (len(unconn_nodes)!=0):
    if max(island_imbalance)<=0:
        break
    for mi in assign_order:        
        for mj in nodes_order:
            for mk in island_all[mi]:
                if link[mj][mk]==1 and island_imbalance[mi]>0:
                        bus1[mj][3]=mi+1
                        island_imbalance[mi]+=bus1[mj][2]
                        unconn_nodes=[i for i,x in enumerate(i[3] for i in bus1) if x==0]
                        nodes_order.pop(0)
island_fin=[]
for isl in range(1,max_islands+1,1):
    fin_islands=[j[3] for j in bus1]
    island_fin+=[[fi for fi,x in enumerate(fin_islands) if x==isl]]
print "The total number of islands are :", max_islands
for px in range(max_islands):
    print "The island and its imbalance:" ,px+1,island_fin[px], island_imbalance[px]
print "The number of unconnected nodes and nodes are:", len(unconn_nodes), unconn_nodes
open_lines=[]
for mii in range(max_islands):
    for mij in range(max_islands):
        for mik in island_fin[mii]:
            for mil in island_fin[mij]:
                if link[mik][mil]!=0 and mii!=mij:
                    open_lines+=[[mik,mil]]
#len_open=len(open_lines)/2
#lines_to_be_opened=[]
#for i in range(len_open):
#    lines_to_be_opened += [open_lines[i]]
print "The lines which have to be opened are", open_lines 
