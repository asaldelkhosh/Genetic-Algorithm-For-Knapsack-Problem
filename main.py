import random



def generate_initial_population(count=6) -> List[Individual]:
    population = set()

    # generate initial population having `count` individuals
    while len(population) != count:
        # pick random bits one for each item and 
        # create an individual 
        bits = [
            random.choice([0, 1])
            for _ in items
        ]
        population.add(Individual(bits))

    return list(population)


def fitness(self) -> float:
    total_value = sum([
        bit * item.value
        for item, bit in zip(items, self.bits)
    ])

    total_weight = sum([
        bit * item.weight
        for item, bit in zip(items, self.bits)
    ])

    if total_weight <= MAX_KNAPSACK_WEIGHT:
        return total_value

    return 0


def selection(population: List[Individual]) -> List[Individual]:
    parents = []

    # randomly shuffle the population
    random.shuffle(population)

    # we use the first 4 individuals
    # run a tournament between them and
    # get two fit parents for the next steps of evolution

    # tournament between first and second
    if population[0].fitness() > population[1].fitness():
        parents.append(population[0])
    else:
        parents.append(population[1])

    # tournament between third and fourth
    if population[2].fitness() > population[3].fitness():
        parents.append(population[2])
    else:
        parents.append(population[3])

    return parents
