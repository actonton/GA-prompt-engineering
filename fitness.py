from ollama import llm
from vector_db import query_db
from average_similar_movie_scores import average_similar_movie_scores



def fitness( prompt  , number_of_movies_to_compare_against):
    llm_response = llm(prompt)
    db_response = query_db(llm_response, number_of_movies_to_compare_against)
    return average_similar_movie_scores(db_response)

# def fitness_func(ga_instance, prompt, number_of_movies_to_compare_against):
#     return actual_fitness(prompt, number_of_movies_to_compare_against)