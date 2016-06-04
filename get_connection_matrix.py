connected_nodes = [[0, 2], [0, 3], [1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [4, 5]]
num_nodes = 6  # max(max(x) for x in connected_nodes) + 1
nodes = list(range(num_nodes))

# This is wrong. see:
# https://docs.python.org/2/faq/programming.html#how-do-i-create-a-multidimensional-list
# matrix = [[0]*num_nodes]*num_nodes

matrix = [[0] * num_nodes for _ in range(num_nodes)]

print(matrix)
print(connected_nodes)

for x in connected_nodes:
    matrix[x[0]][x[1]] = 1

print(matrix)
