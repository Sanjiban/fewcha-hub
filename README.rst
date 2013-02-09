fewcha-hub
==========
AIM
--------
This tool creates a graph of the commit history of the git repo which is entered by the user

TOOLS USED
-----------
- GitPython
- matplotlib

DESCRIPTION
------------
This is a command-line based program, the purpose of which, is to draw a graph of the no. of commits made by the author of the git repo inputted by the user, with time.
Since I am using matplotlib, so the x-axis is not labeled with the names of the months, but instead with the number of months elapsed, and the respective no. of commits
made, is being shown in the y-axis, thus creating a graph rather than a histogram. 
This code is going to work for any and every project that was done in github; the only requirement is that, the project on which you want to apply it, must be cloned
in your machine from beforehand. Then you just need to pass the path of the folder of the cloned project as command-line argument during running the program, and the
required graph will come out.
The output that has been shown in the example is for the software Marble.