from selection import selection
from crossover import crossover
from mutation import mutation
from prompt_initial_generation import *
from ollama_prompt_generator import *
import random

# def generate_generation_0(initial_words, extra_info):
#     # Assuming each element in initial_words is a list of words
#     prompt = ' '.join(' '.join(words) for words in initial_words)
#     return f"{prompt} - {extra_info}"

def genetic_algorithm(initial_words, number_of_prompts, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate):
    #population = [generate_generation_0(initial_words, 10) for _ in range(number_of_prompts)]
    print("Running Genetic Algorithm")
    population = generate_generation_0(initial_words, number_of_prompts)

    new_population = []
    selected_prompts = selection(population, number_of_prompts_to_select)
    for _ in range(2):

        for i in range(0, len(new_population), 2):
            child1, child2 = crossover(selected_prompts[random.randint(0, len(selected_prompts) - 1)], selected_prompts[random.randint(0, len(selected_prompts) - 1)], crossover_rate)
            new_population.append(mutation(child1, mutation_rate))
            new_population.append(mutation(child2, mutation_rate))




    return new_population

# print(genetic_algorithm(["Movie Batman", "Movie Mafia", "King Lear Movie"], 1, 1, 0.2, 0.9))

initial_words = ollama_generation()
number_of_prompts = 10
number_of_prompts_to_select = 4
number_of_movies_to_compare_against = 5
mutation_rate = 0.1
crossover_rate = 0.8

result_population = genetic_algorithm(initial_words, number_of_prompts, number_of_prompts_to_select, number_of_movies_to_compare_against, mutation_rate, crossover_rate)
#print(result_population)


for result in result_population:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)