#!/usr/bin/python

import copy

with open('links.txt') as f:
    link = [[int(x) for x in line.split( )] for line in f ]
print link

with open('buses1.txt') as f:
    bus = [[int(x) for x in line.split( )] for line in f ]
print bus

u = [i for i, x in enumerate(bus) if x[1] == 1] #generator bus index
print u

v = [j for j, x in enumerate(bus) if x[1] == 2] #load bus index
print v

p = [[i for i, x in enumerate(link[j]) if x == 1] for j in u] #links to generator buses
q = [[i for i, x in enumerate(link[j]) if x == 1 and i in v] for j in u] #links to generator buses
print p, q

# Issue:
# 1. Not sorted
# 2. Not considered the case when, num. generators > num. nodes
# 3. If above case is solved, we have to update generator only after node.
j = 1
bus1 = copy.deepcopy(bus) #deep copy is to be used as it is a copy of list of lists, else bus1=bus[:] would suffice
for i in u: # assigning islands to generators and the nearest max loads 
    bus1[i][3] = j #generators are assigned island number
    m = [bus[n][2] for n in q[j - 1]] #check all the nearby connected load nodes
    #print m
    #print min(m)
    bus1[q[j - 1][m.index(min(m))]][3] = j #island numbers are alloted to the load nodes
    j = j+1
print bus1

island_number = [i[3] for i in bus1] #we store all the island numbers in the 4th coloumn of the bus1, we dont touch bus 
#print island_number
max_islands = max(island_number) #for using it later
island_all = [] #To sort all islands are in the order
for l in range(1, max_islands + 1): #we want only the island assigned 1 or 2 or 3, no need for 0(unconnected nodes)
    island = [i for i, x in enumerate(i[3] for i in bus1) if x == l]
    island_all += [island] #this list has all the islands in order
print island_all

output = [] #We will be saving the island values in here, sum will be imbalance of each island
for j in range(1, max_islands + 1): 
    imbalance_array = [bus[i][2] for i, x in enumerate(k[3] for k in bus1) if x == j]
    output += [imbalance_array]
island_imbalance = [sum(output[i]) for i in range(max_islands)] #Imbalance of an island in an array, first element will be imbalance of island 1 and so on...

island_index = [i for i in range(max_islands)]

sort_imbal = [] #We sort the imbalances with respect to the islands, higher the imbalance first it will be filled
for i in range(max_islands): #Sorting of islands with respect to imbalance
    sort_imbal.append([i, island_imbalance[i]])
az = sorted(sort_imbal, key=lambda x: x[1], reverse=True)
assign_order=[i[0] for i in az] # In this order the islands will be assigned

sort_node = [] #We sort the nodes also, higher the value first it will be taken into the island
unconn_nodes = [i for i, x in enumerate(i[3] for i in bus1) if x == 0] #Initial unconnected nodes are stored
for i in unconn_nodes: #Sorting nodes with respect to the weights of the nodes
    sort_node.append([i, bus[i][2]])
nz = sorted(sort_node, key=lambda x: x[1])
nodes_order = [i[0] for i in nz]

while (len(unconn_nodes) != 0):
    if max(island_imbalance) <= 0:
        break
    for mi in assign_order:
        print mi, assign_order     
        for mk in island_all[mi]:
            print mk 
            for mj in nodes_order:
                print mj 
                if link[mj][mk] == 1 and island_imbalance[mi] > 0: 
                        bus1[mj][3] = mi + 1 
                        island_imbalance[mi] += bus1[mj][2]
                        unconn_nodes = [i for i, x in enumerate(i[3] for i in bus1) if x == 0]
                        print island_all[mi]
                        print nodes_order
                        try:
                            island_all[mi].append(
                            nodes_order.pop(0))
                            #print nodes_order
                            #print island_all[mi]
                        except:
                            break

island_fin=[]
for isl in range(1, max_islands+1):
    fin_islands = [j[3] for j in bus1]
    island_fin += [[fi for fi, x in enumerate(fin_islands) if x == isl]]

print "The total number of islands are :", max_islands
for px in range(max_islands):
    print "The island and its imbalance:", px + 1, island_fin[px], island_imbalance[px]
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
