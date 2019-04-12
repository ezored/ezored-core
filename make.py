#!/usr/bin/env python

import os
import sys

from modules import ezored

ezored_path = os.path.dirname(os.path.abspath(__file__))
proj_path = ezored_path

proj_path = '/Users/paulo/Developer/workspaces/cpp/ubook-sdk-mobile'

if __name__ == '__main__':
    ezored.run(ezored_path, proj_path, sys.argv)
