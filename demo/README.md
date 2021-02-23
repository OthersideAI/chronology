# How To Use Chronology -- A Walkthrough Demo

# [WATCH THE DEMO LIVESTREAM HERE](https://youtu.be/G3PctszbrrE)

## Step 0 - Installation

1. Download Chronology using the command (*you can also find it on pip [here](https://pypi.org/project/chronological/)*):
```python
python3 -m pip install chronological
```
2. Clone this repo to your local machine
3. Create a `.env` file and add your OpenAI API key to it in the format: `OPENAI_API_KEY="MY_API_KEY"`
4. Run each step with the command: 
```python
python3 step_1.py
```

## Step 1 - Completions

Completions are the bread and butter of the OpenAI API, and the first thing most people use when they use the playground.

In this step, we'll examine how to:

1. Read in a prompt from a text file
2. Use the prompt to make an `awaited completion` from the `davinci` engine
3. Load in two variables and attach them to the same prompt
4. Create completions with each variable-formatted prompt

## Step 2 - Searching

The Semantic Search API is a powerful tool to be able to filter a set of documents based on a query.

In this step, we'll examine how to:

1. Read in a list of animals from a text file
2. Return the top document that matches our query by using an `awaited search` from the `ada` engine
3. Return the top three documents that match the same query

## Step 3 - Linking it All Together: Extra Logic and Using Different Engines

The power of Chronology starts to show with this step. We'll meld the power of programming logic with the power of the OpenAI API. 

In this step, we'll examine how to:
1. Capture the result from a search call to OpenAI using the `ada` engine
2. Apply extra logic to that search call
3. Run a completion with the result of the search call + logic using the `davinci` engine

## Extra: Using the UI

If you would prefer to build Chronology chains without writing code, I have great news! There is a `no-code UI` for Chronology, called the [Chronology UI](https://chronology-ui.vercel.app/#).

Here is a [in depth Loom video tutorial on how to use Chronology UI with Chronology](https://www.loom.com/share/47cb8d328ebd446db4d98ea1c0cac2c7)

*They say a picture is worth 1000 words, so what's a video worth!*

*You can see the GitHub repo for Chronology UI [here](https://github.com/OthersideAI/chronology-ui)*