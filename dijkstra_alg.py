from indexed_priority_queue import IndexPriorityQueue

graph = [[1, 3, 4], [2, 3], [4], [1, 2, 4], []]
routes = [[0, 10, -1, 30, 100], [-1, 0, 50, 40, -1], [-1, -1, 0, -1, 10], [-1, 40, 20, 0, 60], [-1, -1, -1, -1, 0]]
result_len = [-1 for i in range(len(graph))]
begin = int(input(f"Введите начальную вершину (от 1 до {len(graph)}): ")) - 1

result_rotes = {i: [] for i in range(len(graph))}

ipq = IndexPriorityQueue(False)
for i in range(len(graph)):
    ipq.push(i, float('inf'))
ipq.changeAtKey(begin, 0)

while not ipq.empty():
    top = ipq.pop() #[номер вершины, расстояние]
    result_len[top[0]] = top[1]
    for x in graph[top[0]]:
        value = ipq.get_val(x)
        if value is not None:
            if value > top[1] + routes[top[0]][x]:
                ipq.changeAtKey(x, top[1] + routes[top[0]][x])
                result_rotes[x] = result_rotes[top[0]].copy()
                result_rotes[x].append(top[0])


print(f"Кратчайшие пути: {result_len}")

for x in result_rotes:
    print(x+1, ": ", end="")
    rout = ""
    for y in result_rotes[x]:
        rout += str(y+1) + " -> "
    if result_rotes[x]: # если пути найдены и в списке не пусто
        rout += str(x+1)
    print(rout)


