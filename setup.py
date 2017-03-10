from setuptools import setup, find packages
from RandPW import __version__, __author__, __email__, __name__

with open('requirements.txt') as f:
	requirements = [line for line in f.read().splitlines() if line]

def long_description():
	with open('README.md', 'rb') as f:
		return str(f.read())

setup(
	name = __name__, 
	version = __version__, 
	packages = find_packages(),

	author = __author__,  
	auther_email = __email__, 
	keyword = 'generate, key, password, random', 
	description = 'A multi-user password manager & generator ', 
	long_description = long_description(), 
	url = 'https://github.com/Gao-Chuan/RandPW', 
	include_package_data = True, 

	install_requires = requirements, 
	entry_points = {
		'console_scripts' : [
			'RandPW = RandPW.command:main',
		]
	}, 
	license='MIT',
)

