import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'includes': [
            'testfreeze_1',
            'testfreeze_2'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('main.py'),

]

setup(name='advanced_cx_Freeze_sample',
      version='0.1',
      description='Advanced sample cx_Freeze script',
      options=options,
      executables=executables
      )
