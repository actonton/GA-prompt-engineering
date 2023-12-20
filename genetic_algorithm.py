from selection import selection
from crossover import crossover
from mutation import mutation
from fitness import fitness
import random

def genetic_algorithm(population, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate):
    selected_prompts = selection(population, number_of_prompts_to_select)
    new_population = []
    for i in range(0, len(selected_prompts), 2):
        child1, child2 = crossover(selected_prompts[random.randint(0, len(selected_prompts) - 1)], selected_prompts[random.randint(0, len(selected_prompts) - 1)], crossover_rate)
        new_population.append(mutation(child1, mutation_rate))
        new_population.append(mutation(child2, mutation_rate))
    return new_population

print(genetic_algorithm(["Movie Batman", "Movie Mafia", "King Lear Movie"], 1, 1, 0.2, 0.9))