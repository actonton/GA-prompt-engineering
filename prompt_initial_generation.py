from random import randint
from wonderwords import RandomWord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from ollama import ollama_generation

sentimentAnalyzer = SentimentIntensityAnalyzer()
# target_output = ollama_generation()

def measure_difference(word_a,  word_b):
    output_scores = sentimentAnalyzer.polarity_scores(word_a)
    target_scores = sentimentAnalyzer.polarity_scores(word_b)
    diff = abs(output_scores['neg'] - target_scores['neg']) + \
           abs(output_scores['neu'] - target_scores['neu']) + \
           abs(output_scores['pos'] - target_scores['pos'])
    return diff


# generating initial prompt
# takes in data an array of words
def generate_prompt(initial_words, target_output):
    print("Generating Prompt")
    #target_scores = sentimentAnalyzer.polarity_scores(target_output)
    r = RandomWord()
    #additional_words = [r.word(include_parts_of_speech=["adjectives"]) for _ in range(len(initial_words))]
    additional_words = []
    initial_words = initial_words.split()
    count = 0
    while(count < 10):
        potential_word = r.word()
        random_index = randint(0,len(initial_words) -1)
        word_from_initial_words_to_compare_against = initial_words[random_index]
        print("Comparing " + word_from_initial_words_to_compare_against +" " + potential_word)
        measured_difference = measure_difference(potential_word, word_from_initial_words_to_compare_against)
        print(measured_difference)
        if measured_difference == 2.0:
            #additional_words.append(potential_word)
            initial_words[random_index] = potential_word
            count += 1
    #initial_words = initial_words.split()
    #additional_words = ' '.join(additional_words)
    initial_prompt = initial_words
    initial_prompt = ' '.join(initial_prompt)
    #initial_prompt = ' '.join(initial_words + additional_words)
   # best_result = best_prompt(target_output, initial_prompt, target_scores)
    return initial_prompt

def generate_generation_0(initial_words, number_of_prompts):
    print("Running Generation 0")
    print(measure_difference("Happy", "Angry"))
    #return [initial_words for _ in range(number_of_prompts + 10)]
    return [ generate_prompt(initial_words, "stuff") for i in range(number_of_prompts)]



# initial_words = ['I', 'want', 'a', 'movie', 'like', 'your', 'mum']
# #print(generate_initial(initial_words, target_output))

# print(generate_generation_0(initial_words, 10))
