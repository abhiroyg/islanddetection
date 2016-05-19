"""
1st column contains generator/node identifier.
2nd column contains a flag indicating if the identifier 
    is a generator or a node. 1 - generator, 2 - node.
3rd column contains load it produces/needs. +ve means it produces
    -ve means it needs. Counting number of positives gives us
    number of generators. From this we can know till which index
    is the separation point in the above adjacency matrix.
4th column contains the island identifier,
    initially zero - not assigned.
"""
with open('buses.txt', 'r') as f:
    buses = [[int(x) for x in line.split()] for line in f]
print "buses:\n", buses

"""
We first store `generator` and then `node` connections.
It is an adjacency matrix.

Right now, there is no order between and among `generator`s
and `node`s positions in the matrix.
"""
with open('links.txt', 'r') as f:
    connections = [[int(x) for x in line.split()] for line in f]
print "connections:\n", connections

# Assuming the order of stuff in buses and connections is same.
# And connections rows and columns also have same order.
generator_indices = [i for i, x in enumerate(j[1] for j in buses) if x == 1]
node_indices = [i for i, x in enumerate(j[1] for j in buses) if x == 2]
print "generator indices:", generator_indices
print "node indices:", node_indices

generator_loads = [buses[i][2] for i in generator_indices]
node_loads = [-buses[i][2] for i in node_indices]
print "generator loads:", generator_loads
print "node loads:", node_loads

# Sort the generators based on their produce
sorted_generators = [x for (y, x) in sorted(zip(generator_loads, generator_indices), key=lambda pair: pair[0])]
print "sorted generator indices:", sorted_generators

# Sort the nodes based on their need
sorted_nodes = [x for (y, x) in sorted(zip(node_loads, node_indices), key=lambda pair: pair[0])]
print "sorted node indices:", sorted_nodes

excess_generators = False
island_count = 1

# Each element of island is of 3 parts:
# 1st part: island_count
# 2nd part: list of island contituents. 1st being the generator.
# 3rd part: the resultant load/produce of the island.
islands = []

# Go from the highest producing to lowest producing
for gi in sorted_generators:
    # If all nodes are connected / no nodes are left to connect to
    if not 0 in [buses[i][3] for i in node_indices]:
        excess_generators = True
        break

    # Get the node that is connected to this generator
    # that is not already a part of any island
    # and also has highest load among all the nodes
    # connected to this generator.
    try:
        node_index = next(ni for ni in sorted_nodes if buses[ni][3] == 0 and connections[gi][ni] == 1)

        # Form the island and add this node to the island.
        buses[gi][3] = island_count
        buses[node_index][3] = island_count

        islands.append([island_count, [gi, node_index], buses[gi][2] + buses[node_index][2]])

        island_count += 1
    except:
        # We don't have to worry about `that is not already a 
        # part of any island` because the if condition at the 
        # top of the loop takes care of that.

        # So, `next` will fail if this generator is not connected
        # to any node.

        # And, since we are not iterating on number of generators
        # still not connected, we will not be in an infinite loop.
        print "This generator is not connected to any node:", gi

# Get all the nodes that are yet to be connected.
# They are in sorted order.
rem_nodes = [ni for ni in sorted_nodes if buses[ni][3] == 0]

sorted_islands = sorted(islands, lambda x: x[2])

# Go from the highest demanding to lowest demanding
for ni in rem_nodes:
    # Get the island that is most producing
    # and connected to this node.
    try:
        island_index = next(i for i, isl in enumerate(sorted_islands) if connections[ni][isl[1][0]] == 1)

        # Add this node to the island.
        buses[3][ni] = sorted_islands[island_index][0]
        sorted_islands[island_index][1].append(ni)
        sorted_islands[island_index][2] += buses[2][ni]

        sorted_islands = sorted(sorted_islands, lambda x: x[2])
    except:
        #If the node is not connected to any generator.
        print "This node is not connected to any generator:", ni

if excess_generators:
    print "There are more generators than nodes."

print "The islands formed are:"
for island in islands:
    print island[0], island[1], island[2]
