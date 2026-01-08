from langchain_openai import AzureChatOpenAI
from config.settings import *

def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        deployment_name=CHAT_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION,
        temperature=0
    )
