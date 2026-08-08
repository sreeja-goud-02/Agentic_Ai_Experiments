# EXP 2 – RAG-Based Question Answering System

## Objective

To implement a Retrieval-Augmented Generation (RAG) system that retrieves relevant information from a knowledge document and uses an LLM to generate an answer.

## Description

This experiment implements a basic RAG-based Question Answering System using Python, Ollama, and a local knowledge document.

The system reads information from a knowledge file, divides the content into smaller chunks, retrieves the most relevant chunks for a user's question, and provides the retrieved context to the Llama 3.2 model.

The LLM then generates an answer using the retrieved information.

## Technologies Used

- Python
- Ollama
- Llama 3.2
- Sentence Transformers
- Scikit-learn
- NumPy

## Workflow

User Question  
↓  
Knowledge Document  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
Similarity Search  
↓  
Relevant Context Retrieval  
↓  
Llama 3.2  
↓  
Generated Answer

## Result

The RAG-based Question Answering System successfully retrieves relevant information from the knowledge document and generates an answer based on the retrieved context.
