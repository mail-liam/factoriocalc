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
    "Firearm Magazine": {"output": 1, "craft_time": 1, "inputs": {"Iron Plate": 4}},
    "Piercing Rounds Magazine": {
        "output": 1,
        "craft_time": 3,
        "inputs": {"Copper Plate": 5, "Steel Plate": 1, "Firearm Magazine": 1},
    },
    "Grenade": {
        "output": 1,
        "craft_time": 8,
        "inputs": {"Coal": 10, "Iron Plate": 5},
    },
    "Wall": {"output": 1, "craft_time": 0.5, "inputs": {"Stone Brick": 5}},
    "Military Science": {
        "output": 2,
        "craft_time": 10,
        "inputs": {"Piercing Rounds Magazine": 1, "Grenade": 1, "Wall": 2},
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