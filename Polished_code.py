#!/usr/bin/env python
# The following code prints the no. of commits made and the months in which the commits were made in the master branch of my repo
import sys
from git import *
import time
if(len(sys.argv)!=2):
	print("<Frequency.py>" "<path of repository cloned in computer>")
repo=Repo(sys.argv[1])
commit_list=repo.iter_commits('master')
date_time_list=[]
yearlist=[]
month_year_list=[]
shortmonthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
monthlist=['January','February','March','April','May','June','July','August','September','October','November','December'];
for my_commit in commit_list:
	date_time_list.append(time.asctime(time.gmtime(my_commit.committed_date)))
for date in date_time_list:
	month=date.split(' ')[1] #name of month in short form
	year=date.split(' ')[-1] #year
	month_year_list.append(monthlist[shortmonthlist.index(month)]+' '+year) #<name of month in full>" "<year>
finallist=[] #list of "month year" WITHOUT REPITION
finalcomlist=[] #list of no. of commits made in each month present in finallist
for element in month_year_list:
	if element not in finallist:
		finallist.append(element)
		finalcomlist.append(0)
	finalcomlist[finallist.index(element)]+=1
start_y, stop_y = finallist[-1].split(" ")[1],  finallist[0].split(" ")[1]
start_m, stop_m = finallist[-1].split(" ")[0],  finallist[0].split(" ")[0]
a=[]
if start_y==stop_y:
	for i in range(monthlist.index(start_m),monthlist.index(stop_m)+1):
		a.append(monthlist[i]+" "+start_y)
else:
	for i in range(monthlist.index(start_m),12):
		a.append(monthlist[i]+" "+start_y)
	for year in range(start_y+1,stop_y):
		for i in range(0,12):
			a.append(monthlist[i]+" "+year)
	for i in range(0,monthlist.index(stop_m)+1):
		a.append(monthlist[i]+" "+stop_y)
for element in a:
	if element in finallist:
		print element,": ",finalcomlist[finallist.index(element)]
	else:
		print element,": 0"
