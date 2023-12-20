from wonderwords import RandomWord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ollama import llm

sentimentAnalyzer = SentimentIntensityAnalyzer()

# generating initial prompt
# takes in data an array of words
def generate_initial(initial_words, target_output):
    target_scores = sentimentAnalyzer.polarity_scores(target_output)
    r = RandomWord()
    additional_words = [r.word(include_parts_of_speech=["adjectives"]) for _ in range(len(initial_words))]
    initial_prompt = ', '.join(initial_words + additional_words)
    best_result = best_prompt(target_output, initial_prompt, target_scores)

    return best_result

def best_prompt(target, initial_prompt, target_scores):
    # decode the binary vector into a list of keywords
    keywords = decode(initial_prompt)
    # get the phenotype (prompt) corresponding to the input genotype
    # here you define the loss function for the algorithm, which must
    # assess how far the output generated by the prompt is from the target,
    # but can include other factors as well, such as prompt size
    loss = get_error(initial_prompt, target, target_scores)
    return loss

def evaluate_prompt(prompt):
    # here you would call the LLM to generate its output based on the 
    # input prompt and return the output
    return llm(prompt)

def get_error(prompt, target_output, target_scores):
    output = evaluate_prompt(prompt)
    error = measure_difference(output, target_output, target_scores)
    return error

def decode(x):
    return [word for i, word in enumerate(x.split(', ')) if word]

def measure_difference(output, target_output, target_scores):
    output_scores = sentimentAnalyzer.polarity_scores(output)
    diff = abs(output_scores['neg'] - target_scores['neg']) + \
           abs(output_scores['neu'] - target_scores['neu']) + \
           abs(output_scores['pos'] - target_scores['pos'])
    return diff


if __name__ == "__main__":
    target_output = 'simple, lively, strong'
    initial_words = ['I', 'want', 'a', 'movie', 'like', 'your', 'mum']
    generate_initial(initial_words, target_output)