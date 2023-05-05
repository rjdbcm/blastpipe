project('lemprex',
    license: 'LICENSE',
    version: run_command('python3', ['-c', 'from setuptools_scm import get_version;print(get_version(normalize=False))'], check:true ).stdout().strip(),
    default_options: [
        'warning_level=3',
        'c_std=c2x',
        # I strongly prefer to use c2x and suppress the warnings on a per-target basis   
        # 'version=@0@'.format(
        # run_command('python3',['-c', 'from setuptools_scm import get_version;print(get_version(normalize=False))'], check:true).stdout().strip()
        # )
    ]
)
NOTICE = '''
╭------------------------ Rubini Distribution -------------------------╮   o                |
|                     -*- NOT FOR OUTSIDE USE -*-                      |             .     -O
|                       SEE LICENSE INFORMATION                        |  .                 |
| License Information:                                                 |         *  o     .  
|        Copyright (c) 2023 Ross J. Duff MSc                           |                .    
|        Developed for the Rubini Project by Peculiar Software         |     *             * 
| Notice:                                                              |           .         
|        This distribution includes software(s) licensed under the     |                  .      
|        Apache License 2.0, modified by Ross J. Duff MSc, and         |      |     .    
|        developed for use in the Rubini Project by Peculiar Software. |     -O-      
|                                                                      |      |       *
╰----------------------------------------------------------------------╯              
'''
python_paths = [join_paths(meson.current_build_dir(), '..')]
python = import('python').find_installation('python3', required: true)
python_dep = python.dependency(embed:true, disabler:true)
scm_version = run_command(python, 
    ['-c', 'from setuptools_scm import get_version;print(get_version(normalize=False))'],
    check:true
).stdout().strip()
subdir('lemprex')