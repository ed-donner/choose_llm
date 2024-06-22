# Choosing the Right LLM
### How to select, train and apply state-of-the-art LLMs to real-world business use cases.

This repo has companion code to accompany my class on identifying and training LLMs.

To get started, after cloning the repo:

1. Create a new virtual environment using something like `python3 -m venv /path/to/new/virtual/environment`
2. Activate the virtual environment with `source /path/to/new/virtual/environment/bin/activate`
3. Create a file called `.env` in the project root directory (this is .gitignored) and add any private API keys, such as below:
```
OPENAI_API_KEY=xxxx
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
HF_TOKEN=xxxx
```
4. From the repo root directory, run `pip install -r requirements.txt`
5. Run `jupyter lab` to launch Jupyter and head over to the intro folder to get started.
