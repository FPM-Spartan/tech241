# shell execution

import os
import subprocess

# store the file path>>
script_dir = os.path.dirname(__file__) # __file__ means THIS file
# store the filepath to the script you want to run>>
script_absolute_path = os.path.join(script_dir + "|shell_scripts.sh")
# calls the shell file and runs it
subprocess.call(['sh', script_absolute_path])