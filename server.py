import os
from pyhypercycle_aim import SimpleServer, JSONResponseCORS, aim_uri

from genetic_algorithm import GeneticAlgorithm

PORT = os.environ.get("PORT", 4002)
SERVER_ENDPOINT = 'http://localhost:4002'

class GeneticExample(SimpleServer):
    manifest = {"name": "GA-prompt-engineering-server",
                "short_name": "GA-Prompt-Engineering",
                "version": "0.1",
                "license": "MIT",
                "author": "Bandersnatch"
                }

    def __init__(self):
        pass

    @aim_uri(uri="/prompt", methods=["POST"],
             endpoint_manifest={
                 "documentation": "Returns the prompt and the score based on the initial movie idea",
             })
    async def prompt(self, request):
        # define the total iterations
        n_iter = 100
        # bits
        n_bits = 20
        # define the population size
        n_pop = 100
        # crossover rate
        r_cross = 0.9
        # mutation rate
        r_mut = 1.0 / float(n_bits)

        request_json = await request.json()
        target_score = request_json['target_score']
        initial_words = request_json["initial_words"]



        # perform the genetic algorithm search
        genetic_algorithm_results = GeneticAlgorithm.genetic_algorithm(initial_words, target_score)
        return JSONResponseCORS({"target_score": target_score, "initial_words": initial_words, "resulting_prompt": genetic_algorithm_results["best_prompt"], "resulting_score": genetic_algorithm_results["best_score"]})


def main():
    # example usage:
    app = GeneticExample()
    app.run(uvicorn_kwargs={"port": PORT, "host": "0.0.0.0"})


if __name__ == '__main__':
    main()
