# Offline Private ChatBot

This project implements a local [Llama 3.2-3B finetuned](https://github.com/ramandrosoa/Offline-Private-ChatBot/blob/main/Untitled13.ipynb) on a custom dataset. 
The primary objective is to create a personalized assistant capable of providing helpful responses in a user-friendly manner.  

## Project Overview

The model was trained on the [lighteval/MATH](https://huggingface.co/datasets/lighteval/MATH) dataset from HuggingFace, focusing on enhancing its ability to understand and respond to mathematical queries.
Prompt engineering was performed to personalize the assistant's interactions.
It uses Streamlit for the user interface. 

## Model Training
I used Ollama to run the model locally. Once the model was trained and saved, I created the personalized model using the following command in the terminal: ollama create math_3b -f Modelfile

## Preview

![ChatBot Interface](MBTI-screenshot1.PNG)
![ChatBot Interface1](MBTI-screenshot.PNG)

 [Finetune](https://github.com/ramandrosoa/Offline-Private-ChatBot/blob/main/Untitled13.ipynb)
[Dataset](https://huggingface.co/datasets/lighteval/MATH)
