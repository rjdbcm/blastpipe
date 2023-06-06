"""python template: check package version"""
from importlib.metadata import version
print(version("@0@"))
