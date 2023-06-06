"""python snippet: grab version info"""
import os
import pathlib

from setuptools_scm import get_version

source = pathlib.Path(os.environ.get("MESON_SOURCE_ROOT", ".."))
print(get_version(str(source), normalize=False))
