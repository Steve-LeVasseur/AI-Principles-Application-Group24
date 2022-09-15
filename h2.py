# Steven LeVasseur
# Ethan Fidler
# Joseph Brayshaw
# Neil McGrogan
# Homework 24

# {city_start: [(city_dest1, dist1), [city_dest2, dist2]],
#  city_dest1: [(city_dest3, dist3), (city_start, dist1)]}
# key: city_name (string)
# value: List of tuples

from tracemalloc import start


road_map = {
    'Arad' : [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest' : [('Giurgiu', 90), ('Urziceni', 85), ('Fagaras', 211), ('Pitesti', 101)],
    'Craiova' : [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Drobeta' : [('Craiova', 120), ('Mehadia', 75)],
    'Eforie' : [('Hirsova', 86)],
    'Fagaras' : [('Bucharest', 211), ('Sibiu', 99)],
    'Giurgiu' : [('Bucharest', 90)],
    'Hirsova' : [('Eforie', 86), ('Urziceni', 98)],
    'Iasi' : [('Neamt', 87), ('Vaslui',92)],
    'Lugoj' : [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia' : [('Drobeta', 75), ('Lugoj', 70)],
    'Neamt' : [('Iasi', 87)],
    'Oradea' : [('Sibiu', 151), ('Zerind', 71)],
    'Pitesti' : [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)],
    'Rimnicu Vilcea' : [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)],
    'Sibiu' : [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara' : [('Arad', 118), ('Lugoj', 111)],
    'Urziceni' : [('Bucharest', 85),('Hirsova', 98) ,('Vaslui', 142)],
    'Vaslui' : [('Iasi', 92), ('Urziceni', 142)],
    'Zerind' : [('Arad', 75), ('Oradea', 71)]
}

road_map_nonums = { # still singleton tuples though
    'Arad' : ['Zerind', 'Sibiu', 'Timisoara'],
    'Bucharest' : ['Giurgiu', 'Urziceni', 'Fagaras', 'Pitesti'],
    'Craiova' : ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'],
    'Drobeta' : ['Craiova', 'Mehadia'],
    'Eforie' : ['Hirsova'],
    'Fagaras' : ['Bucharest', 'Sibiu'],
    'Giurgiu' : ['Bucharest'],
    'Hirsova' : ['Eforie', 'Urziceni'],
    'Iasi' : ['Neamt', 'Vaslui'],
    'Lugoj' : ['Mehadia', 'Timisoara'],
    'Mehadia' : ['Drobeta', 'Lugoj'],
    'Neamt' : ['Iasi'],
    'Oradea' : ['Sibiu', 'Zerind'],
    'Pitesti' : ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea' : ['Craiova', 'Pitesti', 'Sibiu'],
    'Sibiu' : ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara' : ['Arad', 'Lugoj'],
    'Urziceni' : ['Bucharest','Hirsova' ,'Vaslui'],
    'Vaslui' : ['Iasi', 'Urziceni'],
    'Zerind' : ['Arad', 'Oradea']
}

road_map_dists = {
    'Arad' : 366,
    'Bucharest' : 0,
    'Craiova' : 160,
    'Drobeta' : 242,
    'Eforie' : 161,
    'Fagaras' : 176,
    'Giurgiu' : 77,
    'Hirsova' : 151,
    'Iasi' : 226,
    'Lugoj' : 244,
    'Mehadia' : 241,
    'Neamt' : 234,
    'Oradea' : 380,
    'Pitesti' : 100,
    'Rimnicu Vilcea' : 193,
    'Sibiu' : 253,
    'Timisoara' : 329,
    'Urziceni' : 80,
    'Vaslui' : 199,
    'Zerind' : 374
}





# Using a Python dictionary to act as an adjacency list
# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

potential_routes = set()

def dfs_why(visited, road_map, city):
    if city not in visited: # don't revisit cities we've already visited
        visited.add(city) # visit city if we haven't visited it yet
        for bordering_city in road_map[city]: # not proper syntax
            dfs_why(visited, road_map, bordering_city)

# some code here that finds the best route in potential_routes 
    # either based on distance or num cities visited
# print the best route

# Driver Code
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')

def w_dfs(graph, start, visited=set(), path=[]): # graph: list, start: string
    path.append(start)
    visited.add(start)
    if (start == 'Bucharest'):
        return path
    for city in graph[start]:
        if (city not in visited):
            result = w_dfs(graph, city, visited=visited, path=path)
            if result is not None:
                return result
    path.pop()
    return None


def best_first(graph, start, visited=set(), path=[]):
    path.append(start)
    visited.add(start)
    if (start == 'Bucharest'):
        return path
    # This part needs to be different
    # Need to evaluate connected cities and order them by
    # shortest straight line distance to Bucharest

    # Right now I only run it on the closest city
    # Still thinking about how to make a proper queue with proper ordering
    closest_city = graph[start][0] # guess that the first neighbor is closest to Bucharest
    for city in graph[start]: # for each neighboring city
        if city not in visited: # if it hasn't been visited yet
            if road_map_dists[city] < road_map_dists[closest_city]: # check if it's closer to Bucharest than the current 'closest_city
                closest_city = city # Make it the new closest_city if it is
    # I only run best first on the closest neighbor to Bucharest
    # all the neighbors should be added to a queue in some way in the final product
    result = best_first(graph, closest_city, visited=visited, path=path) # Run best first on the closest neighbor to Bucharest
    if result is not None:
        return result
    path.pop()
    return None    

result = best_first(road_map_nonums, "Arad")
print(result)

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
