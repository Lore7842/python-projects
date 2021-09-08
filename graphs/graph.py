# grafo come matrice delle adiacenze

graph = {
    'adj': [[0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]],

    'edges': [],
    'z': -1,
}


def init(graph):
    for i in range(5):
        for j in range(5):
            if graph['adj'][i][j] == 1:
                graph['edges'].append({
                    'u': i,
                    'v': j,
                })


def dfsR(visited, graph, root):
    visited.add(root)
    print(root+1, end=' ')
    for i in range(5):
        if graph['adj'][root][i] == 1 and i not in visited:
            dfsR(visited, graph, i)


def dfs(graph):
    for i in range(5):
        visited = set()
        print('Dfs dal nodo: {}\n'.format(i+1))
        dfsR(visited, graph, i)
        print('\n')


init(graph)
dfs(graph)
# print(graph)
