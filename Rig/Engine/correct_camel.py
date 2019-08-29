from os import getcwd
import sys
sys.path.append('C:\\Users\\aweber\\Downloads\\Text-Factory')
print(sys.path)
import re
from Rig.Hold.filesystem_gate import swallow_file, dump_in_file


def correct(file):
    target = swallow_file(file)
    convert(target)
    dump_in_file(file, convert(target))

def convert(name):
    s1 = re.sub('(.[^"\'])([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

correct(sys.argv[1])