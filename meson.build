project('mytool', 'c', version: '0.0.1')

srcs  = files('src/main.c')

exe_install_dir = ''
if get_option('wheel')
    python = import('python').find_installation(pure: false)
    exe_install_dir = join_paths(python.get_install_dir(), 'mytool', 'bin')
else
    exe_install_dir = get_option('bindir')
endif

myexe = executable('mytool', srcs, install: true, install_dir: exe_install_dir)

if get_option('wheel')
    # python executable wrapper
    stub_files = files('py/mytool/__init__.py', 'py/mytool/__main__.py')
    install_data(stub_files, install_dir: join_paths(python.get_install_dir(), 'mytool'))
endif
