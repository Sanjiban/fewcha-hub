#!/usr/bin/env python
# The following code prints the no. of commits made and the months in which the commits were made in the master branch of my repo
from git import *
import time
repo=Repo('/home/sanjiban/fewcha-hub')
commit_list=repo.iter_commits('master')
date_time_list=[]
yearlist=[]
month_year_list=[]
shortmonthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
monthlist=['January','February','March','April','May','June','July','August','September','October','November','December'];
for my_commit in commit_list:
	date_time_list.append(time.asctime(time.gmtime(my_commit.committed_date)))
for date in date_time_list:
	month=date.split(' ')[1]
	year=date.split(' ')[-1]
	month_year_list.append(monthlist[shortmonthlist.index(month)]+' '+year)
finallist=[]
finalcomlist=[]
for element in month_year_list:
	if element not in finallist:
		finallist.append(element)
		finalcomlist.append(0)
	finalcomlist[finallist.index(element)]+=1
for month,number in zip(finallist,finalcomlist):
	print number,' commits were made in ',month
