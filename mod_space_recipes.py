from base_recipes import recipes, assembler

mod_recipes = {
    "Heat Shielding": {
        "output": 1,
        "craft_time": 10,
        "machine": assembler,
        "inputs": { "Stone": 20, "Steel Plate": 2, "Sulfur": 8 },
    },
    "Electric Furnace": {
        "output": 1,
        "craft_time": 5,
        "machine": assembler,
        "inputs": { "Advanced Circuit": 5, "Steel Plate": 10, "Heat Shielding": 2 },
    },
    "Productivity Module": {
        "output": 1,
        "craft_time": 2,
        "machine": assembler,
        "inputs": { "Advanced Circuit": 5, "Electronic Circuit": 5 },
    },
    "Low Density Structure": {
        "output": 1,
        "craft_time": 20,
        "inputs": { "Glass": 10, "Copper Plate": 20, "Plastic Bar": 10, "Steel Plate": 5 },
    },
}

recipes.update(mod_recipes)