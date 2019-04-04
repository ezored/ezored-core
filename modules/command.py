"""Module: Base commands"""

import glob
import importlib
import os
import sys
from collections import OrderedDict

from app import const

ezored_commands = OrderedDict()


# -----------------------------------------------------------------------------
def get_all_commands(ezored_path, proj_path, args):
    """
    Create command dictionary

    :param proj_path: project root path
    :param ezored_path: ezored path
    :param args: call arguments
    """
    # search on ezored path
    sys.path.insert(0, ezored_path)

    command_list = glob.glob(os.path.join(ezored_path, 'bcommands', '*.py'))

    if command_list:
        for command_path in command_list:
            command_name = os.path.basename(command_path)
            command_name = os.path.splitext(command_name)[0]

            if command_name.startswith('__'):
                continue

            command_module = importlib.import_module('bcommands.{0}'.format(
                command_name
            ))

            ezored_commands[command_name] = command_module

    # search on project path
    project_command_path = os.path.join(
        proj_path,
        const.DIR_NAME_FILES,
    )

    sys.path.insert(0, project_command_path)

    command_list = glob.glob(os.path.join(
        project_command_path,
        const.DIR_NAME_FILES_COMMANDS,
        '*.py',
    ))

    if command_list:
        for command_path in command_list:
            command_name = os.path.basename(command_path)
            command_name = os.path.splitext(command_name)[0]

            if command_name.startswith('__'):
                continue

            command_module = importlib.import_module('{0}.{1}'.format(
                const.DIR_NAME_FILES_COMMANDS,
                command_name,
            ))

            ezored_commands[command_name] = command_module


# -----------------------------------------------------------------------------
def run_method(command_name, method, params):
    """Run target with verb"""

    if command_name in ezored_commands.keys():
        method = getattr(ezored_commands[command_name], method)
        return method(params)


# -----------------------------------------------------------------------------
def show_help(params):
    """
    Show help message of command

    :param params: parameters
    """
    params['command_name'] = 'show_help'
    ezored_commands['help'].run(params)


# -----------------------------------------------------------------------------
def process_command(ezored_path, proj_path, args):
    """
    Entrypoint to call commands

    :param proj_path: project root path
    :param ezored_path: ezored path
    :param args: call arguments
    """
    get_all_commands(ezored_path, proj_path, args)

    params = {
        'args': args,
        'ezored_path': ezored_path,
        'proj_path': proj_path,
    }

    if len(args) > 0:
        command_name = str(args[0])
        args.pop(0)

        if command_name in ezored_commands.keys():
            params['command_name'] = command_name
            ezored_commands[command_name].run(params)
        else:
            show_help(params)
    else:
        show_help(params)
