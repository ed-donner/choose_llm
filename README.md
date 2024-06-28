# Choosing the Right LLM
### How to select, train and apply state-of-the-art LLMs to real-world business use cases.

This repo has companion code for my class on comparing and training LLMs.

### Resources to accompany the class

https://edwarddonner.com/2024/06/26/choosing-the-right-llm-resources/

### Experimenting with the examples yourself

To get started, after cloning the repo:

1. Create a new virtual environment using something like `python3 -m venv /path/to/new/virtual/environment`
2. Activate the virtual environment with `source /path/to/new/virtual/environment/bin/activate`
3. Create a file called `.env` in the project root directory (this is .gitignored) and add any private API keys, such as below. Alternatively you can type these keys directly into the notebooks. Details on creating API keys are in the resources.
   
```
OPENAI_API_KEY=xxxx
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
HF_TOKEN=xxxx
```

4. From the repo root directory, run `pip install -r requirements.txt`
5. Run `jupyter lab` to launch Jupyter and head over to the intro folder to get started.

There are a couple of Google Colab notebooks that we will refer to:

1. https://colab.research.google.com/drive/1CRgX6RVqnWZDexXLACbq91pX2I7O7Swu#scrollTo=uuTX-xonNeOK
2. https://colab.research.google.com/drive/19E9hoAzWKvn9c9SHqM4Xan_Ph4wNewHS#scrollTo=3MGyNCSAFfy6

### Alternative set up instructions if you're having problems

If you have an issues with the setup instructions, it might be that you have an older Python version on your box.
Use these alternative instructions:

1. Install Anaconda

https://docs.anaconda.com/anaconda/install/

2. Use Anaconda to create a new Python 3.12.3 environment:

`conda create -n choose-llms python=3.12.3`

3. Activate the environment:

`conda activate choose-llms`

4. Install the dependencies:
   
`pip install -r requirements.txt`

5. Run `jupyter lab` and head to the intro folder
