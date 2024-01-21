# Setup
- Install Python version 3.11 (pyenv recommended)
- Run the `install_dependencies.sh` script to install requirements and setup a virtual enviornment (`.venv`)
- Activate the virtual enviornment `source .venv/bin/activate`
- Create `.env` file and populate it with API keys:
    - `OPENAI_API_KEY`

# Running Locally
Run the `run_app.sh` script to start a local instance of the application:
```
./run_app.sh
```

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