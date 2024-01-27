import heapq

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_row = (state[i] - 1) // 3
            goal_col = (state[i] - 1) % 3
            current_row = i // 3
            current_col = i % 3
            distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance

def astar(initial_state):
    open_set = [(heuristic(initial_state), 0, initial_state)]
    closed_set = set()

    while open_set:
        _, cost, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            return current_state, cost

        closed_set.add(tuple(current_state))

        blank_idx = current_state.index(0)
        possible_moves = [i for i in range(9) if abs(blank_idx - i) == 1 or abs(blank_idx - i) == 3]
        
        for move in possible_moves:
            next_state = current_state[:]
            next_state[blank_idx], next_state[move] = next_state[move], next_state[blank_idx]

            if tuple(next_state) not in closed_set:
                heapq.heappush(open_set, (heuristic(next_state) + cost + 1, cost + 1, next_state))

initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]

solution, solution_cost = astar(initial_state)

print("Solution found:")
for i in range(0, 9, 3):
    print(solution[i:i+3])
print(f"Solution cost: {solution_cost}")

def print_solution_steps(state):
    if state == goal_state:
        return
    blank_idx = state.index(0)
    possible_moves = [i for i in range(9) if abs(blank_idx - i) == 1 or abs(blank_idx - i) == 3]
    for move in possible_moves:
        next_state = state[:]
        next_state[blank_idx], next_state[move] = next_state[move], next_state[blank_idx]
        if tuple(next_state) in closed_set:
            print_solution_steps(next_state)
            print(next_state)
            break

print("Solution path:")
print(initial_state)
closed_set = set(map(tuple, [initial_state]))
print_solution_steps(initial_state)
