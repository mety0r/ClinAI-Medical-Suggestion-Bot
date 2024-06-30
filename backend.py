import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load documents
def load_documents(directory):
    return SimpleDirectoryReader(directory).load_data()

# Initialize LlamaCPP model
def initialize_llm():
    return LlamaCPP(
        model_url='https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
        model_path=None,
        temperature=0.1,
        max_new_tokens=256,
        context_window=3900,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": -1},  # Enable GPU layers
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )

# Initialize embedding model
def initialize_embed_model():
    return LangchainEmbedding(
        HuggingFaceEmbeddings(model_name="thenlper/gte-large")
    )

# Create service context
def create_service_context(llm, embed_model):
    return ServiceContext.from_defaults(
        chunk_size=256,
        llm=llm,
        embed_model=embed_model
    )

# Create query engine
def create_query_engine(documents, service_context):
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    return index.as_query_engine()

# Main function to setup everything
def setup_query_engine(data_directory):
    documents = load_documents(data_directory)
    llm = initialize_llm()
    embed_model = initialize_embed_model()
    service_context = create_service_context(llm, embed_model)
    return create_query_engine(documents, service_context)
