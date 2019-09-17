import sys

def check_arglen(argv, minimum, maximum=-1):
    "Checks arguments length vs expected minimum and maximum."
    maximum = minimum if maximum == -1 else maximum
    size = len(argv)
    return size if size >= minimum and size <= maximum else sys.exit(f"Expected arguments between {minimum} and {maximum}. Found {size}.")

def contents(entry):
    "Quick debug."
    if (type(entry) == tuple or list or set):
        for each in entry:
            print(each)
    elif (type(entry) == dict):
        for key, value in entry:
            print(key, value)
    else:
        print(entry)

def get_final_values(iterable):
    """Returns every unique final value (non-list/tuple/dict/set) in an iterable.
    
    For dicts, returns values, not keys."""
    ret = list()
    if type(iterable) == dict:
        return(get_final_values(list(iterable.values())))
    for entry in iterable:
        if (type(entry) == tuple or type(entry) == list or type(entry) == set):
            ret.extend(get_final_values(entry))
        elif (type(entry) == dict):
            ret.extend(get_final_values(entry.values()))
        else:
            ret.extend(iterable)
    return(set(ret))

check_arglen(("thtfh","thth","thyyegrdht",'thrg','trherg'),2,3)