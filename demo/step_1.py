from chronological import read_prompt, cleaned_completion, main

# basic example -- playground reconstruction
# prompt src: https://en.wikipedia.org/wiki/Olive_oil
async def basic_example():
    prompt_summarize_for_a_2nd_grader = read_prompt('summarize_for_a_2nd_grader')
    completion_summarize_for_a_2nd_grader = await cleaned_completion(prompt_summarize_for_a_2nd_grader, max_tokens=100, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    return completion_summarize_for_a_2nd_grader

# basic example with variables -- playground reconstruction
# prompt src: https://en.wikipedia.org/wiki/Olive_oil, https://en.wikipedia.org/wiki/Interior_design
async def basic_example_with_variables():
    var_olive_oil = "Olive oil is a liquid fat obtained from olives (the fruit of Olea europaea; family Oleaceae), a traditional tree crop of the Mediterranean Basin, produced by pressing whole olives and extracting the oil. Olive oil is the most common vegetable oil. It is commonly used in cooking, for frying foods or as a salad dressing. It is also used in cosmetics, pharmaceuticals, and soaps, and as a fuel for traditional oil lamps, and has additional uses in some religions. The olive is one of three core food plants in Mediterranean cuisine; the other two are wheat and grapes. Olive trees have been grown around the Mediterranean since the 8th millennium BC."
    var_interior_design = "Interior design is the art and science of enhancing the interior of a building to achieve a healthier and more aesthetically pleasing environment for the people using the space. An interior designer is someone who plans, researches, coordinates, and manages such enhancement projects. Interior design is a multifaceted profession that includes conceptual development, space planning, site inspections, programming, research, communicating with the stakeholders of a project, construction management, and execution of the design."

    prompt_summarize_for_a_2nd_grader_with_variables = read_prompt("summarize_for_a_2nd_grader_with_variables")

    # use the Python3 `format()` method to replace {0} with our variables
    prompt_var_olive_oil = prompt_summarize_for_a_2nd_grader_with_variables.format(var_olive_oil)
    prompt_var_interior_design = prompt_summarize_for_a_2nd_grader_with_variables.format(var_interior_design)

    completion_var_olive_oil = await cleaned_completion(prompt_var_olive_oil, max_tokens=100, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])
    completion_var_interior_design = await cleaned_completion(prompt_var_interior_design, max_tokens=100, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    return (completion_var_olive_oil, completion_var_interior_design)


async def logic():
    basic_example_res = await basic_example()
    basic_example_with_vars_res = await basic_example_with_variables()

    print('-------------------------')
    print('Basic Example Response: {0}'.format(basic_example_res))
    print('-------------------------')
    print('Basic Example with Variables Responses: {0}'.format(basic_example_with_vars_res))
    print('-------------------------')


# invoke Chronology to run the async logic
main(logic)
