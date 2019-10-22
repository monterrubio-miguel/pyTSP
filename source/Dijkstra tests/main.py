from graph import *
from queue import PriorityQueue
from math import inf

# Helper function
# To avoid neighbours already visited
def neighbourNotDone(search_by_name, doneArr):
    for element in doneArr:
        name = element[0]
        if name == search_by_name:
            return False
    return True

pq = PriorityQueue()
# initialize priority queue
# tuple meaning/formatting = (cost, node_name, path_via)
pq.put((0, 'start', '-'))
min_distances = {}

# Initialize costs
# set the minimum cost/distance. cost to start = 0 and all other const are infinite
for key, value in graph.graph_dict.items():
    if key == 'start':
        min_distances[key] = 0
    else:
        min_distances[key] = inf

visited = []
# Default values
current = (0, '')
current_name = ''
while current_name != 'end':
    current_cost, current_name, path_via = pq.get()
    for neighbour_name, neighbour_weight in graph.graph_dict[current_name]:
        # if neighbour not in done array
        if neighbourNotDone(neighbour_name, visited):
            cost = current_cost + neighbour_weight
            # replace priority queue value when the cost is less
            if min_distances[neighbour_name] > cost:
                min_distances[neighbour_name] = cost
                pq.put((cost, neighbour_name, current_name))
    visited.append((current_name, path_via))


print(visited)
# Backtrack on done array to get the shortest path
ans = []
connection = 'end'
for element in reversed(visited):
    if connection == element[0]:
        ans.append(connection)
        connection = element[1]
ans.reverse()
print('shortest path: ', ans)



