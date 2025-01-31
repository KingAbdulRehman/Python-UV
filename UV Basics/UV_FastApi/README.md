# UV FastAPI Project

This FastAPI project sets up a simple GET API that responds with "Hello World!".

## Installation

To install all dependencies, run the following command:
```
uv pip install -r pyproject.toml
```

## Running the Project

To run the project, execute the following command:
```
uv run hello.py
```

This will start the application on the default port `127.0.0.1`, which is configured at the end of the `hello.py` file.

## Testing the API

To test the API, open a browser and navigate to:
```
http://127.0.0.1/
```
You should see the "Hello World!" response.

Alternatively, you can use an API client like Postman or Thunder Client to test the endpoint.