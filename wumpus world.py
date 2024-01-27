import heapq

# Define the Wumpus World grid
grid = [[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]

# Define the initial state of the agent
start = (0, 0)

# Define the goal state of the agent
goal = (3, 3)

# Define the possible actions of the agent
actions = ["up", "down", "left", "right"]

# Define the heuristic function


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Define the A* algorithm


def a_star(grid, start, goal, actions):
    # Create a priority queue for storing the states to be explored
    heap = []
    heapq.heappush(heap, (0, start))
    # Create a dictionary for storing the cost of reaching each state
    cost = {start: 0}
    # Create a dictionary for storing the came from information for each state
    came_from = {start: None}
    # While the priority queue is not empty
    while heap:
        # Get the state with the lowest cost
        current = heapq.heappop(heap)[1]
        # If the current state is the goal state, return the came from information
        if current == goal:
            return came_from
        # For each possible action
        for action in actions:
            # Compute the next state
            if action == "up":
                next_state = (current[0] - 1, current[1])
            elif action == "down":
                next_state = (current[0] + 1, current[1])
            elif action == "left":
                next_state = (current[0], current[1] - 1)
            elif action == "right":
                next_state = (current[0], current[1] + 1)
            # If the next state is outside of the grid, skip it
            if next_state[0] < 0 or next_state[0] >= len(grid) or next_state[1] < 0 or next_state[1] >= len(grid[0]):
                continue
            # If the next state is a wall, skip it
            if grid[next_state[0]][next_state[1]] == 1:
                continue
            # Compute the cost of reaching the next state
            new_cost = cost[current] + 1
            # If the next state has not been visited yet or if the new cost is lower than the previous cost
            if next_state not in cost or new_cost < cost[next_state]:
                # Update the cost of reaching the next state
                cost[next_state] = new_cost
                # Update the came from information for the next state
                came_from[next_state] = current
                # Add the next state to the priority queue
                heapq.heappush(
                    heap, (new_cost + heuristic(next_state, goal), next_state))

    # If the # If the loop completes without finding a path, return None
                return None
            path = a_star(grid, start, goal, actions)
            if path is not None:

                    # Create an empty list for storing the path
                    path_list = [goal]
                    # Get the current state
                    current = goal
                    # While the current state is not the start state
            while current != start:
                    # Get the previous state
                    current = path[current]
                    # Add the previous state to the path list
                    path_list.append(current)
                    # Print the path in reverse order
                    print(path_list[::-1])
            else:
                    print("No path found")
        