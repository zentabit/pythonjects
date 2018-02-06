from random import randint

population = { "pop1": 30 }
population_keys = {"pop1": 2}


for key in population:
    new_key = randint(-10, 10)
    if new_key > 0:
        population['pop'+(str(int(key[2:][1:])+1))] = population[key]
    original = population[key]
    population[key] -= original * 0.2
    population[key] += original * population_keys[key]

print(population)
