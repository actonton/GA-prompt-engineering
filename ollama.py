from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Weaviate
from wonderwords import RandomWord
import asyncio

llm = Ollama(model="orca-mini")
embeddings = OllamaEmbeddings(model="orca-mini")



# Ollama Embeddings creation demo
# sample_text = "This is an example text to turn into a vector"
# query_result = embeddings.embed_query(sample_text)
# print(query_result)


def generate_words():
    random_array = []

    for _ in range(0, 1):
        temp = []
        for _ in range(0, 1):
            temp.append(RandomWord().word())
        random_array.append(temp)
    print(random_array)

    genre = RandomWord().word()
    print(genre)
    prompts_array = [llm(f"I want a movie like {str(random_array)} from a genre {genre} which I want to watch") for _ in range(0, 1)]

    print(prompts_array)

if __name__ == '__main__':
    generate_words()



