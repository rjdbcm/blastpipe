"""python template: check core metadata"""
import pathlib
import os
#
import tomli
# pylint: disable=consider-using-with
source = pathlib.Path(os.environ.get("MESON_SOURCE_ROOT", ".."))
project_file = open(source/"pyproject.toml", "rb")
pyproject_toml = tomli.load(project_file)
project_file.close()
core_metadata = pyproject_toml.get("project", {"optional_dependencies": {}})
print(core_metadata.get("optional_dependencies", {"todo": []}).get("@0@", "fail"))
