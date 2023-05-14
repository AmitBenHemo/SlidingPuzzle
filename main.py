from queue import Queue, PriorityQueue


with open('input.txt', 'r') as f:
    algorithm_code = int(f.readline().strip())
    n = int(f.readline().strip())
    state = f.readline().strip().split('-')
    state = [int(x) for x in state]


# Define heuristic function for the defined search strategy
def manhattan_distance(state):
    # Compute manhattan distance heuristic
    distance = 0
    for i in range(n):
        for j in range(n):
            if state[i*n+j] == n*n-1:
                continue
            row = state[i*n+j] // n
            col = state[i*n+j] % n
            distance += abs(row-i) + abs(col-j)
    return distance


def move_left(n, state, empty_index):
    if empty_index % n == 0:
        return None
    new_state = state.copy()
    new_state[empty_index], new_state[empty_index-1] = new_state[empty_index-1], new_state[empty_index]
    return new_state, empty_index-1

def move_right(n, state, empty_index):
    if empty_index % n == n-1:
        return None
    new_state = state.copy()
    new_state[empty_index], new_state[empty_index+1] = new_state[empty_index+1], new_state[empty_index]
    return new_state, empty_index+1

def move_up(n, state, empty_index):
    if empty_index < n:
        return None
    new_state = state.copy()
    new_state[empty_index], new_state[empty_index-n] = new_state[empty_index-n], new_state[empty_index]
    return new_state, empty_index-n

def move_down(n, state, empty_index):
    if empty_index >= n*(n-1):
        return None
    new_state = state.copy()
    new_state[empty_index], new_state[empty_index+n] = new_state[empty_index+n], new_state[empty_index]
    return new_state, empty_index+n


def ids(n, state):
    for depth in range(1000):
        path = dfs(state, state.index(0), [], depth)
        if path is not None:
            return path
    return None

def dfs(state, empty_index, path, depth_limit):
    if state == list(range(1, n*n)) + [0]:
        return path
    if depth_limit == 0:
        return None
    close_list = set()
    for move_func, move_dir in [(move_left, 'L'), (move_right, 'R'), (move_up, 'U'), (move_down, 'D')]:
        next_state = move_func(n, state, empty_index)
        if next_state is not None and tuple(next_state[0]) not in close_list:
            new_path = path + [move_dir]
            close_list.add(tuple(next_state[0]))
            res = dfs(next_state[0], next_state[1], new_path, depth_limit-1)
            if res is not None:
                return res
    return None


def bfs(n, state):
    q = Queue()
    q.put((state, state.index(0), []))
    close_list = set()
    while not q.empty():
        current_state, empty_index, path = q.get()
        if current_state == list(range(1, n*n)) + [0]:
            return path
        close_list.add(tuple(current_state))
        for move_func, move_dir in [(move_left, 'L'), (move_right, 'R'), (move_up, 'U'), (move_down, 'D')]:
            next_state = move_func(n, current_state, empty_index)
            if next_state is not None and tuple(next_state[0]) not in close_list:
                q.put((next_state[0], next_state[1], path + [move_dir]))
    return None

def heuristic(state):
    # Compute the Manhattan distance as the heuristic
    dist = 0
    n = int(len(state) ** 0.5)
    for i in range(n):
        for j in range(n):
            val = state[i*n + j]
            if val != 0:
                row, col = (val-1) // n, (val-1) % n
                dist += abs(row - i) + abs(col - j)
    return dist

def a_star(n, state):
    q = PriorityQueue()
    q.put((heuristic(state), state, state.index(0), []))
    close_list = set()
    while not q.empty():
        _, current_state, empty_index, path = q.get()
        if current_state == list(range(1, n*n)) + [0]:
            return path
        close_list.add(tuple(current_state))
        for move_func, move_dir in [(move_left, 'L'), (move_right, 'R'), (move_up, 'U'), (move_down, 'D')]:
            next_state = move_func(n, current_state, empty_index)
            if next_state is not None and tuple(next_state[0]) not in close_list:
                priority = len(path) + 1 + heuristic(next_state[0])
                q.put((priority, next_state[0], next_state[1], path + [move_dir]))
    return None


def ida_star(n, state):
    threshold = heuristic(state)
    path = []
    while True:
        result, new_threshold = search(state, path, 0, threshold, n)
        if result is not None:
            return result
        if new_threshold == float('inf'):
            return None
        threshold = new_threshold

def search(state, path, g, threshold, n):
    f = g + heuristic(state)
    if f > threshold:
        return None, f
    if state == list(range(1, n*n)) + [0]:
        return path, f
    min_cost = float('inf')
    empty_index = state.index(0)
    for move_func, move_dir in [(move_left, 'L'), (move_right, 'R'), (move_up, 'U'), (move_down, 'D')]:
        next_state = move_func(n, state, empty_index)
        if next_state is not None and path[-1:] != move_dir:
            new_path = path + [move_dir]
            result, new_threshold = search(next_state[0], new_path, g + 1, threshold, n)
            if result is not None:
                return result, f
            min_cost = min(min_cost, new_threshold)
    return None, min_cost

def write_output(path):
    with open('output.txt', 'w') as f:
        f.write(''.join(path))
    
if(algorithm_code==1):
    write_output(ids(n, state))
if(algorithm_code==2):
    write_output(bfs(n, state))
if(algorithm_code==3):
    write_output(a_star(n, state))
if(algorithm_code==4):
    write_output(ida_star(n, state))
