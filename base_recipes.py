assembler = {
    "name": "Assembler",
    "speed": 1.25,
}

electric_furnace = {
    "name": "Electric Furnace",
    "speed": 2,
}

chemical_plant = {
    "name": "Chemical Plant",
    "speed": 1,
}

refinery = {
    "name": "Oil Refinery",
    "speed": 1,
}

recipes = {
    "Iron Gear": {
        "output": 1,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 2}
    },
    "Copper Wire": {
        "output": 2,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Copper Plate": 1}
    },
    "Electronic Circuit": {
        "output": 1,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 1, "Copper Wire": 3},
    },
    "Automation Science": {
        "output": 1,
        "craft_time": 5,
        "machine": assembler,
        "inputs": {"Copper Plate": 1, "Iron Gear": 1},
    },
    "Transport Belt": {
        "output": 2,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 1, "Iron Gear": 1},
    },
    "Inserter": {
        "output": 1,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 1, "Iron Gear": 1, "Electronic Circuit": 1},
    },
    "Logistic Science": {
        "output": 1,
        "craft_time": 6,
        "machine": assembler,
        "inputs": {"Transport Belt": 1, "Inserter": 1},
    },
    "Firearm Magazine": {
        "output": 1,
        "craft_time": 1,
        "machine": assembler,
        "inputs": {"Iron Plate": 4}
    },
    "Steel Plate": {
        "output": 1,
        "craft_time": 16,
        "machine": electric_furnace,
        "inputs": {"Iron Plate": 5},
    },
    "Piercing Rounds Magazine": {
        "output": 1,
        "craft_time": 3,
        "machine": assembler,
        "inputs": {"Copper Plate": 5, "Steel Plate": 1, "Firearm Magazine": 1},
    },
    "Grenade": {
        "output": 1,
        "craft_time": 8,
        "machine": assembler,
        "inputs": {"Coal": 10, "Iron Plate": 5},
    },
    "Stone Brick": {
        "output": 1,
        "craft_time": 3.2,
        "machine": electric_furnace,
        "inputs": {"Stone": 2},
    },
    "Wall": {
        "output": 1,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Stone Brick": 5}
    },
    "Military Science": {
        "output": 2,
        "craft_time": 10,
        "machine": assembler,
        "inputs": {"Piercing Rounds Magazine": 1, "Grenade": 1, "Wall": 2},
    },
    "Pipe": {
        "output": 1,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 1 }
    },
    "Advanced Circuit": {
        "output": 1,
        "craft_time": 6,
        "machine": assembler,
        "inputs": {"Copper Wire": 4, "Electronic Circuit": 2, "Plastic Bar": 2},
    },
    "Engine Unit": {
        "output": 1,
        "craft_time": 10,
        "machine": assembler,
        "inputs": {"Iron Gear": 1, "Pipe": 2, "Steel Plate": 1},
    },
    "Chemical Science": {
        "output": 2,
        "craft_time": 24,
        "machine": assembler,
        "inputs": {"Advanced Circuit": 3, "Engine Unit": 2, "Sulfur": 1},
    },
    "Electric Furnace": {
        "output": 1,
        "craft_time": 5,
        "machine": assembler,
        "inputs": {"Advanced Circuit": 5, "Steel Plate": 10, "Stone Brick": 10},
    },
    "Productivity Module": {
        "output": 1,
        "craft_time": 15,
        "machine": assembler,
        "inputs": {"Advanced Circuit": 5, "Electronic Circuit": 5},
    },
    "Iron Stick": {
        "output": 2,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Iron Plate": 1}
    },
    "Rail": {
        "output": 2,
        "craft_time": 0.5,
        "machine": assembler,
        "inputs": {"Stone": 1, "Iron Stick": 1, "Steel Plate": 1},
    },
    "Production Science": {
        "output": 3,
        "craft_time": 21,
        "machine": assembler,
        "inputs": {"Electric Furnace": 1, "Productivity Module": 1, "Rail": 30},
    },
    "Battery": {
        "output": 1,
        "craft_time": 4,
        "machine": chemical_plant,
        "inputs": {"Iron Plate": 1, "Copper Plate": 1, "Sulfuric Acid": 20}
    },
    "Electric Engine Unit": {
        "output": 1,
        "craft_time": 10,
        "machine": assembler,
        "inputs": {"Electronic Circuit": 2, "Engine Unit": 1, "Lubricant": 15}
    },
    "Flying Robot Frame": {
        "output": 1,
        "craft_time": 20,
        "machine": assembler,
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
        "machine": assembler,
        "inputs": {"Copper Plate": 20, "Plastic Bar": 5, "Steel Plate": 2},
    },
    "Processing Unit": {
        "output": 1,
        "craft_time": 10,
        "machine": assembler,
        "inputs": {"Advanced Circuit": 2, "Electronic Circuit": 20, "Sulfuric Acid": 5},
    },
    "Utility Science": {
        "output": 3,
        "craft_time": 21,
        "machine": assembler,
        "inputs": {
            "Flying Robot Frame": 1,
            "Low Density Structure": 3,
            "Processing Unit": 2,
        },
    },
}