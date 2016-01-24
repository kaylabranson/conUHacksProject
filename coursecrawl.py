import urllib2
import string
from bs4 import BeautifulSoup
import re

class School:
	def __init__(self, name, url):
		self.name = name
		self.url = url #url listing courses

class Course:
	def __init__(self, name):
		self.name = name

def extractCourseCatalog(School):
	#accesses the url & takes html
	url = urllib2.urlopen(School.url)
	html = url.read()
	#parsing html web content
	txt_content = BeautifulSoup(html, 'html.parser').get_text()
	#creating a file, converting text to unicode, saving file
	txt_name = School.name + '.txt'
	txt_file = open(txt_name, 'w')
	encoded_content = txt_content.encode('utf-8')
	txt_file.write(encoded_content)
	txt_file.close()

	#use regex to find courses, remove duplicates and sort
	course_names = re.findall('^COMP [1-5]\d\d', encoded_content, flags=re.MULTILINE)
	uniq_names = list(set(course_names))
	uniq_names.sort()

	names_file = open(School.name + '_courses.txt', 'w')

	# put each course in school_courses file exactly once
	for course in (uniq_names):
		names_file.write(course + '\n')

	names_file.close()


McGill = School('McGill', 'https://www.cs.mcgill.ca/academic/courses/all_courses')
Concordia = School('Concordia', 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#b71.70.10')

print McGill.name
extractCourseCatalog(McGill)

print Concordia.name
extractCourseCatalog(Concordia)