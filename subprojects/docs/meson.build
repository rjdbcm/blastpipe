project('blastpipe', version: '1.0.0')
author           = 'Ross J. Duff MSc'
copyright_date   = '2023'
copyright        = ', '.join([copyright_date, author])
sphinx           = find_program('sphinx-build')
html_static_path = get_option('html_static_path')
templates_path   = get_option('templates_path')
pdflatex = find_program('pdflatex', disabler: true)
builder_dirs     = {'html': 'dirhtml', 'man': 'man'}
if pdflatex.found()
 builder_dirs += {'pdf': 'latex'}
endif
foreach dir: [html_static_path, templates_path]
 subdir(dir)
endforeach
all = ['index.rst']
foreach source: all
 configure_file(input: source, output: source, configuration: configuration_data())
endforeach
env = environment()
env.append('PYTHONPATH', meson.global_build_root())
foreach name, builder: builder_dirs 
 sphinx_args = [sphinx, '-C',
  '-Dhtml_static_path='+','.join(html_static_path),
  '-Dexclude_patterns='+','.join(get_option('exclude_patterns')),
  '-Dextensions='      +','.join(get_option('sphinx_ext')),
  '-Dtemplates_path='  +','.join(templates_path),
  '-Dproject='         + meson.project_name(),
  '-Dauthor='          + author,
  '-Dcopyright='       + copyright,
  '-Dhtml_theme='      + get_option('html_theme'),
  '-j', 'auto',
  '-v', # + 'v' # +'v'
  '-W',
  '-E', 
  '-a',
  '-b', builder]
 sphinx_args += meson.project_build_root()
 sphinx_args += '@OUTPUT@'
 custom_target(name, command: sphinx_args, input: all, output: name, env: env,
  build_by_default: true, install: true, install_dir: get_option('datadir'))
endforeach
