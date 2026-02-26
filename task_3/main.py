from pathlib import Path
from function import *
import sys

com_line_arg = [arg for arg in sys.argv]
file_path = Path(com_line_arg[1])

if len(com_line_arg) > 2:
    option_arg = com_line_arg[2]
else:
    option_arg = 0

print(load_logs(file_path))