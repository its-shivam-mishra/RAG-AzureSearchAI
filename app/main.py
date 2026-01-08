from app.rag_chain import build_rag_chain

rag_chain = build_rag_chain()

print("🚀 RAG system ready")

while True:
    question = input("\nAsk a question (exit to quit): ")
    if question.lower() == "exit":
        break

    answer = rag_chain.invoke(question)
    print("\nAnswer:\n", answer)
