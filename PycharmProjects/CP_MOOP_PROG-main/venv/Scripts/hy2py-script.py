#!d:\cprog\venv\scripts\python.exe
# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'hy==0.26.0','console_scripts','hy2py'
__requires__ = 'hy==0.26.0'
import re
import sys

from hy.cmdline import hy2py_main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(hy2py_main())