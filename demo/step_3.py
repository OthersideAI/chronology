from chronological import read_prompt, fetch_max_search_doc, main, cleaned_completion

async def fetch_three_top_animals(query, n):
    # splitting on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    return await fetch_max_search_doc(query, prompt_animals, engine="ada", n=n)


async def find_each_animals_favorite_food(animals):
    prompt_what_is_the_favorite_food_of = read_prompt('what_is_the_favorite_food_of')
    favorite_foods = []
    for animal in animals:
        res = await cleaned_completion(prompt_what_is_the_favorite_food_of.format(animal), engine="davinci", temperature=0.2, stop=["\n\n"])
        favorite_foods.append({ animal: res})
    return favorite_foods

async def logic():
    animals = await fetch_three_top_animals('monkey', 3)
    favorite_foods = await find_each_animals_favorite_food(animals)
    print(favorite_foods)

main(logic)