import urllib2
import string
from bs4 import BeautifulSoup
import re

class School:
	def __init__(self, name, url):
		self.name = name
		self.url = url #url listing courses

class Course:
	def __init__(self, name, description):
		self.name = name
		self.description = description

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
	course_names = re.findall('COMP [0-5]\d*', html)
	uniq_names = list(set(course_names))
	uniq_names.sort()
	getCourseDescriptions(uniq_names)

	names_file = open(School.name + '_courses.txt', 'w')

	# put each course in school_courses file exactly once
	for course in (uniq_names):
		names_file.write(course + '\n')

	names_file.close()

def getCourseDescriptions(course_list):
	for course in course_list:
		course = Course(course)


# Construct objects for schools, extract data from their websites
McGill = School('McGill', 'https://www.cs.mcgill.ca/academic/courses/all_courses')
Concordia = School('Concordia', 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#b71.70.10')
Carleton = School('Carleton', 'http://calendar.carleton.ca/undergrad//courses/COMP/')
extractCourseCatalog(McGill)
extractCourseCatalog(Concordia)
extractCourseCatalog(Carleton)
