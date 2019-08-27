"""Setuptools entry point."""
import codecs
import os
import pathlib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(dist_directory: str) -> str:
    with open(pathlib.Path(__file__).parent / '{dist_directory}/version.txt'.format(dist_directory=dist_directory), mode='r') as version_file:
        version = version_file.readline()
    return version


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

description = 'Regexp related'

dirname = os.path.dirname(__file__)
readme_filename = os.path.join(dirname, 'README.rst')

long_description = description
if os.path.exists(readme_filename):
    try:
        readme_content = codecs.open(readme_filename, encoding='utf-8').read()
        long_description = readme_content
    except Exception:
        pass

setup(name='lib_regexp',
      version=get_version('lib_regexp'),
      description=description,
      long_description=long_description,
      long_description_content_type='text/x-rst',
      author='Robert Nowotny',
      author_email='rnowotny1966@gmail.com',
      url='https://github.com/bitranox/lib_regexp',
      packages=['lib_regexp'],
      classifiers=CLASSIFIERS,
      install_requires=[],
      setup_requires=['pytest-runner'],
      # requirements for pip install --install-options: test and setup.py test
      tests_require=['mypy ; platform_python_implementation != "PyPy" and python_version >= "3.5"',
                     'pytest',
                     'pytest-pep8 ; python_version < "3.5"',
                     'pytest-codestyle ; python_version >= "3.5"',
                     'pytest-mypy ; platform_python_implementation != "PyPy" and python_version >= "3.5"']
      )
