a=[[0,2],[0,3],[1,2],[1,4],[2,3],[2,5],[3,4],[4,5]]
b=[0,1,2,3,4,5]
dummy=[]
dummy_x=[0]*len(b)
for i in range(len(b)):
    dummy+=[dummy_x]
print dummy
'''for lii in range(len(a)): 
        print "The coloumn we are checking is", lii   
        for bii in range(len(b)):
            print "index of first node",bii
            for bij in range(len(b)):
                print "the second node index being checked is", bij
                print "the first bus checked", b[bij]
                print "the second bus checked", b[bii]
                print "the row we are checking is", a[lii]
                if a[lii][0]==b[bii] and a[lii][1]==b[bij]:
                        dummy[bii][bij]=1
                        print "success"
                        #dummy[bij][bii]=1
print dummy'''
kei=[]
kej=[]
for ki in range(len(a)):
    kei+=[b.index(a[ki][0])]
    kej+=[b.index(a[ki][1])]
print dummy
print kei
print kej
for i in kei:
    for j in kej:
        dummy[i][j]=1
print dummy
