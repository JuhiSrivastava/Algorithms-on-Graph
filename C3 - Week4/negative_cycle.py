#Uses python3

def relax_all_edges(adj,dist):
    flag = False
    for j in range(len(adj)):
        for v in adj[j]:
            k = adj[j].index(v)
            if dist[v] > dist[j] + cost[j][k]:
                dist[v] = dist[j] + cost[j][k]
                flag = True
    return flag


def negative_cycle(adj, cost,infVal):
    dist = [infVal for _ in range(n)]
    dist[0] = 0
    flag1 = False
    for i in range(len(adj) +1):
        flag1 = relax_all_edges(adj,dist)
        if not flag1:
            break
        if flag1 and  i == len(adj):
            return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)] 
    cost = [[] for _ in range(n)]
    infVal = 1
    for i in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(c)
        infVal = infVal + c
    print(negative_cycle(adj, cost, infVal))
