import cmd
from setuptools import setup


# Loads _version.py module without importing the whole package.
def get_version_and_cmdclass(pkg_path):
    import os
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location(
        'version', os.path.join(pkg_path, '_version.py'),
    )
    module = module_from_spec(spec)# type: ignore    
    spec.loader.exec_module(module)# type: ignore
    return module.__version__, module.get_cmdclass(pkg_path)


version, cmdclass = get_version_and_cmdclass('blastpipe')


setup(
    name='blastpipe',
    version=version,
    cmdclass=cmdclass,
    description='Gets projects flowing with boilerplate code!',
    url='http://gitlab.com',
    author='Ross J. Duff',
    author_email='rjdbcm@github.com',
    license='MIT',
    packages=['blastpipe'],
    zip_safe=False
)
