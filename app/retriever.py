from langchain_community.vectorstores import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings
from config.settings import *

def get_retriever():
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        deployment=EMBEDDING_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION
    )

    vector_store = AzureSearch(
        azure_search_endpoint=AZURE_SEARCH_ENDPOINT,
        azure_search_key=AZURE_SEARCH_KEY,
        index_name=AZURE_SEARCH_INDEX,
        embedding_function=embeddings.embed_query,
        
        vector_field_name="my_vector"  
    )

    return vector_store.as_retriever(
        search_type="similarity"
    )
