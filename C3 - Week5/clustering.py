#Uses python3
import math

class Node:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.parent = c
        self.rank = 0

class Edge:
    def __init__(self, a, b, c):
        self.u = a
        self.v = b
        self.weight = c

def MakeSet(i, nodes, x, y):
    nodes.append(Node(x[i], y[i], i))

def weight(x1, y1, x2, y2):
  return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def Find(i, nodes):
  if (i != nodes[i].parent) :
        nodes[i].parent = Find(nodes[i].parent, nodes)
  return nodes[i].parent

def Union(u, v, nodes):
    r1 = Find(u, nodes)
    r2 = Find(v, nodes)
    if (r1 != r2):
        if (nodes[r1].rank > nodes[r2].rank):
            nodes[r2].parent = r1
        else:
            nodes[r1].parent = r2
            if (nodes[r1].rank == nodes[r2].rank):
                nodes[r2].rank += 1

def clustering(x, y, k):
    #write your code here
    n = len(x)
    nodes = []
    for i in range(n):
       MakeSet(i, nodes, x, y)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append(Edge(i, j, weight(x[i], y[i], x[j], y[j])))
    edges = sorted(edges, key=lambda edge: edge.weight)
    union_num = 0
    for edge in edges:
        if Find(edge.u, nodes) != Find(edge.v, nodes):
            union_num += 1
            Union(edge.u, edge.v, nodes)
        if(union_num > n - k):
            return edge.weight
    return -1.

if __name__ == '__main__':
    n = int(input())
    x=[]
    y=[]
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    k = int(input())
    print("{0:.9f}".format(clustering(x, y, k)))
    