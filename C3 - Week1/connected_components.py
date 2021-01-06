#Uses python3

def Explore(adj,v, visited,result):
    visited[v] = result
    for w in adj[v]:
        if visited[w] == 0:
            Explore(adj,w, visited,result)

def number_of_components(adj):
    result = 0
    visited = [0 for _ in range(n)]
    for i in range(len(adj)):
        if visited[i] == 0:
            result = result +1
            Explore(adj,i, visited,result)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]  
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))