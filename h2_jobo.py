# Steven LeVasseur
# Ethan Fidler
# Joseph Brayshaw
# Neil McGrogan
# Homework 24

# {city_start: [(city_dest1, dist1), [city_dest2, dist2]],
#  city_dest1: [(city_dest3, dist3), (city_start, dist1)]}
# key: city_name (string)
# value: List of tuples

from queue import PriorityQueue

road_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest': [('Giurgiu', 90), ('Urziceni', 85), ('Fagaras', 211), ('Pitesti', 101)],
    'Craiova': [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Pitesti': [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)],
    'Rimnicu Vilcea': [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)]
}

road_map_nonums = {  # still singleton tuples though
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Bucharest': ['Giurgiu', 'Urziceni', 'Fagaras', 'Pitesti'],
    'Craiova': ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Neamt': ['Iasi'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Craiova', 'Pitesti', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Zerind': ['Arad', 'Oradea']
}

road_map_dists = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def r_dfs(graph, start, visited=set(), path=[]):  # graph: list, start: string
    path.append(start)
    visited.add(start)
    if start == 'Bucharest':
        return path
    for city in graph[start]:
        if city not in visited:
            result = r_dfs(graph, city, visited=visited, path=path)
            if result is not None:
                return result
    path.pop()
    return None


def best_first(start):
    p_queue = PriorityQueue()
    p_queue.put((road_map_dists[start], start))

    visited = {}

    for location in road_map.keys():
        visited[location] = False

    while not p_queue.empty():
        curr = p_queue.get()[1]
        print(f"{curr} ")

        if curr == "Bucharest":
            break

        for neighbor in road_map_nonums[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                p_queue.put((road_map_dists[neighbor], neighbor))


best_first("Drobeta")

# result = best_first(road_map_nonums, "Arad")
# print(result)

# result = w_dfs(road_map_nonums, "Arad")
# print(result)

"""
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
"""

# A* search summarized:
# You'll need to implement a queue
# From you starting city, look at each neighbor's straight line distance to Bucharest
# Go to the neighbor with the shortest straight line distance and add others to queue in order
# Evaluate new city's neighbors, adding distance travelled already to their straightline distances
# IF the new city's neighbor's straightline distance + distance travelled already
# is HIGHER than that of one of the other city's in the queue, the neighbor goes behind that city in the queue
# Essentially, every time we consider a new city to go to,
# we consider all cities that we can reach by ANY city we already visited
# See 4-InformedSearch.pdf to see it in action
