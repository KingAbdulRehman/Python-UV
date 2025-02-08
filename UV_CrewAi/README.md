# Project Overview

This project consists of three main flows:

## 1. Test Flow
- **File:** `main.py`
- **Description:** This flow uses the `listen` method to check the initial setup.

## 2. LLM Call Flow
- **File:** `call_llm.py`
- **Description:** 
  - First, generate a city using the LLM.
  - Then, generate a fact about that city.
  - Finally, save the fact in `fact.md` and validate its correctness.

## 3. Route Flow
- **File:** `route_flow.py`
- **Description:** Randomly pick a city and run the process for that city.

## Setup

To run these flows, set up the API key in the `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```


