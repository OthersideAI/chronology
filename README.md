# Chronology

Chronology is a library that enables users of OpenAI's GPT-3 language model to more easily build complex language-powered applications. 

It provides a simple and intuitive interface for working with GPT-3.

We built this at OthersideAI to help mitigate some of the monotonous work we had to do when developing with GPT-3. Our library has the following features:

- Asynchronously call GPT-3, enabling multiple prompts to generate at the same time
- Easy creation and modification of prompts
- Chain prompts together, feeding output from one or multiple prompts into another prompt, allowing for highly-complex systems to be built quickly

We built this library to be as intuitive as possible. There are no complicated concepts to master.

# Installation

chronology is hosted on [`PyPI`](https://pypi.org/project/chronology/).

Chronology is supported on Python 3.6 and above.

To install chronology:

`pip install chronology`

This project also depends on the following packages: 
* [`openai-api`](https://github.com/openai/openai-python)
* [`python-dotenv`](https://pypi.org/project/python-dotenv/)
* [`loguru`](https://github.com/Delgan/loguru)
* [`asyncio`](https://docs.python.org/3/library/asyncio.html)

# Usage

After you have downloaded the package, create a `.env` file at the root of your project and put your OpenAI API key in as:

`OPENAI_API_KEY = "MY_API_KEY"`

You now have a few options. You can use the UI to generate the chain or you can use the API directly.

## [Using ChronologyUI](https://github.com/OthersideAI/chronology-ui)

Here is a [Loom video](https://www.loom.com/share/47cb8d328ebd446db4d98ea1c0cac2c7?sharedAppSource=personal_library) showing how to use the UI with the Python [`chronology`](https://github.com/OthersideAI/chronology) package.

## Using the API Directly

### [`main`](#main)

The `main` function is an async function that holds all of your business logic. You then invoke this logic by passing it as an argument to `main`. **Required**

## Example:

```
# you can name this function anything you want, the name "logic" is arbitrary
async def logic():
    # you call the Chronology functions, awaiting the ones that are marked await
    prompt = read_prompt('example_prompt')
    completion = await cleaned_completion(prompt, max_tokens=100, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    print('Completion Response: {0}'.format(completion))
    
    # you can also run whatever you want in this function
    for i in range(4):
     print("hello")


# invoke the Chronology main fn to run the async logic
main(logic)
```

### [`fetch_max_search_doc`](#fetch_max_search_doc)
####  **Must be awaited**

Fetch document value with max score. Wrapper for OpenAI API Search. 

Optional:

min_score_cutoff = if maximum score is less than cutoff, None will be returned. Defaults to -1

full_doc = return whole response with max, but doesn't grab doc for you. Defaults to False. [doc, doc.index, doc.score]

### [`raw_completion`](#raw_completion)
####  **Must be awaited**

Wrapper for OpenAI API completion. Returns raw result from GPT-3.

### [`cleaned_completion`](#cleaned_completion)
####  **Must be awaited**

Wrapper for OpenAI API completion. Returns whitespace trimmed result from GPT-3.

### [`gather`](#gather)
####  **Must be awaited**

Run methods in parallel (they don't need to wait for each other to finish).

Requires method argumets to be async.

Example: await gather(fetch_max_search_doc(query_1, docs), fetch_max_search_doc(query_2, docs))

### [`read_prompt`](#read_prompt)

Looks in prompts/ directory for a text file. Pass in file name only, not extension.

Example: prompts/hello-world.txt -> read_prompt('hello-world')


### [`add_new_lines_start`](#add_new_lines_start)

Add N new lines to the start of a string.

### [`add_new_lines_end`](#add_new_lines_end)

Add N new lines to the end of a string.

### [`append_prompt`](#append_prompt)

Add new content to the end of a string.

### [`prepend_prompt`](#prepend_prompt)

Add new content to the start of a string.

### [`set_api_key`](#set_api_key)

Set your OpenAI API key in the code.

## Contributing

Chronology & ChronologyUI are both open source!

This project is an evolving use case and we welcome any contribution or feedback.

### Open Bouties: 

- [ ] adding all the fields the OpenAI Python API accepts to Chronology
- [ ] adding a test suite that calls different length chains
- [ ] extending `fetch_max_search_doc` to have smarter logic around minimium scores 
- [ ] make `gather` run faster, using [threads](https://docs.python.org/3/library/asyncio-task.html#running-in-threads)

## Learn More

Chronology is the backbone of https://OthersideAI.com. We use it to chain prompt calls and asyncronously call GPT-3. Our application is highly complex, and has many steps. Chronology allows us to parallelize those steps, significantly cutting down the time it takes to generate an email.

To learn more about OthersideAI, take a look at the following resources:

- [Our Homepage](https://www.othersideai.com/)
- [Our Twitter](https://twitter.com/othersideai)

Contact: info@othersideai.com
