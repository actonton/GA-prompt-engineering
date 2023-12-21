from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Weaviate
from wonderwords import RandomWord
import asyncio
import random
import re

llm = Ollama(model="orca-mini")
embeddings = OllamaEmbeddings(model="orca-mini")



# Ollama Embeddings creation demo
# sample_text = "This is an example text to turn into a vector"
# query_result = embeddings.embed_query(sample_text)
# print(query_result)


def ollama_generation():
    random_array = []
    genres = [
    "Action",
    "Adventure",
    "Comedy",
    "Drama",
    "Horror",
    "Science Fiction (Sci-Fi)",
    "Fantasy",
    "Mystery",
    "Thriller",
    "Crime",
    "Romance",
    "Musical",
    "Historical",
    "Biography",
    "War",
    "Western",
    "Animation",
    "Family",
    "Documentary",
    "Experimental/Art House",
    "Mockumentary",
    "Sports",
    "Superhero",
    "Political",
    "Romantic Comedy (Rom-Com)"
]
    for _ in range(1):
        temp = []
        for _ in range(1):
            temp.append(RandomWord().word())
        random_array.append(temp)

    movie_info = llm(f"I want a movie idea that has features like {str(random_array)} from a {genres[random.randint(0, len(genres) - 1)]} which I want to produce")

    # Extracting only the title using regular expression
    # match = re.search(r'"([^"]+)"', movie_info)
    # title = match.group(1) if match else None

    return movie_info

# Example usage:
# movie_info = ollama_generation()
# print("Movie information:", movie_info)



