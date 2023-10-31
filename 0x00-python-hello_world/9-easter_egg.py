#!/usr/bin/python3
import sys
from io import StringIO

backup = sys.stdout
sys.stdout = StringIO()
import this
print(sys.stdout.getvalue(), end='')
sys.stdout = backup
