recipes = {
    "Iron Gear": { "output": 1, "craft_time": 0.5, "inputs": { "Iron Plate": 2 } },
    "Copper Wire": { "output": 2, "craft_time": 0.5, "inputs": { "Copper Plate": 1 } },
    "Electronic Circuit": {
        "output": 1,
        "craft_time": 0.5,
        "inputs": { "Iron Plate": 1, "Copper Wire": 3 },
    },
    "Automation Science": {
        "output": 1,
        "craft_time": 5,
        "inputs": { "Copper Plate": 1, "Iron Gear": 1 },
    },
    "Transport Belt": {
        "output": 2,
        "craft_time": 0.5,
        "inputs": { "Iron Plate": 1, "Iron Gear": 1 },
    },
    "Inserter": {
        "output": 1,
        "craft_time": 0.5,
        "inputs": { "Iron Plate": 1, "Iron Gear": 1, "Electronic Circuit": 1 },
    },
    "Logistic Science": {
        "output": 1,
        "craft_time": 6,
        "inputs": { "Transport Belt": 1, "Inserter": 1 },
    },
    "Pipe": { "output": 1, "craft_time": 0.5, "inputs": { "Iron Plate": 1 } },
    "Advanced Circuit": {
        "output": 1,
        "craft_time": 6,
        "inputs": { "Copper Wire": 4, "Electronic Circuit": 2, "Plastic Bar": 2 },
    },
    "Engine Unit": {
        "output": 1,
        "craft_time": 10,
        "inputs": { "Iron Gear": 1, "Pipe": 2, "Steel Plate": 1 },
    },
    "Chemical Science": {
        "output": 2,
        "craft_time": 24,
        "inputs": { "Advanced Circuit": 3, "Engine Unit": 2, "Sulfur": 1 },
    },
    "Electric Furnace": {
        "output": 1,
        "craft_time": 5,
        "inputs": { "Advanced Circuit": 5, "Steel Plate": 10, "Stone Brick": 10 },
    },
    "Productivity Module": {
        "output": 1,
        "craft_time": 15,
        "inputs": { "Advanced Circuit": 5, "Electronic Circuit": 5 },
    },
    "Iron Stick": { "output": 2, "craft_time": 0.5, "inputs": { "Iron Plate": 1 } },
    "Rail": {
        "output": 2,
        "craft_time": 0.5,
        "inputs": { "Stone": 1, "Iron Stick": 1, "Steel Plate": 1 },
    },
    "Production Science": {
        "output": 3,
        "craft_time": 21,
        "inputs": { "Electric Furnace": 1, "Productivity Module": 1, "Rail": 30 },
    },
    "Flying Robot Frame": {
        "output": 1,
        "craft_time": 20,
        "inputs": {
            "Battery": 2,
            "Electric Engine Unit": 1,
            "Electronic Circuit": 3,
            "Steel Plate": 1,
        },
    },
    "Low Density Structure": {
        "output": 1,
        "craft_time": 20,
        "inputs": { "Copper Plate": 20, "Plastic Bar": 5, "Steel Plate": 2 },
    },
    "Processing Unit": {
        "output": 1,
        "craft_time": 10,
        "inputs": { "Advanced Circuit": 2, "Electronic Circuit": 20, "Sulfuric Acid": 5 },
    },
    "Utility Science": {
        "output": 3,
        "craft_time": 21,
        "inputs": {
            "Flying Robot Frame": 1,
            "Low Density Structure": 3,
            "Processing Unit": 2,
        },
    },
}

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
