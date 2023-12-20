import json

def average_similar_movie_scores(search_results):
   json_results = json.loads(search_results)
   scores = ((json_results["data"])["Get"])["Movie"]
   average = 0
   for score in scores:
         average += float(score["score"])
   return average/abs(len(scores))
