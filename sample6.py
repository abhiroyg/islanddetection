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
    bus1[q[j-1][m.index(min(m))]-1][3]=j #island numbers are alloted to the load nodes
    j=j+1
island_number=[i[3] for i in bus1] #we store all the island numbers in the 4th coloumn of the bus1, we dont touch bus 
max_islands=max(island_number) #for using it later
island_all=[] #To sort all islands are in the order
for l in range(1,max_islands+1,1): #we want only the island assigned 1 or 2 or 3, no need for 0(unconnected nodes)
    island=[i for i,x in enumerate(i[3] for i in bus1) if x==l]
    island_all +=[island] #this list has all the islands in order
output=[] #We will be saving the island values in here, sum will be imbalance of each island
sort_imbal=[] #We sort the imbalances with respect to the islands, higher the imbalance first it will be filled
sort_node=[] #We sort the nodes also, higher the value first it will be taken into the island
for j in range(1,max_islands+1,1): 
    imbalance_array=[bus[i][2] for i,x in enumerate(k[3] for k in bus1) if x==j]
    output+=[imbalance_array]
island_imbalance=[sum(output[i]) for i in range(max_islands)] #Imbalance of an island in an array, first element will be imbalance of island 1 and so on...
island_index=[i for i in range(max_islands)]
unconn_nodes=[i for i,x in enumerate(i[3] for i in bus1) if x==0] #Initial unconnected nodes are stored
for i in range(max_islands): #Sorting of islands with respect to imbalance
    sort_imbal.append([i,island_imbalance[i]])
az = sorted(sort_imbal, key=lambda x: x[1], reverse=True)
assign_order=[i[0] for i in az] # In this order the islands will be assigned
for i in unconn_nodes:#Sorting nodes with respect to the weights of the nodes
    sort_node.append([i,bus[i][2]])
nz = sorted(sort_node, key=lambda x: x[1])
nodes_order=[i[0] for i in nz]
while (len(unconn_nodes)!=0):
    if max(island_imbalance)<=0:
        break
    for mi in assign_order:
        print "node assignment order",nodes_order
        for mk in island_all[mi]:
            print "order",assign_order
            print "order element(gen)",mi     
            for mj in nodes_order:
                print "element in island is",mk
                print "the node we are checking", mj
                if link[mj][mk]==1 and island_imbalance[mi]>0: 
                        bus1[mj][3]=mi+1
                        print "the bus which is getting connected ", bus1[mj][0]-1 
                        island_imbalance[mi]+=bus1[mj][2]
                        unconn_nodes=[i for i,x in enumerate(i[3] for i in bus1) if x==0]
                        print "island",island_all[mi]
                        try:
                            no=nodes_order.pop(nodes_order.index(mj))
                            island_all[mi]+=[mj]
                            print "island after adding node ",island_all[mi]
                        except:
                            break                            
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
print "The lines which have to be opened are", open_lines 
