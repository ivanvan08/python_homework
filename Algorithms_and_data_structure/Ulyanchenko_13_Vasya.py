def vasya(old_graph):
    new_graph = [[] for i in old_graph]
    for v in range(len(old_graph)):
        for w in old_graph[v]:
            new_graph[w].append(v)
    print(new_graph)


if __name__ == '__main__':
    first_graph = [[1, 2], [2], [], [1]]
    second_graph = [[1], [0]]
    vasya(first_graph)
    vasya(second_graph)
