"""Module: Ezored"""

import colorama
from modules import command


# -----------------------------------------------------------------------------
def run(ezored_path, proj_path, args):
    colorama.init()
    command.process_command(ezored_path, proj_path, args[1:])
