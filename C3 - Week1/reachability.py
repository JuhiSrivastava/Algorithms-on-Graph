#Uses python3

def Explore(adj,v, visited):
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            Explore(adj,w, visited)

def reach(adj, x, y):
    #write your code here
    visited = [0 for _ in range(n)]
    Explore(adj,x-1, visited)
    if visited[y-1] == 1:
        return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]  
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = map(int, input().split())
    print(reach(adj, x, y))
