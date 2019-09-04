from os import path, getcwd, walk
from os.path import join
import sys
from datetime import datetime

swd = getcwd() #starting working directory

###########################Checkers###########################

def are_files_in(folder, files, dealbreaker=True):
    "In a folder, will check if the given files exist. Returns a list of absentees."
    absentees = []
    for filename in files:
        if is_file_in(folder, filename, dealbreaker) == False:
            absentees.append(path.join(folder, filename))
    return(absentees)

def is_file_in(folder, filename, dealbreaker=True):
    "In a folder, will check if the given file exists. If an absent file is a dealbreaker, aborts the program."
    if not (path.isfile(path.join(folder, filename))):
        if dealbreaker == True:
            print ("Mandatory file '" + path.join(folder, filename) + "' was not found. Aborting program.")
            sys.exit()
        return (False)
    return(True)


###########################Searchers###########################
def find(target_file, source_folder=None, recursive=True, multiple=False):
    'Finds the file/folder inside source_folder. if multiple == true, will return all files/folders matching the name.'
    if source_folder == None:
        source_folder = swd
    if recursive and multiple == True:
        return [join(folder, name) for folder, name in walk(source_folder)[1:] if name == target_file]
    elif recursive == True and multiple == False:
        for folder, name in walk(source_folder)[1:]:
             if name == target_file:
                return (join(folder,name))
    else:
        if path.exists(join(source_folder, target_file)):
            return join(source_folder, target_file)
    pass


###########################Readers###########################
def swallow_file(filename, byte_text=True):
    "Will read a whole file and return its contents."
    try:
        with open(filename, "rb" if byte_text==True else "r") as targetfile: targettext = targetfile.read()
    except IOError as e: return(print(e))
    return(targettext)

###########################Writers###########################

def save(contents):
    "Will save the contents in program_name + _save."
    try:
        targetfile = open(sys.argv[0] + '_save', "w")
        targetfile.write(contents)
    except IOError as e:
        print(e)
        return
    finally:
        targetfile.close()

def save_by_date(contents):
    "will save the contents in program_name + date + _save."
    try:
        targetfile = open(sys.argv[0] + datetime.today() + '_save', "w")
        targetfile.write(contents)
    except IOError as e:
        print(e)
        return
    finally:
        targetfile.close()

def save_as(filename, contents):
    "will save the contents in the given file."
    try:
        targetfile = open(filename, "w")
        targetfile.write(contents)
    except IOError as e:
        print(e)
        return
    finally:
        targetfile.close()

def dump_in_file(filename, contents, folder=swd, byte_text=False):
    """Will write the string or byte contents in folder/filename."""
    try:
        with open(join(folder + filename), 'w' if (byte_text == False) else 'wb') as _: _.write(contents)
    except IOError as e: print(e)

def append_to_file(filename, contents, folder=swd, byte_text=False):
    """Will append the string or byte contents in folder/filename."""
    try:
        with open(join(folder + filename), 'a' if (byte_text == False) else 'ab') as targetfile: targetfile.write(contents)
    except IOError as e: print(e)