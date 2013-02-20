from __future__ import print_function

import sys
import restclient
import urlparse
import functools
import argparse
import json
import getpass
import collections

import keyring
from jaraco.util.string import local_format as lf

def create_repository(name, auth, url, private=False):
	make_url = functools.partial(urlparse.urljoin, url)
	headers, content = restclient.POST(make_url('repositories/'),
		params=dict(name=name, is_private=private, scm='hg',
			language='python'),
		async=False,
		headers=dict(Authorization=auth), accept=['text/json'],
		resp=True,
	)
	if not 200 <= int(headers['status']) <= 300:
		print(lf("Error occurred: {headers[status]}"), file=sys.stderr)
		raise SystemExit(1)
	return json.loads(content)

def add_version(project, version, auth, url):
	"""
	project should be something like user/project
	"""
	make_url = functools.partial(urlparse.urljoin, url)
	url = make_url(lf('repositories/{project}/versions'))
	headers, content = restclient.POST(
		url,
		params=dict(name=version),
		async=False,
		headers=dict(Authorization=auth),
		accept=['text/json'],
		resp=True,
	)
	if not 200 <= int(headers['status']) <= 300:
		print(lf("Error occurred: {headers[status]}"), file=sys.stderr)
		raise SystemExit(1)
	return json.loads(content)

Credential = collections.namedtuple('Credential', 'username password')

def get_mercurial_creds(system, username=None):
	"""
	Return named tuple of username,password in much the same way that
	Mercurial would (from the keyring).
	"""
	# todo: consider getting this from .hgrc
	username = username or getpass.getuser()
	keyring_username = '@@'.join((username, system))
	system = 'Mercurial'
	password = keyring.get_password(system, keyring_username)
	if not password:
		password = getpass.getpass()
	return Credential(username, password)

def print_result(res):
	width = max(len(key) for key in res) + 1
	for key, value in res.iteritems():
		print(lf("{key:<{width}}: {value}"))

def basic_auth(userpass):
	return 'Basic ' + userpass.encode('base64')

def create_repository_cmd():
	parser = argparse.ArgumentParser()
	parser.add_argument('repo_name')
	parser.add_argument('-a', '--auth', type=basic_auth,
		default = ':'.join(get_mercurial_creds('https://bitbucket.org'))
	)
	parser.add_argument('-u', '--url', default='https://api.bitbucket.org/1.0/')
	parser.add_argument('-p', '--private', default=False,
		action="store_true")
	args = parser.parse_args()
	res = create_repository(args.repo_name, args.auth, args.url,
		private = args.private)
	print_result(res)

if __name__ == '__main__':
	create_repository_cmd()
