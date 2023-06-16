
# pylint: disable=unused-import
try:
    import toml
except ImportError:
    import tomli as toml

import setuptools

class OZICommand(setuptools.Command):
    pass
