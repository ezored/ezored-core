#!/usr/bin/env python

import os
import sys

from modules import ezored

ezored_path = os.path.dirname(os.path.abspath(__file__))
proj_path = ezored_path

if __name__ == "__main__":
    ezored.run(ezored_path, proj_path, sys.argv)
