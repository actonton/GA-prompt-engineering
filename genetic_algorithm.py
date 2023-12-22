from selection import selection
from crossover import crossover
from mutation import mutation
from prompt_initial_generation import *
from ollama import *
from fitness import batch_fitness, fitness
import random


def genetic_algorithm(initial_words, number_of_generations, population_size, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate):
    best_individual = None
    best_fitness = 0

    print("Running Genetic Algorithm")

    # Initialize the first generation
    population = generate_generation_0(initial_words, population_size)

    for generation in range(number_of_generations):
        # Evaluate fitness
        #fitness_scores = [fitness(i,  number_of_movies_to_compare_against) for i in population]
        #fitness_scores = fitness(population, number_of_movies_to_compare_against)
        fitness_scores = batch_fitness(population, number_of_movies_to_compare_against)

        # Select individuals for crossover
        selected_prompts = selection(population, fitness_scores, number_of_prompts_to_select)

        # Create the new population
        new_population = []
        for _ in range(population_size // 2):
            parent1 = selected_prompts[random.randint(0, len(selected_prompts) - 1)]
            parent2 = selected_prompts[random.randint(0, len(selected_prompts) - 1)]
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            new_population.append(mutation(child1, mutation_rate))
            new_population.append(mutation(child2, mutation_rate))

        # Update the current population with the new one
        population = new_population

        # Update the best individual
        best_index = fitness_scores.index(max(fitness_scores))
        if fitness_scores[best_index] > best_fitness:
            best_individual = population[best_index]
            best_fitness = fitness_scores[best_index]

        # Print information about the current generation
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    return best_individual, best_fitness




def call_genetic_algorithm(initial_words):
    number_of_generations = 5
    population_size = 20
    number_of_prompts_to_select = 10
    number_of_movies_to_compare_against = 3
    mutation_rate = 0.1
    crossover_rate = 0.8
    return genetic_algorithm(initial_words, number_of_generations, population_size, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate)
