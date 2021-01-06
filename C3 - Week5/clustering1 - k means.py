#Uses python3
#K-Means
import math
from statistics import mean
def calculate_distance(x1,x2,y1,y2):
    return math.sqrt( math.pow((x1 - x2),2) + math.pow((y1 - y2),2))

def cluster_centroid(x,y,k,centerPoints):
    clustersx = [[] for i in range(k)]
    clustersy = [[] for i in range(k)]
    flag = False
    for i in range(n):
        dist =[]
        for j in range(k):
            dist.append(calculate_distance(x[i],centerPoints[j][0],y[i],centerPoints[j][1]))
        clusterNum = dist.index(min(dist))
        clustersx[clusterNum].append(x[i])
        clustersy[clusterNum].append(y[i])
    print("Before ", centerPoints)
    print(clustersx)
    print(clustersy)
    for i in range(k):
        meanx = mean(clustersx[i])
        if centerPoints[i][0] != meanx:
            centerPoints[i][0] = meanx
            flag = True
        meany = mean(clustersy[i])
        if centerPoints[i][1] != meany:
            centerPoints[i][1] = meany
            flag = True
    print("After ", centerPoints) 
    return flag

def clustering(x, y, k):
    centerPoints = [[x[i],y[i]] for i in range(k)]
    flag1 = True
    while flag1:
        print("Iteration -------")
        flag1 = cluster_centroid(x,y,k,centerPoints)
    return -1.

if __name__ == '__main__':
    n = int(input())
    x=[]
    y=[]
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    k = int(input())
    print("{0:.9f}".format(clustering(x, y, k)))
    