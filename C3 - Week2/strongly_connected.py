#Uses python3

import sys

sys.setrecursionlimit(200000)

def Explore(adj,v, visiting):
    visiting[v] = 1
    for w in adj[v]:
        if visiting[w] == 0:
            Explore(adj,w, visiting) 
    return visiting

def DFS(adj):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(adj)):
            visited[i] = Explore(adj,i, visited[i])
    return visited
           
def number_of_strongly_connected_components(adj):
    visited = DFS(adj)
    li = [0 for i in range(len(adj))]
    result = 0
    for i in range(len(adj)):
        if li[i] == 0:
            result = result + 1
            li[i] = result
            for j in range(i+1,len(adj)):
                if li[j] == 0 and visited[i][j] == 1 and visited[j][i] == 1:
                    li[j] = result
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]  
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))