# Лаб 11. Задание 2.
from pathlib import Path
import yaml
from pprint import pprint


with open(Path('files/lab11_2_yaml.yml')) as f:
    yaml_data = yaml.safe_load(f)

pprint(yaml_data)

