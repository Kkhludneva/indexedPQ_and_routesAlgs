
graph = [[1, 3, 4], [2, 3], [4], [1, 2, 4], []]
routes = [[0, 10, 0, -10, 100], [0, 0, 50, 40, 0], [0, 0, 0, 0, 10], [0, 40, -20, 0, 60], [0, 0, 0, 0, 0]]
result_rotes = {i: [] for i in range(len(graph))}

result_len = [float('inf') for i in range(len(graph))]
begin = int(input(f"Введите начальную вершину (от 1 до {len(graph)}): ")) - 1
result_len[begin] = 0

for i in range(len(graph)-2):
    for u in range(len(graph)):
        for v in graph[u]:
            if result_len[v] > result_len[u] + routes[u][v]:
                result_len[v] = result_len[u] + routes[u][v]
                result_rotes[v] = result_rotes[u].copy()
                result_rotes[v].append(u)
    # print(result_len)


print(f"Кратчайшие пути: {result_len}")

for x in result_rotes:
    print(x+1, ": ", end="")
    rout = ""
    for y in result_rotes[x]:
        rout += str(y+1) + " -> "
    if result_rotes[x]: # если пути найдены и в списке не пусто
        rout += str(x+1)
    print(rout)