from transformers import pipeline

# Load a tiny model for question-answering
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

print("✅ AI Ready! Ask me anything (type 'exit' to quit)")

while True:
    question = input("\n❓ Your question: ")
    if question.lower() == 'exit':
        print("👋 Bye!")
        break
    
    context = """
    Neil Armstrong was the first man to walk on the Moon in 1969. 
    The Moon is Earth's only natural satellite. 
    Water freezes at 0 degrees Celsius. 
    The Eiffel Tower is located in Paris, France.
    """
    # Note: In real cases, you can load dynamic contexts too!

    result = qa_pipeline(question=question, context=context)
    print("🤖 Answer:", result['answer'])
