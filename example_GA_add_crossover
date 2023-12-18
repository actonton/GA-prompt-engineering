import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random
import numpy as np

# Sample movie overviews
movie_overviews = [
    "An epic adventure about a headstrong girl who yearns for more than society can offer.",
    "A heartwarming tale of friendship, love, and overcoming adversity.",
    "A thrilling journey of discovery and the struggle for justice."
]

# Sample generated prompts
generated_prompts = [
    "An adventure story",
    "A tale of friendship and love",
    "A thrilling journey"
]

# Text preprocessing function
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Tokenize and lower case
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Function to calculate fitness (text similarity)
def calculate_fitness(overviews, prompts):
    processed_overviews = [preprocess(overview) for overview in overviews]
    processed_prompts = [preprocess(prompt) for prompt in prompts]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_overviews + processed_prompts)
    similarity_matrix = cosine_similarity(tfidf_matrix[:len(overviews)], tfidf_matrix[len(overviews):])
    return np.mean(similarity_matrix, axis=1)

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self._initialize_population()

    def _initialize_population(self):
        return [random.choice(generated_prompts) for _ in range(self.population_size)]

    def _crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            # Simple crossover: take half from one parent and half from another
            half = len(parent1) // 2
            child = parent1[:half] + parent2[half:]
            return child
        return parent1

    def _mutate(self, prompt):
        if random.random() < self.mutation_rate:
            return random.choice(generated_prompts)
        return prompt

    def evolve(self):
        fitness_scores = calculate_fitness(movie_overviews, self.population)
        next_generation = []
        for _ in range(self.population_size):
            parent1 = self._select_parent(fitness_scores)
            parent2 = self._select_parent(fitness_scores)
            child = self._crossover(parent1, parent2)
            child = self._mutate(child)
            next_generation.append(child)
        self.population = next_generation

    def _select_parent(self, fitness_scores):
        total_fitness = sum(fitness_scores)
        pick = random.uniform(0, total_fitness)
        current = 0
        for i, fitness in enumerate(fitness_scores):
            current += fitness
            if current > pick:
                return self.population[i]

# Create an instance of the GA
ga = GeneticAlgorithm(population_size=10, mutation_rate=0.1, crossover_rate=0.7)

# Example: Evolve the population
ga.evolve()

# Print the evolved population
print("Evolved Population:")
for prompt in ga.population:
    print(prompt)

