import json
from pathlib import Path

_data = json.loads((Path(__file__).parent / "brands.json").read_text())

brand_a: list = _data["brand_a"]
brand_b: list = _data["brand_b"]
