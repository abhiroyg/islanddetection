"""
We first store `generator` and then `node` connections.
It is an adjacency matrix.
"""
with open('links.txt', 'r') as f:
    connections = [int(x) for line in f for x in line.split()]

"""
1st column contains generator/node identifier.
2nd column contains load it produces/needs. +ve means it produces
    -ve means it needs. Counting number of positives gives us
    number of generators. From this we can know till which index
    is the separation point in the above adjacency matrix.
3rd column contains the island identifier, initially zero - not assigned.
"""
with open('bases.txt', 'r') as f:
    bases = [int(x) for line in f for x in line.split()]

# There will be at least one node - so no need for exception handling.
node_start = next(i for i, x in enumerate(bases[1]) if x < 0)


