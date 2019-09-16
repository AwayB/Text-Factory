import os
import site
[site.addsitedir(dirs) for dirs, _, _ in os.walk('.') if str(dirs).split(os.path.sep)[-1][0] != '.' and '.git' not in dirs and '__pyc' not in dirs]

def include(package):
    """It's a goddamned hacky, ugly, but at least EXISTING relative import.
    
    Fuck PEP 328.
    
    Guido's Wrath will be terrible, but at least now we can include(..PEP328_begone)."""
    here = os.path.dirname(__file__)
    target = os.path.join(here, package.strip(str(package.split('.'))[:-1])[:-1])
    goback = os.getcwd()
    os.chdir(target)
    module = __import__(package.split('.')[-1])
    os.chdir(goback)
    return module
