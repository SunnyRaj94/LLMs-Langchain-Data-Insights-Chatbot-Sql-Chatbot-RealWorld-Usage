# Real-World-Large-Language-Models
  The Real-World-Large-Language-Models repository provides a comprehensive toolkit for leveraging state-of-the-art large language models (LLMs) in practical applications. By integrating LangChain, Meta's LLaMA 2, and various quantized models, this repository enables developers to efficiently build and deploy LLM-powered solutions on a wide range of hardware, including consumer-grade devices.

## Overview
Large Language Models (LLMs) are pivotal in advancing natural language processing (NLP) and understanding. They employ deep learning techniques to generate, comprehend, and interact with human language at a sophisticated level. LLaMA 2, developed by Meta, is a leading open-source LLM that competes with OpenAI's GPT series and Google's PaLM 2, distinguished by its openness for research and commercial use.

## Key Features
 ### LangChain Integration
  - **LangChain Framework:** An open-source platform that facilitates the development of applications powered by LLMs. It seamlessly integrates with external components, enabling robust and scalable AI-driven solutions.
  - **Model Loading and Management:** Simplifies the process of loading and managing large models, making it easier to deploy and use LLMs in real-world scenarios.
 ### Meta’s LLaMA 2 Models
  - Versatile Model Collection: Includes a range of pretrained and fine-tuned models with parameters varying from 7 billion to 70 billion, optimized for dialogue and interactive use cases.
  - High Performance: Demonstrates superior performance compared to other open-source models and rivals closed-source models in human evaluations for both helpfulness and safety.
### Efficient Model Deployment
   - **llama.cpp:** A specialized C/C++ implementation designed for running the LLaMA model with 4-bit integer quantization on Apple silicon and x86 architectures. Initially a web chat prototype, it now functions as a sandbox for developing the ggml library's features.
   - **GGML:** A C library that optimizes the deployment of large language models by using quantization techniques to reduce model size and computational requirements, making it feasible to run sophisticated models on consumer-grade hardware.

### Quantized Models
  - **Hugging Face Community Contributions:** Access to a variety of quantized models optimized for different hardware, such as the T4 GPU. This repository particularly focuses on models based on the GGML library, like the Llama-2-13B-chat-GGML model.
  - **Efficient Resource Usage:** Quantized models retain essential performance while minimizing resource consumption, making them ideal for deployment in constrained environments.


## Common Knowledge

- Large Language Models (LLMs) are foundational machine learning models that use deep learning algorithms to process and understand natural language.
- Llama 2 is Meta's open source large language model (LLM). It's basically the Facebook parent company's response to OpenAI's GPT models and Google's AI models like PaLM 2—but with one key difference: it's freely available for almost anyone to use for research and commercial purposes.

- The Llama 2 is a collection of pretrained and fine-tuned generative text models, ranging from 7 billion to 70 billion parameters, designed for dialogue use cases.

- It outperforms open-source chat models on most benchmarks and is on par with popular closed-source models in human evaluations for helpfulness and safety.

- LangChain is an open source framework that lets software developers working with artificial intelligence (AI) and its machine learning subset combine large language models with other external components to develop LLM-powered applications.

- llama.cpp's
    Its objective is to run the LLaMA model with 4-bit integer quantization on MacBook. It is a plain C/C++ implementation optimized for Apple silicon and x86 architectures, supporting various integer quantization and BLAS libraries. Originally a web chat example, it now serves as a development playground for ggml library features.

- GGML
    A C library for machine learning, facilitates the distribution of large language models (LLMs). It utilizes quantization to enable efficient LLM execution on consumer hardware. GGML files contain binary-encoded data, including version number, hyperparameters, vocabulary, and weights. The vocabulary comprises tokens for language generation, while the weights determine the LLM's size. Quantization reduces precision to optimize resource usage.

## Quantized Models from the Hugging Face Community
- The Hugging Face community provides quantized models, which allow us to efficiently and effectively utilize the model on the T4 GPU. It is important to consult reliable sources before using any model.

- There are several variations available, but the ones that interest us are based on the GGLM library.

- We can see the different variations that [Llama-2-13B-GGML](https://huggingface.co/models?search=llama%202%20ggml) has here.

- In this case, we will use the model called [Llama-2-13B-chat-GGML](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML).

## Load models as llm in langchain
- To see how to load model from bin file, refer this [link here](https://python.langchain.com/docs/use_cases/question_answering/how_to/local_retrieval_qa)
