# Setup
- Install Python version 3.11 (pyenv recommended)
- Run the `install_dependencies.sh` script to install requirements and setup a virtual environment (`.venv`)
- Activate the virtual environment `source .venv/bin/activate`
- Create `.env` file and populate it with API keys:
    - `OPENAI_API_KEY`

# Running Locally
Standup the Milvus Vector Database container by running:
```shell
docker compose up
```

Then run the `run_app.sh` script to start a local instance of the application:
```shell
./run_app.sh
```

Once the application starts, open your browser and navigate to:
```
http://localhost:5000
```

# Application Architecture

The application follows a modular architecture to ensure flexibility and maintainability. Here's an overview of the main components:

- **`app/services/llm_interaction.py`**: This module provides an abstraction layer for interacting with language models (LLMs) and embeddings. It allows the application to dynamically switch between different LLMs based on configuration, without modifying the codebase.

- **`app/utils/util.py`**: This module contains utility functions for car diagnostics, such as generating diagnostic context using the selected LLM and embeddings.

- **`app/routes/`**: This directory contains the route definitions for the application, including routes for handling ChatGPT interactions and form submissions.

- **`app/__init__.py`**: This module initializes the Flask application and sets up the necessary configurations, such as loading environment variables and registering blueprints.

# Configuring the LLM
The application supports using different LLMs for generating car diagnostic responses. To specify the LLM to use, set the following environment variables in your `.env` file:

- `LLM_TYPE`: The type of LLM to use (e.g., "openai", "anthropic"). Default is "openai".
- `EMBEDDINGS_TYPE`: The type of embeddings to use (e.g., "openai", "anthropic"). Default is "openai".

For example, to use OpenAI's GPT models and embeddings, your .env file should include:
```
LLM_TYPE=openai
EMBEDDINGS_TYPE=openai
OPENAI_API_KEY=your_openai_api_key
```
Make sure to provide the necessary API keys for the selected LLM and embeddings providers.

# Testing

The application includes unit tests to ensure the correctness of the implemented functionality. The tests are located in the `tests/` directory and cover the following modules:

- **`tests/test_llm_interaction.py`**: This module contains unit tests for the `llm_interaction` module, verifying the behavior of the `get_llm` and `get_embeddings` functions under different scenarios.

To run the tests, execute the following command:
```shell
python -m unittest discover tests
```

## Understanding `requirements.txt` and `dev.txt`

In this project, dependency management is divided into two primary categories, each represented by a separate file:

1. **`requirements.txt`**: This file lists the essential Python packages required to run the application. These dependencies are what any user or environment needs to successfully execute the application's core functionality.

2. **`dev.txt`**: On the other hand, `dev.txt` extends `requirements.txt` by including additional packages that are only necessary for development environments. These may include code linters, formatters, testing frameworks, and other tools that aid in the development process but are not required for running the application itself.

# Minimum Viable Product
- Set up a frontend framework
- Develop the UI components
- Implement fields to take in car issue prompt
- Return diagnosis

# Resources
- [OpenAi API reference](https://platform.openai.com/docs/api-reference/introduction)



# Setup
- Install Python version 3.11 (pyenv recommended)
- Run the `install_dependencies.sh` script to install requirements and setup a virtual environment (`.venv`)
- Activate the virtual environment `source .venv/bin/activate`
- Create `.env` file and populate it with API keys:
    - `OPENAI_API_KEY`

# Running Locally
Standup the Milvus Vector Database container by running:
```shell
docker compose up
```

Then run the `run_app.sh` script to start a local instance of the application:
```shell
./run_app.sh
```

Once the application starts, open your browser and navigate to:
```
http://localhost:5000
```

## Understanding `requirements.txt` and `dev.txt`

In this project, dependency management is divided into two primary categories, each represented by a separate file:

1. **`requirements.txt`**: This file lists the essential Python packages required to run the application. These dependencies are what any user or environment needs to successfully execute the application's core functionality.

2. **`dev.txt`**: On the other hand, `dev.txt` extends `requirements.txt` by including additional packages that are only necessary for development environments. These may include code linters, formatters, testing frameworks, and other tools that aid in the development process but are not required for running the application itself.

# Application Architecture

The application follows a modular architecture to ensure flexibility and maintainability. Here's an overview of the main components:

- **`app/services/llm_interaction.py`**: This module provides an abstraction layer for interacting with language models (LLMs) and embeddings. It allows the application to dynamically switch between different LLMs based on configuration, without modifying the codebase.

- **`app/utils/util.py`**: This module contains utility functions for car diagnostics, such as generating diagnostic context using the selected LLM and embeddings.

- **`app/routes/`**: This directory contains the route definitions for the application, including routes for handling ChatGPT interactions and form submissions.

- **`app/__init__.py`**: This module initializes the Flask application and sets up the necessary configurations, such as loading environment variables and registering blueprints.

# Testing

The application includes unit tests to ensure the correctness of the implemented functionality. The tests are located in the `tests/` directory and cover the following modules:

- **`tests/test_llm_interaction.py`**: This module contains unit tests for the `llm_interaction` module, verifying the behavior of the `get_llm` and `get_embeddings` functions under different scenarios.

To run the tests, execute the following command:



# Minimum Viable Product
- Set up a frontend framework
- Develop the UI components
- Implement fields to take in car issue prompt
- Return diagnosis

# Resources
- [OpenAi API reference](https://platform.openai.com/docs/api-reference/introduction)
