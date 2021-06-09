import heapq
import time
import asyncio
import openai
import os
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
MAX_SEARCH_DOCUMENT_QUANTITY = 200

async def set_api_key(api_key):
    openai.api_key = api_key

# oai


async def _search(q, docs, engine="ada"):
    logger.debug("""CONFIG:
    Query: {0}
    Docs: {1}
    Engine: {2}
    """.format(q, docs, engine))
    response = openai.Engine(engine).search(
        documents=docs,
        query=q
    )
    logger.debug("GPT-3 Search Result: {0}".format(response))
    return response


async def _completion(prompt, engine="ada", max_tokens=64, temperature=0.7, top_p=1, stop=None, presence_penalty=0, frequency_penalty=0, echo=False, n=1, stream=False, logprobs=None, best_of=1, logit_bias={}):
    logger.debug("""CONFIG:
    Prompt: {0}
    Temperature: {1}
    Engine: {2}
    Max Tokens: {3}
    Top-P: {4}
    Stop: {5}
    Presence Penalty {6}
    Frequency Penalty: {7}
    Echo: {8}
    N: {9}
    Stream: {10}
    Log-Probs: {11}
    Best Of: {12}
    Logit Bias: {13}"""
                 .format(repr(prompt), temperature, engine, max_tokens, top_p, stop, presence_penalty, frequency_penalty, echo, n, stream, logprobs, best_of, logit_bias))
    response = openai.Completion.create(engine=engine,
                                        prompt=prompt,
                                        max_tokens=max_tokens,
                                        temperature=temperature,
                                        top_p=top_p,
                                        presence_penalty=presence_penalty,
                                        frequency_penalty=frequency_penalty,
                                        echo=echo,
                                        stop=stop,
                                        n=n,
                                        stream=stream,
                                        logprobs=logprobs,
                                        best_of=best_of,
                                        logit_bias=logit_bias)
    logger.debug("GPT-3 Completion Result: {0}".format(response))
    return response

# Helpers

def _batch_docs(docs, n):
    """Yield successive n-sized batches from list of docs."""
    for i in range(0, len(docs), n):
        yield docs[i:i + n]

def _max_search_doc(resp, n):
    max_docs = heapq.nlargest(n, resp['data'], key=lambda x: x['score'])
    return max_docs


def _fetch_response(resp, n):
    if n == 1:
        return resp.choices[0].text
    else:
        logger.debug('_fetch_response :: returning {0} responses from GPT-3'.format(n))
        texts = []
        for idx in range(0, n):
            texts.append(resp.choices[idx].text)
        return texts


def _trimmed_fetch_response(resp, n):
    if n == 1:
        return resp.choices[0].text.strip()
    else:
        logger.debug('_trimmed_fetch_response :: returning {0} responses from GPT-3'.format(n))
        texts = []
        for idx in range(0, n):
            texts.append(resp.choices[idx].text.strip())
        return texts


def prepend_prompt(new_stuff, prompt):
    '''
    Add new content to the start of a string.
    '''
    return "{0}{1}".format(new_stuff, prompt)


def append_prompt(new_stuff, prompt):
    '''
    Add new content to the end of a string.
    '''
    return "{1}{0}".format(new_stuff, prompt)


def add_new_lines_end(prompt, count):
    '''
    Add N new lines to the end of a string.
    '''
    return "{0}{1}".format(prompt, "\n"*count)


def add_new_lines_start(prompt, count):
    '''
    Add N new lines to the start of a string.
    '''
    return "{1}{0}".format(prompt, "\n"*count)


def read_prompt(filename):
    '''
    Looks in prompts/ directory for a text file. Pass in file name only, not extension.

    Example: prompts/hello-world.txt -> read_prompt('hello-world')
    '''
    return Path('./prompts/{0}.txt'.format(filename)).read_text()


async def gather(*args):
    '''
    Run methods in parallel (they don't need to wait for each other to finish).

    Requires method argumets to be async.

    Example: await gather(fetch_max_search_doc(query_1, docs), fetch_max_search_doc(query_2, docs))
    '''
    return await asyncio.gather(*args)

# Wrappers


async def cleaned_completion(prompt, engine="ada", max_tokens=64, temperature=0.7, top_p=1, stop=None, presence_penalty=0, frequency_penalty=0, echo=False, n=1, stream=False, logprobs=None, best_of=1, logit_bias={}):
    '''
    Wrapper for OpenAI API completion. Returns whitespace trimmed result from GPT-3.
    '''
    resp = await _completion(prompt,
                             engine=engine,
                             max_tokens=max_tokens,
                             temperature=temperature,
                             top_p=top_p,
                             presence_penalty=presence_penalty,
                             frequency_penalty=frequency_penalty,
                             echo=echo,
                             stop=stop,
                             n=n,
                             stream=stream,
                             logprobs=logprobs,
                             best_of=best_of,
                             logit_bias=logit_bias)
    return _trimmed_fetch_response(resp, n)


async def raw_completion(prompt, engine="ada", max_tokens=64, temperature=0.7, top_p=1, stop=None, presence_penalty=0, frequency_penalty=0, echo=False, n=1, stream=False, logprobs=None, best_of=1, logit_bias={}):
    '''
    Wrapper for OpenAI API completion. Returns raw result from GPT-3.
    '''
    resp = await _completion(prompt,
                             engine=engine,
                             max_tokens=max_tokens,
                             temperature=temperature,
                             top_p=top_p,
                             presence_penalty=presence_penalty,
                             frequency_penalty=frequency_penalty,
                             echo=echo,
                             stop=stop,
                             n=n,
                             stream=stream,
                             logprobs=logprobs,
                             best_of=best_of,
                             logit_bias=logit_bias)
    return _fetch_response(resp, n)


async def fetch_max_search_doc(q, docs, engine="ada", min_score_cutoff=-1, full_doc=False, n=1):
    '''
    Fetch document value with max score. Wrapper for OpenAI API Search.

    Optional:

    min_score_cutoff = if maximum score is less than cutoff, None will be returned. Defaults to -1

    full_doc = return whole response with max, but doesn't grab doc for you. Defaults to False. [doc, doc.index, doc.score]
    
    n = return top n most similar documents. Defaults to 1.
    '''
    if n > len(docs):
        return 'N > # of docs'
   
    resp = {'data':[]}
    for batch in _batch_docs(docs, MAX_SEARCH_DOCUMENT_QUANTITY):
        resp['data'].extend((await _search(q, batch, engine=engine))['data'])

    if not full_doc:
        max_docs = _max_search_doc(resp, n)
        max_docs_filtered = []
        for doc in max_docs:
            if float(doc['score']) > min_score_cutoff:
                max_docs_filtered.append(docs[doc['document']])
        if len(max_docs_filtered) > 0:
            return max_docs_filtered
        else:
            return None
    else:
        max_docs = _max_search_doc(resp, n)
        max_docs_filtered = []
        for doc in max_docs:
            if float(doc['score']) > min_score_cutoff:
                max_docs_filtered.append(doc)
        if len(max_docs_filtered) > 0:
            return max_docs_filtered
        else:
            return None


def main(fn, **args):
    '''
    Main function that runs logic. Accepts a function implemented on your end!
    '''
    tic = time.perf_counter()
    asyncio.run(fn(**args))
    toc = time.perf_counter()
    logger.debug(f"FINISHED WORKFLOW IN {toc - tic:0.4f} SECONDS")
