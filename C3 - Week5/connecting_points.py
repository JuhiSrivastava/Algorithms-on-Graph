#Uses python3
import math

def prim(x,y):
    cost = [100000000 for _ in range(n)]
    que = [100000000 for _ in range(n)]
    index = [i for i in range(n)]
    cost[0] = 0
    que[0] = 0
    while len(que) > 0:
        u = que.index(min(que))
        node = index[u]
        for v in range(n):
            if node == v:
                continue
            if v in index:
                dis = calculate_distance(x[node],x[v],y[node],y[v])
                if cost[v] > dis:
                    cost[v] = dis
                    que[index.index(v)] = cost[v]
        del que[u]
        del index[u]
    return sum(cost)

def calculate_distance(x1,x2,y1,y2):
    return math.sqrt( math.pow((x1 - x2),2) + math.pow((y1 - y2),2))

def minimum_distance(x, y):
    return prim(x,y)

if __name__ == '__main__':
    n = int(input())
    x=[]
    y=[]
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    print("{0:.9f}".format(minimum_distance(x, y)))
