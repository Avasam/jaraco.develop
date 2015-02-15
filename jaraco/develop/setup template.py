#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import io

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()
with io.open('CHANGES.txt', encoding='utf-8') as changes:
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
	install_requires=[
	],
	setup_requires=[
		'hgtools',
		'pytest-runner',
		'sphinx',
	],
	tests_require=[
		'pytest',
	],
	license='MIT',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
