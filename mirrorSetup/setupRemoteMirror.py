#!/usr/bin/env python
import git
import re

organizationName = 'DTU-DABAI'  # DTUComputeCognitiveSystems

repo = git.Repo('.')
assert not repo.bare
repoGit = repo.git

# Get name of repository from the origin
urlOrigin = repoGit.remote('get-url', 'origin')
pattern = '.*/(.*).git'
repoName = re.match(pattern, urlOrigin)
repoName = repoName.group(1)
#print(repoName)

# Set URL for mirror
remoteMirrorURL = 'https://github.com/' + organizationName + '/' + repoName

# Add mirror as remote to local repository
repoGit.remote('add', '--mirror=push', 'mirror_repo', remoteMirrorURL)
