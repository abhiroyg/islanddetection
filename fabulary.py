a=[[40001,40003],[40001,40007],[40002,40005]]
b=range(40001,40008) + range(40101, 40105)

# print b
# b = [[x] for x in b]
# print b
# 
# count = 0
# for i in range(len(b)):
#     b[i].append(count)
#     count += 1
# 
# print b

b = {k:0 for k in b}
count = 0
for key in b:
    b[key] = count
    count += 1

matrix = [[0] * len(b) for _ in range(len(b))]
print matrix
print a

for x in a:
    matrix[b[x[0]]][b[x[1]]] = 1

print matrix
