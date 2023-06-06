if get_option('dev').enabled()
 add_test_setup('dev', is_default: true, env: env)
 env.append('TESTS_BUILDDIR', build_root)
 env.append('PYTHONPATH'    , build_root)
 pip = find_program('pip', required: false, disabler: true)
 no_check = {'check': false, 'env': env}
 opt_cov_eq_project_name = '--cov='+project_name
 build_commands = {'dev': []}
 test_app_args = {}
 foreach name: namespace
  add_test_setup(name, exclude_suites: get_option(name+'-exclude-suites'))
  set_variable(name, get_option(name).enable_auto_if(get_option('dev').enabled()))
  set_variable(name+'_kwargs', {'suite': name, 'env': env})
  command_names = get_option(name+'-suite')
  foreach command: command_names
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
 foreach app, args : test_app_args
  args = {'args': args, 'env': env}
  foreach name : namespace
   if app in get_option(name+'-suite')
    args += {'suite': name}
    if app in should_fail
     args += {'should_fail': true}
    endif
   endif
  endforeach
  feature = get_variable(args['suite'])
  test_app = feature.enabled()? dev.get_variable(app.replace('-', '_')) : disabler()
  test_app.found() and feature.enabled()? test(app, test_app, kwargs: args) : false
 endforeach
 foreach dir : ['prefix', 'bindir', 'libdir', 'datadir']
  summary({'📁 '+dir : get_option(dir)}, section: '〽️ meson install -C @0@'.format(build_dir))
 endforeach
endif
