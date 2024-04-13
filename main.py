# How to convert Dataclass to JSON in Python 

import json
from dataclasses import dataclass, asdict


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_available: int = 0


item1 = InventoryItem('A', 100, 1)
print(item1)

print('-' * 50)

to_json = json.dumps(asdict(item1))
print(to_json)

print('-' * 50)

print(type(to_json))
