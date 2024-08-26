# Choosing the Right LLM
### How to select, train and apply state-of-the-art LLMs to real-world business use cases.

This repo has companion code for my class on comparing and training LLMs.

### Resources to accompany the class

The resources are [here](https://edwarddonner.com/2024/06/26/choosing-the-right-llm-resources/)

### Recommended installation: using Anaconda

The recommended approach is to use Anaconda, which ensures our Python versions are consistent.
If you'd prefer to use a virtualenv, that should work fine too - instructions are in the next section.

After cloning this repo, install Anaconda if you don't have it already:

https://docs.anaconda.com/anaconda/install/

Then here are the installation instructions:

1. Use Anaconda to create a new Python 3.11 environment:

`conda create -n choose-llms python=3.11`

2. Activate the environment:

`conda activate choose-llms`

3. Create a file called `.env` in the project root directory (this is .gitignored) and add any private API keys, such as below. Alternatively you can type these keys directly into the notebooks. Details on creating API keys are in the resources.
   
```
OPENAI_API_KEY=xxxx
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
HF_TOKEN=xxxx
```

4. Install the dependencies:
   
`pip install -r requirements.txt`

5. Run `jupyter lab` and head to the intro folder

### Google Colabs

At 2 points in the class we will refer to Google Colab notebooks.

In segment 1, when we run inference with open source models: [Link here](https://colab.research.google.com/drive/1CRgX6RVqnWZDexXLACbq91pX2I7O7Swu)

In segment 3, our main project to predict Amazon prices: [Data Curator Colab](https://colab.research.google.com/drive/1cYLqi3_XlXzbzYMKd8j0VDycIKmWABAS) | 
[Training Colab](https://colab.research.google.com/drive/1TA_GwdrpWwRZfUw8I9y2fqqwFv9CBU1O) | 
[Inference Colab](https://colab.research.google.com/drive/1V6_F3r6Tge3EASyffdcWWMrA7vOzHNL8)

### Alternative instructions: using a virtualenv, if you prefer

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



