fewcha-hub
==========
AIM
--------
This tool creates a graph of the commit history of the git repo which is entered by the user

TOOLS TO BE USED
-----------------
- GitPython
- matplotlib

DESCRIPTION
------------
This is a command-line based program, the purpose of which, is to draw a graph of the no. of commits made by the author of the git repo inputted by the user, with time.
My actual plan was to create a histogram in which all the months from the beginning to the end of the project will be labeled and the corresponding no. of commits made
in that month would be shown in the histogram. But since I am using matplotlib, so the x-axis could not be labeled with the names of the months, but instead with the
number of months elapsed, and the respective no. of commits made is being shown in the y-axis, thus creating a graph rather than a histogram.