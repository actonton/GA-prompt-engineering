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
    for _ in range(0, 1):
        temp = []
        for _ in range(0, 1):
            temp.append(RandomWord().word())
        random_array.append(temp)
    print(random_array)
    prompts_array = [llm(f"I want a movie name that has features like {str(random_array)} from a {genres[random.randint(0, len(genres) - 1)]} which I want to watch") for _ in range(0, 1)]

    print(prompts_array)
    return prompts_array




