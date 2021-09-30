
from setuptools import setup, find_packages
from dotbak.core.version import get_version

VERSION = get_version()

f = open('README-pypi.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='dotbak',
    version=VERSION,
    description='Lazily Backup Files and Directories',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='BJ Dierkes',
    author_email='derks@datafolklabs.com',
    url='https://github.com/datafolklabs/dotbak',
    license='BSD (three-clause)',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'dotbak': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        dotbak = dotbak.main:main
    """,
)
