#!/usr/bin/env python
# The following code plots a graph of the no. of commits made with the elapse of time from the beginning to the end of the project
import sys, os
from git import *
import time
import matplotlib.pyplot as plt
if(len(sys.argv)!=2):
	sys.exit("Error: Wrong format! Correct format is: './Graph_Creator.py '<path of the cloned git repo from root>")
path=sys.argv[1]
if(not(os.path.exists(path))):
	sys.exit("Error: Given path does not exist! Please try again...")
repo=Repo(sys.argv[1])
commit_list=repo.iter_commits('master')
date_time_list=[]
yearlist=[]
month_year_list=[]
monthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
for my_commit in commit_list:
	date_time_list.append(time.asctime(time.gmtime(my_commit.committed_date)))
for date in date_time_list:
	month=date.split(' ')[1] #name of month in short form
	year=date.split(' ')[-1] #year
	month_year_list.append(month+' '+year) #<month>" "<year>
finallist=[] #list of "month year" WITHOUT REPITION
finalcomlist=[] #list of no. of commits made in each month present in finallist
for element in month_year_list:
	if element not in finallist:
		finallist.append(element)
		finalcomlist.append(0)
	finalcomlist[finallist.index(element)]+=1
start_y, stop_y = finallist[-1].split(" ")[1], finallist[0].split(" ")[1]
start_m, stop_m = finallist[-1].split(" ")[0], finallist[0].split(" ")[0]
a=[] #list of all the months from beginning to end of project, even those during which no commits were made
b=[] #list of number of commits made in each of the months from beginning to end of project
if start_y==stop_y:
	for i in range(monthlist.index(start_m),monthlist.index(stop_m)+1):
		a.append(monthlist[i]+" "+start_y)
else:
	for i in range(monthlist.index(start_m),12):
		a.append(monthlist[i]+" "+start_y)
	for year in range((int)(start_y)+1,(int)(stop_y)):
		for i in range(0,12):
			a.append(monthlist[i]+" "+str(year))
	for i in range(0,monthlist.index(stop_m)+1):
		a.append(monthlist[i]+" "+str(stop_y))
for element in a:
	if element in finallist:
		b.append(finalcomlist[finallist.index(element)])
	else:
		b.append(0)
time=[a.index(element) for element in a]
plt.plot(time,b)
plt.xlabel("Months elapsed")
plt.ylabel("No. of commits")
plt.axis([0,len(a),0,max(b)+1])
plt.show()
