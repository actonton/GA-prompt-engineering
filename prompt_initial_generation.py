from random import randint
from wonderwords import RandomWord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ollama import llm

sentimentAnalyzer = SentimentIntensityAnalyzer()

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
    #target_scores = sentimentAnalyzer.polarity_scores(target_output)
    r = RandomWord()
    #additional_words = [r.word(include_parts_of_speech=["adjectives"]) for _ in range(len(initial_words))]
    additional_words = []
    while(len(additional_words) < len(initial_words)):
        potential_word = r.word()
        word_from_initial_words_to_compare_against = initial_words[randint(0,len(initial_words) -1)]
        if measure_difference(potential_word, word_from_initial_words_to_compare_against) > 0.5:
            additional_words.append(potential_word)

    initial_prompt = ', '.join(initial_words + additional_words)
   # best_result = best_prompt(target_output, initial_prompt, target_scores)
    return initial_prompt

def generate_generation_0(initial_words, number_of_prompts):
    return [ generate_prompt(initial_words, "stuff") for i in range(number_of_prompts)  ]


# target_output = 'simple, lively, strong'
# initial_words = ['I', 'want', 'a', 'movie', 'like', 'your', 'mum']
# #print(generate_initial(initial_words, target_output))

# print(generate_generation_0(initial_words, 10))
