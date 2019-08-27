from sys import argv
from setuptools import setup, find_packages

def full():
    setup(name='TF',
    version='0.1',
    author='Alexandre WEBER',
    author_email='alexandre.weber@amadeus.com',
    url='https://github.com/Oulala-Leon/Text-Factory',
    license='Apache 2.0',
    description="TextWork Factory. All text-based operations should be processable. ETA: A Very Long Time.",
    long_description=open('README.md').read(),
    package_data={'':'*.py'},
    install_requires=["lxml", "requests", "psv", "chardet", 'email', 'beautifulsoup4', 'keyring', 'keyrings.cryptfile'])

if (argv[1] == 'full'):
    name = argv[0]
    argv.clear()
    argv.append(name)
    argv.append('install')    
    full()