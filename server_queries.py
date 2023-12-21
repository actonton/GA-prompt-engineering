import requests
from server import SERVER_ENDPOINT

def parse_query(query: str):
    return query.split()


def query_server(initial_words, target_score):
    response = requests.post(SERVER_ENDPOINT + '/prompt', json={"initial_words": parse_query(initial_words),"target_score": target_score})
    print(response.json())



