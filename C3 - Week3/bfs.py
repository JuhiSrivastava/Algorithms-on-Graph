#Uses python3

import queue

def distance(adj, s, t):
    dis = [-1]*(len(adj))
    dis[s] = 0
    que = queue.Queue(maxsize=len(adj))
    que.put(s)
    while not que.empty():
        u = que.get()
        for i in adj[u]:
            if dis[i] == -1:
                que.put(i)
                dis[i] = dis[u] + 1
            if i == t:
                return dis[t]
    return dis[t]

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]  
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = map(int, input().split())
    print(distance(adj, s-1, t-1))