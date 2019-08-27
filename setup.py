from sys import argv
from setuptools import setup, find_packages

core_files = ('XMLOps', 'tell', 'setup', 'FSGate', 'WebGate')

def full():
    setup(name='TF',
    long_name='Text Factory',
    version='1.0',
    author='Alexandre WEBER',
    author_email='alexandre.weber@amadeus.com',
    url='https://github.com/Oulala-Leon/Text-Factory',
    license='Apache 2.0',
    description="TextWork Factory. All text-based operations should be processable. ETA: A Very Long Time.",
    long_description=open('README.txt').read(),
    package_data=(core_files, 'CSVOps', 'XLSXOps', 'credentials', 'emailOps'),
    install_requires=["lxml", "requests", "psv", "chardet", 'email', 'beautifulsoup4', 'keyring', 'keyrings.cryptfile'])

if (argv[1] == 'full'):
    full()