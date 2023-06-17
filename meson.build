project('blastpipe', default_options: ['warning_level=3'], license: 'LICENSE', 
 license_files: ['LICENSE.txt'], meson_version: '>=1.1.0', version: run_command(
  'python3', # scm_version_snip
  ['-c', 'from setuptools_scm import get_version;print(get_version(normalize=False))'], 
  check:true
 ).stdout().strip()
)
env             = environment()
source_root     = meson.current_source_dir()
build_root      = meson.current_build_dir()
fs              = import('fs')
pymod           = import('python')
project_name    = get_option('project-name'   ).auto()? meson.project_name() : 'todo'
build_dir       = get_option('build-dir'      ).auto()? fs.stem(build_root)  : 'todo'
source_to_build = get_option('source-to-build').auto()? configuration_data() : 'todo'
docs_source     = get_option('docs-source'    ).auto()? 'subprojects/docs'   : 'todo'
test_source     = get_option('test-source'    ).auto()? 'tests'              : 'todo'
dev  = subproject('dev')
foreach var : get_option('variables')
 name = var.replace('-', '_')
 set_variable(name, dev.get_variable(name))
endforeach
docs = subproject('docs')
scm_version = run_command(python, ['-c', scm_version_snip], check:true).stdout().strip()
foreach source : ['README.rst', 'CHANGELOG.md', 'pyproject.toml', 'NOTICE.md', 'LICENSE.txt']
 configure_file(input: source, output: source, configuration: source_to_build)
endforeach
python_files = []
stub_files = []
foreach dir : [project_name, test_source]
 subdir(dir)
endforeach
foreach file : python_files
 python.install_sources(file)
endforeach
stubs = custom_target('stubs', install: true, install_dir: get_option('prefix'),
 output: stub_files, build_by_default: true, 
 command: [find_program('pyright', required: true), '--createstub', project_name])
foreach dir : ['prefix', 'bindir', 'libdir', 'datadir', 'localedir', 'python.install_env', 
                'python.platlibdir', 'python.purelibdir']
  summary({'📁 '+dir : get_option(dir)}, section: '〽️ meson install -C @0@'.format(build_dir))
endforeach