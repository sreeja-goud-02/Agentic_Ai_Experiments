# EXP 3 – Prompt Chaining for Summarization

## Objective

To implement a multi-step prompt chaining workflow where the output of one LLM step becomes the input for the next step.

## Description

This experiment demonstrates prompt chaining using Ollama and the Llama 3.2 language model.

The system accepts a topic from the user and processes it through multiple sequential steps. First, the system generates a short summary of the topic. The generated summary is then passed to the next step to extract important key points. Finally, the key points are used to generate three important questions.

## Technologies Used

- Python
- Ollama
- Llama 3.2

## Workflow

User Topic
↓
Generate Summary
↓
Extract Key Points
↓
Generate Questions
↓
Final Output

## Result

The prompt chaining workflow successfully passes the output of each step as input to the next step and generates the final questions based on the original topic.
