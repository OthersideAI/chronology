from chronological import read_prompt, fetch_max_search_doc, main

async def fetch_top_animal(query):
    # splitting on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    return await fetch_max_search_doc(query, prompt_animals, engine="ada")

async def fetch_three_top_animals(query, n):
    # splitting on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    return await fetch_max_search_doc(query, prompt_animals, engine="ada", n=n)

async def logic():
    fetch_top_animal_res = await fetch_top_animal("monkey")
    fetch_top_three_animals_res = await fetch_three_top_animals("monkey", 3)

    print('-------------------------')
    print('Fetch Top Animal Response: {0}'.format(fetch_top_animal_res))
    print('-------------------------')
    print('Fetch Top Three Animals Response: {0}'.format(fetch_top_three_animals_res))
    print('-------------------------')

main(logic)