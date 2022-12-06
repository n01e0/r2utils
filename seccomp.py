import r2pipe, sys
import subprocess
from Helper.pipeHelper import *
from termcolor import colored

pipe = createR2Pipe()
if pipe is None:
    print(colored("only callable inside a r2-instance!", "red", attrs=["bold"]))
    exit(0)

binfile = str(pipe.cmdj('ij')['core']['file'])

subprocess.run(f'seccomp-tools dump ./{binfile}', shell=True)
