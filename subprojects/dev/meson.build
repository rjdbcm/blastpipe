# boilerplate python development environment <20 SLoC
project('dev', version: '0.0.1')
env   = environment()
fs    = import('fs')
pymod = import('python')
# emoji
emoji_no_version       = get_option('emoji-no-version')    
emoji_metadata_version = get_option('emoji-metadata-version')
emoji_directory        = get_option('emoji-directory')
emoji_setup            = get_option('emoji-setup')
emoji_dist             = get_option('emoji-dist')
emoji_docs             = get_option('emoji-docs')
emoji_lint             = get_option('emoji-lint')
emoji_test             = get_option('emoji-test')
summary({
 emoji_no_version       : 'non-standard PyPA version metadata',
 emoji_metadata_version : 'standard PyPA version metadata',
 emoji_directory        : 'install directory',
 emoji_setup            : 'developer setup invocations (dev)',
 emoji_dist             : 'distribution               (dist)',
 emoji_docs             : 'documentation              (docs)',
 emoji_lint             : 'linting & typechecking     (lint)',
 emoji_test             : 'testing & checkpointing    (test)',
}, section: '〽️ Configuration Legend')
# prescript arrays
no_version             = get_option('no-version')
unhashable             = get_option('unhashable')
should_fail            = get_option('should-fail')
module_only            = get_option('module-only')
# descript arrays   
namespace              = get_option('namespace')
pytest_plugins         = get_option('pytest-plugins')
python_dependencies    = get_option('python-dependencies')
# features   
dev                    = get_option('dev')
source_to_build        = get_option('source-to-build')
docs_source            = get_option('docs-source')
test_source            = get_option('test-source')
# templates   
core_metadata          = get_option('core-metadata-template')
metadata_version       = get_option('version-metadata-template')
# snippets   
scm_version_snip       = get_option('scm-version-snip')
# Python 3.9+ setup
python = pymod.find_installation('python3', modules: python_dependencies, required: true, 
                                 disabler: true)
pip = find_program('pip', required: true, disabler: true)
# foreach var : get_option('variables')
# if var not in unhashable
# summary({var: get_variable(var.replace('-', '_'))}, section: '🔧')
# endif endforeach
source_to_build.enable_auto_if(source_to_build.auto())
docs_source.enable_auto_if(docs_source.auto())
test_source.enable_auto_if(test_source.auto())
no_check = {'check': false, 'env': env}
install = ['install']
build_commands = {'dev': []}
test_app_args = {}
pip_repr = pip.path()
foreach name: namespace
 command_names = get_option(name+'-suite')
 summary({get_variable('emoji_'+name)+' @0@=auto'.format(name): '[auto|enabled|disabled]'}, 
  section: '🧪 meson setup --reconfigure -D[option]')
 foreach command: command_names
  flag = command in module_only? disabler() : find_program(command, required: false, disabler: true)
  set_variable(command.replace('-', '_'), flag)
  requirements = ['-vvv', '-r', name/command/'requirements.txt']
  install += requirements
  build_commands += {name: ['install'] + requirements}
  set_variable(name, get_option(name).enable_auto_if(get_option('dev').enabled()))
  set_variable(name+'_kwargs', {'suite': name, 'env': env})
  _args = get_option('args-'+command)
  command_args = []
  foreach arg : _args
   if arg.startswith('@') and arg.endswith('@')
    arg = arg.strip('@')
    arg = is_variable(arg)? get_variable(arg) : arg
   endif
   command_args += arg
  endforeach
  if command not in pytest_plugins
   test_app_args += {command: command_args}
  endif
 endforeach
endforeach
build_commands += {'dev': install}
foreach suite, command_arr : build_commands
 if get_option('dev').auto() or get_option(suite).enabled()
  debug(run_command(pip, command_arr, check: true).stdout())
 endif
 if suite in 'dev'
  break
 endif
endforeach
foreach pytest_plugin : pytest_plugins
 plugin_found = run_command(pip, 'check', pytest_plugin, kwargs: no_check).returncode() == 0
 plugin_found? true : warning('missing plugin @0@'.format(pytest_plugin))
endforeach
done = []
foreach name : namespace
 foreach suite : get_option(name+'-exclude-suites')
  foreach app : get_option(suite+'-suite')
   if app in done
    continue
   endif
   emoji = get_variable('emoji_'+suite)
   header = [emoji, 'meson', 'test', '--setup=@0@'.format(suite)]
   feature = get_variable(suite)
   if app not in no_version
    summary({'📦 '+app: get_variable(app.replace('-', '_')).version()}, section: ' '.join(header))
   endif
   packaged_version = run_command(python, ['-c', metadata_version.format(app)], 
   kwargs: no_check).stdout().strip()
   fallback_version = run_command(pip, ['show', app], kwargs: no_check).stdout().split('\n')
   fallback_version = fallback_version.length() > 2? fallback_version[1].split(':')[1].strip(
   ) : 'unknown'
   if app in no_version
    if packaged_version == ''
     app = '📡 '+app
     version = fallback_version
    else
     app = '📦 '+app
     version = packaged_version
    endif
    if app not in done
     summary({app : version}, section: ' '.join(header))
    endif
   endif
   done += app
  endforeach
 endforeach
endforeach
foreach pytest_plugin : pytest_plugins
 packaged_version = run_command(python, ['-c', metadata_version.format(pytest_plugin)], 
 kwargs: no_check).stdout().strip()
 fallback_version = run_command(pip, ['show', pytest_plugin], kwargs: no_check).stdout(
 ).split('\n')
 fallback_version = fallback_version.length() > 2? fallback_version[1].split(':')[1].strip():\
 'unknown'
 if pytest_plugin in no_version
  summary({emoji_metadata_version+' '+pytest_plugin: fallback_version}, 
          section: '✅ meson test --setup=test')
 else
  summary({'📡 '+pytest_plugin: packaged_version}, section: '✅ meson test --setup=test')
 endif
endforeach
