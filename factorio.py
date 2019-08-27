from base_recipes import recipes

results = {}

sciences = [
    "Automation Science",
    # "Logistic Science",
    "Chemical Science",
    # "Production Science",
    # "Utility Science",
]
output = 1

CRAFT_SPEED = 0.75
PROD = 1


def calc_input_required(item, output_per_sec, prod=PROD, speed=CRAFT_SPEED):
    if item in recipes:
        recipe = recipes[item]
        craft_output = recipe["output"] * prod / (recipe["craft_time"] / speed)
        assemblers = output_per_sec / craft_output
        print(f"- {assemblers} assemblers for {item}")

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
    for science in sciences:
        print(f"To make {output} {science} per second, you will need:")
        calc_input_required(science, output)
        print("\nTOTAL RAW:")
        for item in results:
            print(f"- {results[item]} {item}s per second")
        print("\n\n")
        results.clear()
