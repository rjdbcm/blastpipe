config_files = [
    '__init__.py',
    'backports.py',
    'buffer.py',
    'loop.py',
    'malloc.py',
    'mixin.py',
    'sequence.py',
    'tailcall.py',
]
python_files += files(config_files)
if get_option('dev').enabled()
foreach file: config_files
configure_file(input: file, output: file, configuration: source_to_build)
endforeach endif
