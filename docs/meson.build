all = ['conf.py', 'index.rst']
foreach source : all
    configure_file(input: source, output: source, configuration: source_to_build)
endforeach
# TODO: add static files and templates to documentation
install_emptydir('_templates')
install_emptydir('_static')