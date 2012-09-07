#!/usr/bin/env python
# The following code prints the no. of commits made and the months in which the commits were made in the master branch of my repo
from git import *
import time
repo=Repo('/home/sanjiban/fewcha-hub')
commit_list=repo.iter_commits('master')
commitlist=[]
yearlist=[]
fulllist=[]
shortmonthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
monthlist=['January','February','March','April','May','June','July','August','September','October','November','December'];
for my_commit in commit_list:
	commitlist.append(time.asctime(time.gmtime(my_commit.committed_date)))
for date in commitlist:
	month=date.split(' ')[1]
	year=date.split(' ')[-1]
	fulllist.append(monthlist[shortmonthlist.index(month)]+' '+year)
finallist=[]
finalcomlist=[]
for element in fulllist:
	if element not in finallist:
		finallist.append(element)
		finalcomlist.append(0)
	finalcomlist[finallist.index(element)]+=1
for date,number in zip(finallist,finalcomlist):
	print number,' commits were made in ',date
