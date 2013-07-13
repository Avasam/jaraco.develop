#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

with open('README.txt') as readme:
	long_description = readme.read()
with open('CHANGES.txt') as changes:
	long_description += '\n\n' + changes.read()

setup_params = dict(
	name='{project_name}',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="{project_name}",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/{project_name}",
	packages=setuptools.find_packages(),
	namespace_packages=['{namespace}'],
	zip_safe=False,
	setup_requires=[
		'hgtools',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
