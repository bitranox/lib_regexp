# single point for all configuration of the project

# stdlib
from typing import List, Dict

package_name = 'lib_regexp'  # type: str
version = '0.1.0'
codeclimate_link_hash = "d854dda63a0f89c04032"   # for lib_regexp
cc_test_reporter_id = '47ba059847780d2ab249a2af91aa2804506b7d0c54cc0abb87ed318b41315c50'   # for lib_regexp

# pypi_password
# to create the secret :
# cd /<repository>
# travis encrypt -r bitranox/lib_parameter pypi_password=*****
# copy and paste the encrypted password here
# replace with:
# travis_pypi_secure_code = '<code>'     # pypi secure password, without '"'
travis_pypi_secure_code = 'MkSjzcbEn8UDv4B/DrZ7mAxQcljC4vWk+NsJhB7v3zDF4B/FdCVo5Fds4fIPN4mxjHTln/Y6FBOEbJgje4pqBh1AMW/EfOsJqvmvfRsBqx4cllNB0e2SAPySw5G8'\
                          'mBLwcGC2y+owSUZyjLb/W5J2bjlS0svfw9yklkEgQsQtZe25boo+IF9dNNI7l8fRM3Re15Hso3AySN/plEBVsnOZVgk8UO4roO9BUQ98vhXfhECKhmRJ5VEwfA/g'\
                          '57NANbiTusH8/4vcAI7RZi0jnLGmNLUauVj7AKWLJ7nvepzIVot1xQzTno0uLZ360IuA88a3j/9g/GBxhqzme4QOYqbD+m4aErwnXSXZxoL4ydGCic7oVrBW0ida'\
                          'FSsh/Hdd5D+XcAyIaVirCmmm7enbeaTFZRLcuBgM/YO7dRAi43Qi4alErKNvZebZVUPcYtXsJTKvXLcBmz5/Ju+nbUEc6gtQqjnn6R3JY3jQeSys62TlV0Y4M4VJ'\
                          'S2EVAUWYks/Dsti5+sZqisOhee9z2LqazraQhe4yKZcQRVURrLch4ryV8ZJZZxp3hV3iClSLxSH7XfbOJiyINnZiGeAPL3WZVm7NdYAQremg8i4OPnw0HVR/jeFP'\
                          'zToGh0s+1yxiABJiRYnd0UWS/MqWqwRQKN8JVuRHVBDz4mU9FGUntTtaIXwkWRI='

# include package data files
# package_data = {package_name: ['some_file_to_include.txt']}
package_data = dict()       # type: Dict[str, List[str]]

author = 'Robert Nowotny'
author_email = 'rnowotny1966@gmail.com'
github_account = 'bitranox'

linux_tests = True
osx_tests = True
pypy_tests = True
windows_tests = True
wine_tests = False
badges_with_jupiter = False

# a short description of the Package - especially if You deploy on PyPi !
description = 'some convenience functions for regexp'  # short description - should be entered here

# #############################################################################################################################################################
# DEFAULT SETTINGS - no need to change usually, but can be adopted
# #############################################################################################################################################################

shell_command = package_name
src_dir = package_name
module_name = package_name
init_config_title = description
init_config_name = package_name

# we ned to have a function main_commandline in module module_name - see examples
entry_points = {'console_scripts': ['{shell_command} = {src_dir}.{module_name}:main_commandline'
                .format(shell_command=shell_command, src_dir=src_dir, module_name=module_name)]}  # type: Dict[str, List[str]]

long_description = package_name  # will be overwritten with the content of README.rst if exists

packages = [package_name]

url = 'https://github.com/{github_account}/{package_name}'.format(github_account=github_account, package_name=package_name)
github_master = 'git+https://github.com/{github_account}/{package_name}.git'.format(github_account=github_account, package_name=package_name)
travis_repo_slug = github_account + '/' + package_name

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules']
