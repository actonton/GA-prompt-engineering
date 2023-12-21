from random import randint

from fitness import fitness

#fitness proportionate ”roulette-wheel” selection
def selection(prompts_array, fitness_scores,  number_of_prompts_to_select):
    print("Running Selection")
    best_prompt = randint(0, len(prompts_array)-1)
    #best_score = fitness(prompts_array[best_prompt], number_of_prompts_to_select)
    best_score = fitness_scores[best_prompt]
    selected_prompts = [prompts_array[best_prompt]]
    for i in range(0, number_of_prompts_to_select):
        #picked_prompt = prompts_array[randint(0, len(prompts_array)-1)]
        #picked_prompt_fitness =  fitness(picked_prompt, number_of_prompts_to_select)
        picked_prompt_index = randint(0, len(prompts_array)-1)
        picked_prompt_fitness = fitness_scores[picked_prompt_index]
        if picked_prompt_fitness> best_score:
            best_score = picked_prompt_fitness
            selected_prompts.append(prompts_array[picked_prompt_index])
    return selected_prompts

# print(selection(["Movie Batman", "Movie Mafia", "King Lear Movie"], 1))