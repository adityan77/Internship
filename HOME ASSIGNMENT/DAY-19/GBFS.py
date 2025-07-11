import heapq

def gbfs(grid, start, goal, heuristic):
    open_list = [(heuristic(start, goal), start)]
    came_from = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        visited.add(current)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))

    return None
