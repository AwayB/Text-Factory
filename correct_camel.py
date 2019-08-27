import re
from FSGate import swallow_file, dump_in_file
import sys


def correct(file):
    target = swallow_file(file)
    convert(target)
    dump_in_file(file, convert(target))

def convert(name):
    s1 = re.sub('(.[^"\'])([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

correct(sys.argv[1])