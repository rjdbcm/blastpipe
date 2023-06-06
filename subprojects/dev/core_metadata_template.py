"""python template: check core metadata"""
import pathlib
import os

import tomli

source = pathlib.Path(os.environ.get("MESON_SOURCE_ROOT", ".."))
with open(source/"pyproject.toml", "rb") as f:
    pyproject_toml = tomli.load(f)
core_metadata = pyproject_toml.get("project", {"optional_dependencies": {}})
print(core_metadata.get("optional_dependencies", {"todo": []}).get("@0@", "fail"))
