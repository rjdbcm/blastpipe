config_files = [
    'test_backports.py',
    'test_loop.py',
    'test_malloc.py',
    'test_mixin.py',
    'test_tailcall.py',
]
python.install_sources(files(config_files), install_tag: 'python-tests')
if get_option('dev').enabled()
foreach file: config_files
configure_file(input: file, output: file, configuration: source_to_build)
endforeach endif