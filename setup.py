from setuptools import setup, find_packages

setup(
    name='theoretical_python',
    version='0.0.0',
    author='Stephane Haussler',
    author_email='stephane.haussler@gmail.com',
    description='Theoretical Universe Python Dependencies',
    packages=find_packages(),
    install_requires=[
        'sphinx', 'myst_parser', 'furo', 'sphinx-book-theme',
        'sphinxcontrib-googleanalytics', 'sphinx_sitemap',
        'sphinx-togglebutton', 'sphinx-reredirect',
    ],
)
