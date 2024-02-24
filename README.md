# Setup
- Install Python version 3.11 (pyenv recommended)
- Run the `install_dependencies.sh` script to install requirements and setup a virtual environment (`.venv`)
- Activate the virtual environment `source .venv/bin/activate`
- Create `.env` file and populate it with API keys (see "Resources" section for links):
    - `OPENAI_API_KEY`
    - `SCRAPEOPS_API_KEY`

# Running Locally
Run the `run_app.sh` script to start a local instance of the application:
```
./run_app.sh
```

## Understanding `requirements.txt` and `dev.txt`

In this project, dependency management is divided into two primary categories, each represented by a separate file:

1. **`requirements.txt`**: This file lists the essential Python packages required to run the application. These dependencies are what any user or environment needs to successfully execute the application's core functionality.

2. **`dev.txt`**: On the other hand, `dev.txt` extends `requirements.txt` by including additional packages that are only necessary for development environments. These may include code linters, formatters, testing frameworks, and other tools that aid in the development process but are not required for running the application itself.

Once the application starts, open your browser and navigate to:
```
http://localhost:5000
```

# Minimum Viable Product
- Set up a frontend framework
- Develop the UI components
- Implement fields to take in car issue prompt
- Return diagnosis

# Resources
- [OpenAi API reference](https://platform.openai.com/docs/api-reference/introduction)
- [ScrapeOps Proxy Aggregator](https://scrapeops.io/app/register/proxy)
- [ScrapeOps Web Scraping Playbook ](https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/)