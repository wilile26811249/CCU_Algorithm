def bellman_ford(graph, source):
    # Step1: Prepare the distance and predecessor for each ndoe
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float("inf"), None
    distance[source] = 0

    # Step2: Relax(Bottom up)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    return distance, predecessor

def trace(predecessor, target):
    path = [target]
    while predecessor[target] != None:
        path.append(predecessor[target])
        target = predecessor[target]

    for node in path[::-1]:
        print(node, end = '')
        if node != path[0]:
            print(' -> ', end = '')

if __name__ == '__main__':
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }

    distance, predecessor = bellman_ford(graph, source = 'a')
    print(distance)
    trace(predecessor, 'd')