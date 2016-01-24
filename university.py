#!/usr/bin/env python
import cgi
import csv
import sys
import os 
import stat
form=cgi.FieldStorage()
school= form["school"].value;
print "Content-Type: text/html"
print 
print "<!doctype html>"
print "<html>"
print "hello world"
print "<head>"
print '<link rel="stylesheet" type="text/css" href="main-offcourse.css" media = "screen"/>'
print "</head>"
print"<body>"
print'<div class = "over-lay">' 
print '<p class ="logo">off course</p>' 
print '<p class = "sub-text">all the study materials you need in one search</p>'
print '<form name="input" action="./cgi-bin/university.py" method="post">'
print '<center>Course code: <input type="text" name="course"></center>'
print '</div>'
print '</html>'
