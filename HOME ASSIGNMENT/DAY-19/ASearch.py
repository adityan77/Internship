def astar(grid, start, goal, heuristic):
    open_list = [(0 + heuristic(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(grid, current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return None
