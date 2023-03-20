from UCS import UCS
from AStar import AStar
from GeneticAlgorithm import GeneticAlgorithm
import time, tracemalloc, random

def print_board(state, n):
    result = [['.' for j in range(n)] for i in range(n)]
    for i in range(n):
        result[state[i]][i] = 'Q'
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=' ')
        print()

NUM_RUN_TIME = 3

if __name__ == '__main__':
    t = []
    mem = []

    n = int(input("Enter the number of queens: "))
    init_state = [random.randint(0, n - 1) for _ in range(n)] #randomly generated an initial state

    print("1. UCS")
    print("2. A*")
    print("3. Genetic algorithm")
    choice = int(input("Your choice: "))

    if choice == 1:
        problem = UCS(init_state, n)
    if choice == 2:
        problem = AStar(init_state, n)
    if choice == 3:
        problem = GeneticAlgorithm(init_state, n)

    for i in range(NUM_RUN_TIME):
        tracemalloc.start() #start tracking memory usage
        start_time = time.time() #start tracking running time

        solution = problem.solve()

        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        t.append(time.time() - start_time)
        mem.append(peak / 1024**2)

        if solution is None:
            print("No solution found")
        else:
            print(f"Solution in test {i + 1}:")
            print_board(solution, n)

    print(f"Avarage running time: {sum(t) / NUM_RUN_TIME:.4f} seconds")
    print(f"Memory usage: {sum(mem) / NUM_RUN_TIME:.2f} MB")