graph_main = [[3, 5], [2, 3, 4, 5], [1], [0, 1], [1, 5], [0, 1, 4]]


def f_graph_search(graph, l_layer, l_path):

    l_next_layer = []

    l_path.extend(l_layer)

    for node in l_layer:

        for elem in graph[node]:

            if (elem not in l_path) and (elem not in l_next_layer):

                l_next_layer.append(elem)

    if len(l_next_layer) != 0:

        f_graph_search(graph, l_next_layer, l_path)


print(graph_main)

n = int(input('Введите стартовую вершину:'))

l_start = []
l_path_result = []

l_start.append(n)

f_graph_search(graph_main, l_start, l_path_result)

print(l_path_result)
