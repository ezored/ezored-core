"""Module: Ezored"""

import colorama
from mod import cmd


# -----------------------------------------------------------------------------
def run(ezored_path, proj_path, args):
    colorama.init()
    cmd.process_command(ezored_path, proj_path, args[1:])
