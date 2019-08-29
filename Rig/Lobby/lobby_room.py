import tell
import sys

def check_arglen(argv, minimum, maximum=-1):
    "Checks arguments length vs expected minimum and maximum."
    maximum = minimum if maximum == -1 else None
    size = len(argv)
    return size if size >= minimum and size <= maximum else sys.exit(tell.README())
