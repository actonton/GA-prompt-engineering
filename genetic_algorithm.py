# from selection import selection
# from crossover import crossover
# from mutation import mutation
# from prompt_initial_generation import *
# from ollama_prompt_generator import *
# import random

# # def generate_generation_0(initial_words, extra_info):
# #     # Assuming each element in initial_words is a list of words
# #     prompt = ' '.join(' '.join(words) for words in initial_words)
# #     return f"{prompt} - {extra_info}"

# def genetic_algorithm(initial_words, number_of_prompts, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate):
#     #population = [generate_generation_0(initial_words, 10) for _ in range(number_of_prompts)]
#     print("Running Genetic Algorithm")
#     population = generate_generation_0(initial_words, number_of_prompts)

#     new_population =  selection(population, number_of_prompts_to_select)
#     for _ in range(2):

#         for i in range(0, len(new_population), 2):
#             child1, child2 = crossover(selected_prompts[random.randint(0, len(selected_prompts) - 1)], selected_prompts[random.randint(0, len(selected_prompts) - 1)], crossover_rate)
#             new_population.append(mutation(child1, mutation_rate))
#             new_population.append(mutation(child2, mutation_rate))




#     return new_population

# # print(genetic_algorithm(["Movie Batman", "Movie Mafia", "King Lear Movie"], 1, 1, 0.2, 0.9))

# initial_words = ollama_generation()
# number_of_prompts = 10
# number_of_prompts_to_select = 4
# number_of_movies_to_compare_against = 5
# mutation_rate = 0.1
# crossover_rate = 0.8

# result_population = genetic_algorithm(initial_words, number_of_prompts, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate)
# #print(result_population)


# for result in result_population:
#     print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#     print(result)


from selection import selection
from crossover import crossover
from mutation import mutation
from prompt_initial_generation import *
from ollama_prompt_generator import *
from fitness import batch_fitness, fitness
import random

# def generate_generation_0(initial_words, extra_info):
#     # Assuming each element in initial_words is a list of words
#     prompt = ' '.join(' '.join(words) for words in initial_words)
#     return f"{prompt} - {extra_info}"

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

    return best_individual

# Example usage
initial_words = ollama_generation()
number_of_generations = 5
population_size = 20
number_of_prompts_to_select = 10
number_of_movies_to_compare_against = 3
mutation_rate = 0.1
crossover_rate = 0.8

best_solution = genetic_algorithm(initial_words, number_of_generations, population_size, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate)
print("Best Solution:", best_solution)