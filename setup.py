from sys import argv
from setuptools import setup, find_packages

def full():
    setup(name='therig',
    version='0.1',
    author='Alexandre WEBER',
    author_email='alexandre.weber@amadeus.com',
    url='https://github.com/KingArrkinian/Text-Factory',
    license='Apache 2.0',
    description="Massive text-oriented operating system. All text-based operations should be processable. ETA: A Very Long Time.",
    long_description=open('README.md').read(),
    package_data={'Rig':'*.py', 'Rig/Chambre':'*.py','Rig/Control':'*.py','Rig/Engine':'*.py','Rig/Factory':'*.py', 'Rig/Hold':'*.py','Rig/Lobby':'*.py','Rig/Platforms':'*.py','Rig/Reactor':'*.py',},
    install_requires=["virtualenv","lxml", "requests", "psv", "chardet", 'email', 'beautifulsoup4', 'keyring', 'keyrings.cryptfile'])

if (argv[1] == 'full'):
    argv[1] = 'install'
    full()