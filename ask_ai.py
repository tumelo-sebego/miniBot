from transformers import pipeline, set_seed

# Load a tiny GPT2 model
generator = pipeline('text-generation', model='distilgpt2')  # DistilGPT2 = small, fast

set_seed(42)  # For consistent outputs (optional)

print("✅ AI Ready! Talk to me (type 'exit' to quit)")

while True:
    prompt = input("\n💬 You: ")
    if prompt.lower() == 'exit':
        print("👋 Bye!")
        break

    output = generator(prompt, max_length=50, num_return_sequences=1)
    print("🤖 AI:", output[0]['generated_text'])
