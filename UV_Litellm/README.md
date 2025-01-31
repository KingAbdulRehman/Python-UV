# UV LiteLLM Project

This project sets up LiteLLM with UV, using the Gemini model.

## Installation

To install all dependencies, run the following command:
```
uv pip install -r pyproject.toml
```

## Setting Up API Key

First, set up the API key in the environment. Create a `.env` file and add the API key as follows:
```
GEMINI_API_KEY=API-KEY
```

## Running the Project

If you want to change the model or message, modify the `hello.py` file accordingly. Then, run the following command to start the project:
```
uv run hello.py
```