import weaviate
from csv_to_json import file_contents, filtered_movies, documents
import json

client = weaviate.Client(
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
def Initialize_db(t):
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

def get_schema_definition():
    return json.dumps( client.schema.get(), indent=2)

def get_movie_count():
    return json.dumps(client.query.aggregate("Movie").with_meta_count().do(), indent=2)

def query_db( query, number_of_results):
    return json.dumps(  client.query.get("Movie", [ "score"]).with_near_text({"concepts": [query]}).with_limit(number_of_results).do(), indent=2)

def delete_all():
    client.schema.delete_class("Movie")



