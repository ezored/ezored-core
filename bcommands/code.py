"""Code manager tool"""

import os
import subprocess

from app import const
from modules import file
from modules import log
from modules import runner


# -----------------------------------------------------------------------------
def run(params):
    args = params['args']

    if len(args) > 0:
        action = args[0]

        if action:
            if action == 'format':
                code_format(params)
            else:
                show_help(params)
        else:
            show_help(params)
    else:
        show_help(params)


# -----------------------------------------------------------------------------
def code_format(params):
    check_clang_format()

    proj_path = params['proj_path']

    dir_list = [
        {
            'path': os.path.join(
                proj_path,
                const.DIR_NAME_FILES,
                const.DIR_NAME_FILES_SRC,
            ),
            'patterns': ['*.cpp', '*.hpp']
        },
        {
            'path': os.path.join(
                proj_path,
                const.DIR_NAME_PROJECTS,
            ),
            'patterns': ['*.cpp', '*.hpp']
        }
    ]

    if dir_list:
        log.info('Formating files...')

        for dir_item in dir_list:
            patterns = dir_item['patterns']

            for pattern_item in patterns:
                files = file.find_files(dir_item['path'], pattern_item)

                for file_item in files:
                    log.info('Formatting file "{0}"...'.format(
                        os.path.relpath(file_item)
                    ))

                    run_args = [
                        'clang-format',
                        '-style',
                        'file',
                        '-i',
                        file_item,
                    ]

                    runner.run(
                        run_args,
                        proj_path
                    )

        log.ok()
    else:
        log.error('No djinni modules to generate')


# -----------------------------------------------------------------------------
def check_clang_format():
    """Checks if invoking supplied clang-format binary works."""
    try:
        subprocess.check_output(['clang-format', '--version'])
    except OSError:
        log.error('Clang-format is not installed')


# -----------------------------------------------------------------------------
def show_help(params):
    log.colored('Available actions:\n', log.PURPLE)
    log.normal('  - format')


# -----------------------------------------------------------------------------
def get_description(params):
    return 'Code manager tool'
