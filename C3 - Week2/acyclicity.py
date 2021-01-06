#Uses python3

def Previsit(v,clock,pre):
    pre[v] = clock[0]
    clock[0] = clock[0] +1

def Postvisit(v,clock,post):
    post[v] = clock[0]
    clock[0] = clock[0] +1

def Explore(adj,v, visited,result,clock,pre,post):
    visited[v] = result
    Previsit(v,clock,pre)
    for w in adj[v]:
        if visited[w] == 0:
            Explore(adj,w, visited,result,clock,pre,post)
    Postvisit(v,clock,post)
    return clock        

def DFS(adj,initial):
    result = 0
    visited = [0 for _ in range(n)]
    pre = [0 for i in range(n)]
    post = [0 for i in range(n)]
    clock = [1]
    for i in range(len(adj)):
        if visited[initial] == 0 and initial != 0:
            result = result +1
            Explore(adj,initial, visited,result,clock,pre,post)
        if visited[i] == 0:
            result = result +1
            Explore(adj,i, visited,result,clock,pre,post)    
    return post
           
def acyclic(adj,initial,m):
    post = DFS(adj,initial)
    for i in range(len(adj)):
        for j in adj[i]:
            if post[i] <= post[j]:
                return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]  
    initial = 0
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        if i ==0:
            initial = a-1
    print(acyclic(adj,initial,m))