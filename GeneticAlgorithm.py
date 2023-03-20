import random, heapq

class GeneticAlgorithm:
    def __init__(self, init_state, n):
        self.n = n
        self.init_state = init_state
        self.generation = 0

    def initialize_population(self, n):
        pop_list = []
        num = random.randint(2, n)
        while num != 0:
            temp = [random.randint(0, self.n - 1) for _ in range(self.n)]
            heapq.heappush(pop_list, (self.fitness(temp), temp))
            num -= 1
        return pop_list

    def fitness(self, cur_state):
        collisions = 0
        for i in range(len(cur_state)):
            for j in range(i + 1, len(cur_state)):
                if cur_state[i] == cur_state[j] or abs(cur_state[i] - cur_state[j]) == j - i:
                    collisions += 1
        return collisions

    def goal_test(self, population: list):
        for i in population:
            if self.fitness(i[1]) == 0:
                return i[1]
        return None

    def random_pick(self, population):
        new_population = []
        n = random.randint(2, len(population))
        for i in range(n):
            new_population.append(population[i][1])
        return new_population

    def crossover(self, parent1, parent2):
        p_len = len(parent1)
        cross_point = random.randint(0, p_len - 1)
        return parent1[:cross_point] + parent2[cross_point:p_len], parent2[:cross_point] + parent1[cross_point:p_len]

    def mutate(self, state):
        state_len = len(state)
        mutate_point = random.randint(0, state_len - 1)
        mutation = random.randint(0, state_len - 1)
        state[mutate_point] = mutation
        return state

    def solve(self):
        population = self.initialize_population(self.n)
        heapq.heappush(population, (self.fitness(self.init_state), self.init_state))
        result = self.goal_test(population)

        while result == None:
            random_pop = self.random_pick(population)
            for i in range(0, len(random_pop), 2):
                if i + 2 <= len(random_pop):
                    #Crossover
                    random_pop[i], random_pop[i + 1] = self.crossover(random_pop[i], random_pop[i + 1])

                    #mutate
                    random_pop[i] = self.mutate(random_pop[i])
                    random_pop[i + 1] = self.mutate(random_pop[i + 1])
                
            for board in random_pop:
                population.pop()
            for board in random_pop:
                heapq.heappush(population, (self.fitness(board), board))
            result = self.goal_test(population)

        return result