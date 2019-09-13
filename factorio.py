from mod_space_recipes import recipes

results = {}

items = [
    # "Automation Science",
    # "Logistic Science",
    # "Chemical Science",
    # "Military Science",
    # "Production Science",
    "Utility Science",
    "Rocket Science",
    # "Advanced Circuit"
]
stops = [
    "Steel Plate",
    "Advanced Circuit",
    "Electronic Circuit",
    "Engine Unit",
    "Battery",
    "Glass",
]
output = 1

PROD = 1


def calc_input_required(item, output_per_sec, prod=PROD):
    if item in recipes and item not in stops:
        recipe = recipes[item]
        speed = recipe["machine"]["speed"]
        craft_output = recipe["output"] * prod / (recipe["craft_time"] / speed)
        assemblers = output_per_sec / craft_output
        print(f"- {assemblers} {recipe['machine']['name']}s for {item}")

        for input, amount in recipe["inputs"].items():
            input_required = assemblers * amount / (recipe["craft_time"] / speed)
            print(f"{item} needs {input_required} {input}s per second")
            calc_input_required(input, input_required)

    else:
        if item in results:
            results[item] += output_per_sec
        else:
            results[item] = output_per_sec


if __name__ == "__main__":
    for item in items:
        print(f"To make {output} {item} per second, you will need:")
        calc_input_required(item, output)
        print("\nTOTAL RAW:")
        for base_item in results:
            print(f"- {results[base_item]} {base_item}s per second")
        print("\n\n")
        results.clear()
