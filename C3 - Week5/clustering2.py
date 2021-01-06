#Uses python3
import math
import numpy as np

def calculate_distance(x1,x2,y1,y2):
    return math.sqrt( math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
def find(clustersx,clustersy,a,b,x,y):
    index1 =[]
    index2 =[] 
    flag1 = False
    flag2 = False
    for l in range(len(clustersx)):
        if flag1 and flag2:
            break
        for m in range(len(clustersx[l])):
            if clustersx[l][m] == x[a] and clustersy[l][m] == y[a] :
                index1.append(l)
                index1.append(m)
                flag1 = True
            if clustersx[l][m] == x[b] and clustersy[l][m] == y[b] :
                index2.append(l)
                index2.append(m)
                flag2 = True
            if flag1 and flag2:
                break
    return index1,index2

def kruskal(matrix,x,y,k):
    clustersx = [[x[i]] for i in range(n)]
    clustersy = [[y[i]] for i in range(n)]
    lastmin = 0
    while k != len(clustersx):
        a,b = np.argwhere(matrix == np.min(matrix))[0]
        index1,index2 = find(clustersx,clustersy,a,b,x,y)
        if index1[0] == index2[0]:
            lastmin = matrix[a][b]
            matrix[a][b] = 1000000
            matrix[b][a] = 1000000
            continue
        clustersx[index1[0]] = clustersx[index1[0]] + clustersx[index2[0]]
        clustersy[index1[0]] = clustersy[index1[0]] + clustersy[index2[0]]
        del clustersx[index2[0]]
        del clustersy[index2[0]]
        lastmin = matrix[a][b]
        matrix[a][b] = 1000000
        matrix[b][a] = 1000000
    h = np.argwhere(matrix == lastmin)
    for i,j in h:
        if matrix[i][j] == 1000000:
            continue
        index1,index2 = find(clustersx,clustersy,i,j,x,y)
        if index1[0] == index2[0]:
            matrix[i][j] = 1000000
            matrix[j][i] = 1000000
    return clustersx,clustersy

def clustering(x, y, k):
    matrix = np.zeros((n,n))
    for i in range(n):
        matrix[i][i] = 1000000
        for j in range(i+1,n):
            dist = calculate_distance(x[i],x[j],y[i],y[j])
            matrix[i][j] = dist
            matrix[j][i] = dist
    if k < n:  
        kruskal(matrix,x,y,k)
    return np.min(matrix)

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
    