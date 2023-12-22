import json
import os
from pyhypercycle_aim import SimpleServer, JSONResponseCORS, aim_uri
from genetic_algorithm import call_genetic_algorithm, genetic_algorithm

PORT = os.environ.get("PORT", 4002)
SERVER_ENDPOINT = 'http://localhost:4002'

class GeneticExample(SimpleServer):
    manifest = {"name": "mendel_prompts_server",
                "short_name": "mp_server",
                "version": "0.1",
                "license": "MIT",
                "author": "Team Bandersnatch"
                }

    def __init__(self):
        pass

    @aim_uri(uri="/prompt", methods=["POST"],
             endpoint_manifest={
                 "documentation": "Returns the prompt and the score based on the initial movie idea",
             })
    async def prompt(self, request):

        request_json = await request.json()
        print(request_json)
        initial_words = request_json["initial_words"]

        genetic_algorithm_results, score_achieved = call_genetic_algorithm(initial_words)
        print(genetic_algorithm_results)
        return JSONResponseCORS({"initial_words": initial_words, "resulting_prompt": genetic_algorithm_results, "resulting_score": score_achieved})


def main():
    # example usage:
    app = GeneticExample()
    app.run(uvicorn_kwargs={"port": PORT, "host": "0.0.0.0"})


if __name__ == '__main__':
    main()
