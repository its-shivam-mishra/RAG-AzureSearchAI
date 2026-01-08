from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.retriever import get_retriever
from app.llm import get_llm

def build_rag_chain():
    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
    You are an enterprise AI assistant.
    Use ONLY the context below to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    chain = (
        {
            "context": retriever,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
