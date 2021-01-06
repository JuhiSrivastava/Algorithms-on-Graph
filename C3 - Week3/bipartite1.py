#Uses python3

import queue
def distance(adj,s,dis):
    dis[s] = 0
    que = queue.Queue(maxsize=len(adj))
    que.put(s)
    flag = 1
    while not que.empty():
        u = que.get()
        seta = set(adj[u])
        for i in adj[u]:
            if dis[i] == -1:
                que.put(i)
                dis[i] = dis[u] + 1
            if len(set(adj[i]).intersection(seta)) > 0:
                flag = 0
                break
        if flag == 0:
            break
    return flag,dis

def bipartite(adj,initial):
    dis = [-1]*(len(adj))
    flag,dis = distance(adj,initial,dis)
    while flag == 1 and -1 in dis:
        e = dis.index(-1)
        if len(adj[e]) > 0:
            flag,dis = distance(adj,e,dis)
        else:
            dis[e] = 0
    return flag

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)] 
    initial = -1
    for i in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue
        if b-1 not in adj[a-1]:
            adj[a - 1].append(b - 1)
        if a-1 not in adj[b-1]:
            adj[b - 1].append(a - 1)
        if i ==0:
            initial = a-1
    print(bipartite(adj,initial))
