import weaviate
from langchain.vectorstores import Weaviate
from langchain.vectorstores.docarray import DocArrayHnswSearch
from ollama import embeddings
from csv_to_json import file_contents, filtered_movies, documents
import json

weaviate_client = weaviate.Client(
    url="http://localhost:8080",
)

class_obj = {
    "class": "Movie",
    "vectorizer": "text2vec-contextionary",
    "moduleConfig": {
        "text2vec-contextionary": {},
    }
}

#RUN ONLY ONCE
def Initialize_db(client):
    client.schema.create_class(class_obj)
    data = json.loads(file_contents)

    client.batch.configure(batch_size=100)  # Configure batch
    with client.batch as batch:  # Initialize a batch process
        for i, d in enumerate(data):  # Batch import data
            print(f"importing movie: {i+1}")
            properties = {
                "names": d["names"],
                "date_x": d["date_x"],
                "score": d["score"],
                "genre": d["genre"],
                "overview": d["overview"],
                "crew": d["crew"],
                "orig_lang": d["orig_lang"],
                "budget_x": d["budget_x"],
                "revenue": d["revenue"],
                "country": d["country"]
            }
            batch.add_data_object(
                data_object=properties,
                class_name="Movie"
            )

def get_schema_definition(client):
    return json.dumps( client.schema.get(), indent=2)

def get_movie_count(client):
    return json.dumps(client.query.aggregate("Movie").with_meta_count().do(), indent=2)

def query_db(client, query):
    return json.dumps(  client.query.get("Movie", ["names", "score", "overview"]).with_near_text({"concepts": [query]}).with_limit(10).do(), indent=2)

def delete_all(client):
    client.schema.delete_class("Movie")





