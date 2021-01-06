#Uses python3

def bipartite(adj):
    seta =set()
    setb =set()
    for i in range(len(adj)):
        if i not in seta and i not in setb:
            seta.add(i)
        if i in seta:
            setb.update(adj[i])
        elif i in setb:
            seta.update(adj[i])
    if len(seta.intersection(setb)) > 0:
        return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)] 
    initial = -1
    for i in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
