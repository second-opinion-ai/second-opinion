
# AI-driven Car Repair Assistant Diagram

## Overview

The `draw_diagrams.py` module draws an architectural diagram on the architecture as of 03/11/2024. This was created for a blog post by the Milvus team.

## Architecture

The system architecture comprises several key components:

- **User Interface (Web Form):** A simple, user-friendly web form where users can submit their car issues.
- **Form Submission & Context Retrieval:** Processes the form submissions and retrieves relevant context for the AI query.
- **Milvus (Vector Database):** Serves as the backend database, efficiently handling query operations to find the most relevant repair data.
- **ChatGPT Service:** Interfaces with the OpenAI API to generate human-like responses based on the query and context provided.
- **OpenAI API (GPT-3.5-turbo):** The AI engine that processes queries and returns intelligent diagnostic suggestions.

## How to Use

This project utilizes the Graphviz Python package to visually represent our architecture in a text-based manner. These diagrams provide a clear overview of the system's structure and data flow.

### Generating Graphs

To generate the architecture diagrams, ensure that you have activated the project's virtual environment and installed all development requirements as outlined in the project's root [README](../README.md).

Once the virtual environment is activated and the necessary packages are installed, you can generate the architecture diagrams by executing the following command from the terminal:
```
python draw_diagrams.py
```

This script will generate the diagrams and save them in a predefined directory. You can view these diagrams to understand the current architecture setup and how the components interact within the system.
