from queue import Queue
def bfs(n, m, edges, s):
    # Write your code here
    adj_lst=[[] for i in range(n+1)]
    for edge in edges:
        adj_lst[edge[0]-1].append(edge[1]-1)
        adj_lst[edge[1]-1].append(edge[0]-1)
    q=Queue()
    q.put(s-1)
    dist=[-1]*(n)
    dist[s-1]=0
    visited=set([s-1])
    while q.empty()==False:
        curr=q.get()
        for node in adj_lst[curr]:
            if node not in visited:
                dist[node]=6+dist[curr]
                q.put(node)
                visited.add(node)
    del dist[s-1]
    return dist