#!/usr/bin/env python3

from yaml import safe_load_all
from importlib.resources import files

attributes = safe_load_all(files("config").joinpath("configuration.yml").read_text(encoding='utf8'))

for attr in attributes:
    print(attr)
