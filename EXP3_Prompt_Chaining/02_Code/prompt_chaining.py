import ollama

print("=" * 50)
print("Prompt Chaining for Summarization")
print("=" * 50)

topic = input("\nEnter a topic: ")

summary = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Write a short summary about {topic} in around 100 words."
        }
    ]
)

summary_text = summary["message"]["content"]

print("\nSUMMARY:")
print(summary_text)

keypoints = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Extract 5 important key points from this summary:\n{summary_text}"
        }
    ]
)

keypoints_text = keypoints["message"]["content"]

print("\nKEY POINTS:")
print(keypoints_text)

questions = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Generate exactly 3 important questions using these key points:\n{keypoints_text}"
        }
    ]
)

print("\nQUESTIONS:")
print(questions["message"]["content"])
