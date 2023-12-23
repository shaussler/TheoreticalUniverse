from setuptools import setup, find_packages

setup(
    name='pynotes',
    version='0.0.1',
    author='Stephane Haussler',
    author_email='stephane.haussler@gmail.com',
    description='Notes',
    packages=find_packages(where="./pynotes"),    
    install_requires=['numpy >= 1.11.1'],
)
