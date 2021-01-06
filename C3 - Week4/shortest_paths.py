#Uses python3

def Explore(adj,v, reachable):
    reachable[v] = 1
    for w in adj[v]:
        if reachable[w] == 0:
            Explore(adj,w, reachable)

def reach(adj, x, reachable):
    Explore(adj,x, reachable)

def relax_all_edges(adj,distance,check,shortest, reachable):
    flag = False
    checkFlag = False
    for j in range(len(adj)):
        if reachable[j] == 0:
            continue
        for v in adj[j]:
            if reachable[v] == 0:
                continue
            k = adj[j].index(v)
            if distance[v] > distance[j] + cost[j][k]:
                distance[v] = distance[j] + cost[j][k]
                if check == True and shortest[v] == 1:
                    shortest[v] = 0
                    checkFlag = True
                flag = True
    return flag,checkFlag

def findDistance(adj, cost,s, distance,shortest, reachable):
    distance[s] = 0
    flag1 = False
    check = False
    returnCheck = True
    for i in range(len(adj)):
        flag1,returnCheck = relax_all_edges(adj,distance,check,shortest, reachable)
        if not flag1:
            break
    returnCheck = True
    if flag1:
        check = True
        while returnCheck:
            flag1,returnCheck = relax_all_edges(adj,distance,check,shortest, reachable)

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    reach(adj, s, reachable)
    findDistance(adj, cost, s, distance,shortest, reachable)

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)] 
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(c)
    s = int(input())
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

