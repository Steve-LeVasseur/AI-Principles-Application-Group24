# Steven LeVasseur
# Ethan Fidler
# Joseph Brayshaw
# Neil McGrogan
# Homework 24

from queue import PriorityQueue

# We have multiple implementations of the map for 
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

road_map_nonums = {
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

road_map_dists = { # Shortest Line Distances
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

# Depth First Search
def dfs(start, graph=road_map_nonums, visited=set(), path=[]):  # graph: list, start: string
    path.append(start)
    visited.add(start)
    if start == 'Bucharest':
        print(f'visited nodes: {len(visited)}')
        return path
    for city in graph[start]:
        if city not in visited:
            result = dfs(city, graph, visited=visited, path=path)
            if result is not None:
                return result
    path.pop()
    return None

# Best First Search
def best_first(start, graph=road_map_nonums, visited=set(), path=[]):
    path.append(start)
    visited.add(start)
    if (start == 'Bucharest'):
        print(f'visited nodes: {len(visited)}')
        return path
    closest_city = graph[start][0] # guess that the first neighbor is closest to Bucharest
    for city in graph[start]: # for each neighboring city
        if city not in visited: # if it hasn't been visited yet
            if road_map_dists[city] < road_map_dists[closest_city]: # check if it's closer to Bucharest than the current 'closest_city
                closest_city = city # Make it the new closest_city if it is
    result = best_first(closest_city, graph, visited=visited, path=path) # Run best first on the closest neighbor to Bucharest
    if result is not None:
        return result
    path.pop()
    return None

# Breadth First Search
def backtrace(parent, start):
    path = ["Bucharest"]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path   

def bfs(start):
    parent = {}
    queue = []
    visited = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == "Bucharest":
            print(f'visited nodes: {len(visited)+1}')
            return backtrace(parent, start)
        for adjacent in road_map_nonums.get(node, []):
            if adjacent not in visited:
                visited.append(adjacent)
                if node not in queue :
                    parent[adjacent] = node # <<<<< record its parent 
                    queue.append(adjacent)


# A*
def a_star(start):
        
    p_queue = PriorityQueue() # form: ((total_dist = prev + SLD, [path]))
    visited = [] # just for checking if a city has already been visited before visiting
    
    curr_city = start

    p_queue.put((road_map_dists[curr_city], [curr_city])) # adding start loc to pq

    while not p_queue.empty(): #isn't empty
        
        temp = p_queue.get() # form: ((total_dist = prev + SLD, [path]))
        path = temp[1] # list of cities travelled to along this path
        curr_city = temp[1][-1] # the city currently being visited
        visited.append(curr_city)
        travelled_dist = temp[0] - road_map_dists[curr_city] # total distance travelled on path so far
        
        if curr_city == "Bucharest":
            print(f'visited nodes: {len(visited)}')
            return path

        for neighbor_to_visit in road_map_nonums[curr_city]:
            if neighbor_to_visit not in visited:
                d = 0 # distance from curr_city to neighbor_to_visit
                new_path = path + [neighbor_to_visit]
                for road in road_map[curr_city]:
                    if road[0] == neighbor_to_visit:
                        d = road[1]
                p_queue.put(((road_map_dists[neighbor_to_visit]+(travelled_dist+d)), new_path))

def testFor(city="Bucharest"):
    print(dfs(city))
    print(best_first(city))
    print(bfs(city))
    print(a_star(city))


testFor("Urziceni")

# Test Result Discussion:
# In our test city of Zerind, we got the following results
# dfs: 6 cities visited. path: ['Zerind', 'Arad', 'Sibiu', 'Fagaras', 'Bucharest']
# best first: 5 cities visited. path: ['Zerind', 'Arad', 'Sibiu', 'Fagaras', 'Bucharest']
# bfs: 13 cities visited. path: ['Zerind', 'Arad', 'Sibiu', 'Fagaras', 'Bucharest']
# a*: 9 cities visited. path: ['Zerind', 'Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

# In our second test city of Drobeta, we got the following results
# dfs: 4 cities visited. path: ['Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
# best first: 4 cities visited. path: ['Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
# bfs: 10 cities visited. path: ['Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
# a*: 5 cities visited. path: ['Drobeta', 'Craiova', 'Pitesti', 'Bucharest']

# In conclusion, we generally say that best first is the best of these search algorithms on this roadmap
# It consistently finds the best path with the fewest cities visited
# Depth first also does fairly well, though that is highly dependent on how the roadmap is assembled
# Breadth first is consistently one of the least efficient algorithms. Taking many more cities visited to reach the answer
# A* is better than breadth first usually. Consistently requiring fewer cities visited.