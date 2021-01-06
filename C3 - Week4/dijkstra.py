#Uses python3

import queue
import numpy as np


def distance(adj, cost, s, t, infVal):
    dist = [infVal for _ in range(n)]
    index = [i for i in range(n)]
    que = [infVal for _ in range(n)]
    dist[s] = 0
    que[s] = 0
    while len(que) > 0:
        u = que.index(min(que))
        node = index[u]
        for v in adj[node]:
            k = adj[node].index(v)
            if dist[v] > dist[node] + cost[node][k]:
                dist[v] = dist[node] + cost[node][k]
                if v in index:
                    que[index.index(v)] = dist[v]
        del que[u]
        del index[u]
    if dist[t] != infVal:
        return dist[t]
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)] 
    cost = [[] for _ in range(n)]
    infVal = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(c)
        infVal = infVal + c
    s, t = map(int, input().split())
    print(distance(adj, cost, s-1, t-1, infVal + 1))
