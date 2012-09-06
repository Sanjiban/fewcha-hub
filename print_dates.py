#!/usr/bin/env python
from git import *
import time
repo=Repo('/home/sanjiban/fewcha-hub')
commit_list=repo.iter_commits('master')
for my_commit in commit_list:
	print time.asctime(time.gmtime(my_commit.committed_date))
