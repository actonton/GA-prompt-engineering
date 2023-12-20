from random import randint

from fitness import fitness

#fitness proportionate ”roulette-wheel” selection
def selection(prompts_array, number_of_prompts_to_select):
    best_prompt = randint(0, len(prompts_array))
    best_score = fitness(prompts_array[best_prompt], number_of_prompts_to_select)
    selected_prompts = [prompts_array[best_prompt]]
    for i in range(0, number_of_prompts_to_select):
        picked_prompt = prompts_array[randint(0, len(prompts_array))]
        picked_prompt_fitness =  fitness(picked_prompt, number_of_prompts_to_select)
        if picked_prompt_fitness> best_score:
            best_score = picked_prompt_fitness
            selected_prompts.append(picked_prompt)
    return selected_prompts

# print(selection(["Movie Batman", "Movie Mafia", "King Lear Movie"], 1))