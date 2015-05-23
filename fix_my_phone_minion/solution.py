import copy
def answer(x, y, z):
    adjList=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
    if x == 5 or y == 5:
        return "{}".format(0)
    else:
        temp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
        temp[x]=1
        for i in range(1,z):
            possible={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
            for root in temp:
                if temp[root]>0:
                    for child in adjList[root]:
                    	possible[child]+=temp[root]
            temp=copy.deepcopy(possible)
        return "{}".format(temp[y])
        
print answer(6, 2, 101)