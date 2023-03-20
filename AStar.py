import heapq

class AStar:
    def __init__(self, init_state, n) -> None:
        self.n = n
        self.init_state = init_state
        self.explored = set()

    def conflicts(self, cur_state):
        count = 0
        for i in range(len(cur_state)):
            for j in range(i + 1, len(cur_state)):
                if cur_state[i] == cur_state[j] or abs(cur_state[i] - cur_state[j]) == j - i:
                    count += 1
        return count

    def successors(self, pState):
        new_board_set = []
        for i in range(self.n):
            for j in range(self.n):
                if j != pState[i]:
                    new_board = pState.copy()
                    new_board[i] = j
                    new_board_set.append(new_board)
        return new_board_set

    def solve(self):
        frontier = [(self.conflicts(self.init_state), 0, self.init_state)]
        open_list = [frontier]
        while open_list:
            heuristic, cost, current = heapq.heappop(frontier)
            if heuristic == 0:
                return current
            self.explored.add(tuple(current))
            for successor in self.successors(current):
                if tuple(successor) not in self.explored:
                    heapq.heappush(frontier, (self.conflicts(successor), cost + 1, successor))
        return None