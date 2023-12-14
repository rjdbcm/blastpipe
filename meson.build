# OZI 0.1 meson.build:root_files,root_children
# Part of blastpipe.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
project(
    'blastpipe',
    default_options: ['warning_level=3'],
    license: 'Apache-2.0 WITH LLVM-exception',
    license_files: ['LICENSE.txt'],
    meson_version: '>=1.1.0',
    version: run_command(
        'python3',
        [
            '-c',
            'from setuptools_scm import get_version;print(get_version(normalize=False))',
        ],
        check: true,
    ).stdout().strip(),
)
env = environment()
source_root = meson.current_source_dir()
build_root = meson.current_build_dir()
fs = import('fs')
pymod = import('python')
project_name = meson.project_name()
build_dir = fs.stem(build_root)
source_to_build = configuration_data()
docs_source = 'subprojects/docs'
test_source = 'tests'
pip_compile = find_program('pip-compile', required: true)
requirements = ['requirements.in']
custom_target(
    'requirements-blastpipe',
    input: requirements,
    output: 'requirements.txt',
    build_always_stale: true,
    build_by_default: true,
    command: [
        'pip-compile',
        '--allow-unsafe',
        '--strip-extras',
        '-q',
        '--generate-hashes',
        '-o',
        '@OUTPUT@',
        '@INPUT@'
    ]
)
foreach var : get_option('variables')
    name = var.replace('-', '_')
    set_variable(name, dev.get_variable(name))
endforeach
python = pymod.find_installation()
pkg_info_req = 'Requires-Dist: @0@'
required = []
foreach requirement : fs.read('requirements.in').split('\n')
    if requirement != '' and not requirement.startswith('#')
        required += pkg_info_req.format(requirement)
    endif
endforeach
pyproject_config.set(
    'PYTHON_VERSION_DIST',
    'py'+''.join(python.language_version().split('.'))
)
pyproject_config.set('SCM_VERSION', meson.project_version())
pyproject_config.set('VCS_TAG', '@VCS_TAG@')
pyproject_config.set('PROJECT_NAME', project_name)
pyproject_config.set('README_TEXT', fs.read('README.rst'))
pyproject_config.set('REQUIREMENTS_IN', '\n'.join(required))
pyproject_config.set('LICENSE', meson.project_license()[0])
configure_file(
    input: 'pyproject.toml',
    output: 'pyproject.toml',
    configuration: pyproject_config
)
run_command(python, ['-c', replace_ruff_target_version], check: true)
configure_file(command: [python, '-c', meson_setuptools_scm], output: 'PKG-INFO')
meson.add_dist_script(pip, 'install', 'tomli>=2.0.0')
meson.add_dist_script(python, '-c', meson_dist_setuptools_scm)
vcs_tag(input: 'pyproject.toml', output: 'pyproject.toml')
root_files = [
    'README.rst',
    'CHANGELOG.md',
    'LICENSE.txt',
    'requirements.in',
    'NOTICE.md',
]
foreach source : root_files
    fs.copyfile(source)
endforeach
run_command(python, ['-c', sync_pkg_readme], check: true)
if false
    executable('root_files', root_files)
endif
root_children = [
    'blastpipe',
    'tests',
]
foreach child: root_children
    subdir(child)
endforeach
if false
    executable('root_children', root_children)
endif
dev = subproject('ozi')
