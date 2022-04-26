import r2pipe, sys
import xml.dom.minidom
from Helper.pipeHelper import *
from termcolor import colored

pipe = createR2Pipe()
if pipe is None:
    print(colored("only callable inside a r2-instance!", "red", attrs=["bold"]))
    exit(0)

strings_list = pipe.cmdj('izj')
for s in strings_list:
    if '<?xml' in s['string']:
        print(hex(s['vaddr']), ':')
        xml = s['string']
        print(xml.encode('utf-8').decode('unicode-escape'))
