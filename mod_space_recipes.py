from base_recipes import recipes, assembler, electric_furnace

mod_recipes = {
    "Sand": {
        "output": 2,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Stone": 1 }
    },
    "Glass": {
        "output": 1,
        "craft_time": 4,
        "machine": electric_furnace,
        "inputs": {"Sand": 4}
    },
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
        "machine": assembler,
        "inputs": { "Glass": 10, "Copper Plate": 20, "Plastic Bar": 10, "Steel Plate": 5 },
    },
    "Rocket Science": {
        "output": 3,
        "craft_time": 20,
        "machine": assembler,
        "inputs": {
            "Battery": 5,
            "Processing Unit": 1,
            "Heat Shielding": 1,
            "Low Density Structure": 1,
            "Liquid Rocket Fuel": 100,
        },
    },
}

recipes.update(mod_recipes)
