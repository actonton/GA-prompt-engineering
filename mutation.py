from numpy.random import rand
from wonderwords import RandomWord
import random

def mutation(prompt, mutation_rate):
    prompt_array = prompt.split()

    for index  in range(len(prompt_array)):
        if rand() < mutation_rate:
            prompt_array[index] = RandomWord().word()

    if rand() < mutation_rate:
        random.shuffle(prompt_array)

    return ' '.join(prompt_array)

# print(mutation("Movie Batman, Omega Shadow", 0.2))

