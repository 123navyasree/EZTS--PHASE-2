#bfs
graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
vis = []
queue = []

#bfs-uses queue
def bfs(vis,graph,node):
    vis.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print (m, end= " ")
        
        for neighbour in graph[m]:
            if neighbour not in vis:
                vis.append(neighbour)
                queue.append(neighbour)

bfs(vis,graph, '5')
#dfs-we use stack
vis=set()
def dfs(vis,graph,node):
    if node not in vis:
        print(node)
        vis.add(node)
        for neighbour in graph[node]:
            dfs(vis,graph,neighbour)
dfs(vis,graph,'5')