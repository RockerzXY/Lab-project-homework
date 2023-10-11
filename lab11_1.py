# Лаб 11. Задание 1.
from pathlib import Path
import yaml
from pprint import pprint


with open(Path('files/yaml_int1.yml')) as f:
    yaml_data = yaml.safe_load(f)

pprint(yaml_data)
