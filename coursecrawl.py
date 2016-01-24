import urllib2
import string
from bs4 import BeautifulSoup
import re

class School:
	def __init__(self, name, url, comp_classes=[]):
		self.name = name
		self.url = url #url listing courses
		self.comp_classes = []

class Course:
	def __init__(self, name, description):
		self.name = name
		self.description = description


def union(a, b):
	relevant_union = (list(set(a) | set(b)))
	irrelevant = ['the', 'in', 'prerequisite' 'this', 'for', 'if', 'will', 'learn', 'of', 'new', 'by', 'through', 'with', 'topics', 'credit', 'while', string.punctuation]

	for word in irrelevant:
		if (word in relevant_union):
			relevant_union.remove(word) 

	return (len(relevant_union))

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

	if (School.name == 'Carleton'):
		getCourseDescriptions(School, uniq_names, txt_content)

	else:
		getCourseDescriptions(School, uniq_names, encoded_content)

	names_file = open(School.name + '_courses.txt', 'w')

	# put each course in school_courses file exactly once
	for course in (uniq_names):
		names_file.write(course + '\n')

	names_file.close()

def getCourseDescriptions(School, course_list, syllabus_data):

	for course in course_list:
		if (School.name == 'McGill'):
			course_pattern = course + r".*?SemesterInstructor"
			course_description = re.findall(course_pattern, syllabus_data, re.DOTALL)
			# print course_description

		if (School.name == 'Concordia'):
			course_pattern = course +  "\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0" + r"(.*?)\nCOMP"
			course_description = re.findall(course_pattern, syllabus_data, re.DOTALL)
			# print course_description

		if (School.name == 'Carleton'):
			coursecode = course.split()
			course_pattern = "COMP" + "\xa0" + coursecode[1] + r"(.*?)\n\nCOMP"
			course_description = re.findall(course_pattern, syllabus_data, re.DOTALL)
			# print course_description

		if course_description:
			course_obj = Course(course, (course_description[0].lower()).split())
			School.comp_classes.append(course_obj)

		else:
			course_obj = Course(course, "NO_DESCRIPTION")
			School.comp_classes.append(course_obj)

def matchClosestCourse(course, Other_School):
	closestMatch = None
	keyCount = 30

	for o_course in Other_School.comp_classes:
		if (abs(int(o_course.name[5]) - int(course.name[5])) <= 1):
			if (union(course.description, o_course.description) > keyCount):
				keyCount = union(course.description, o_course.description)
				closestMatch = o_course

	return closestMatch


# Construct objects for schools, extract data from their websites
McGill = School('McGill', 'https://www.cs.mcgill.ca/academic/courses/all_courses')
Concordia = School('Concordia', 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#b71.70.10')
Carleton = School('Carleton', 'http://calendar.carleton.ca/undergrad//courses/COMP/')
extractCourseCatalog(McGill)
extractCourseCatalog(Concordia)
extractCourseCatalog(Carleton)


for comp_class in McGill.comp_classes:
	if(comp_class.description != "NO_DESCRIPTION"):
		closest_co = matchClosestCourse(comp_class, Concordia)
		closest_ca = matchClosestCourse(comp_class, Carleton)

		if (closest_co and closest_ca):
			print "McGill: " + comp_class.name +  "\t Concordia equivalent: " + closest_co.name + "\t Carleton equivalent: " + closest_ca.name

		elif closest_co:
			print "McGill: " + comp_class.name +  "\t Concordia equivalent: " + closest_co.name

		elif closest_ca:
			print "McGill: " + comp_class.name + "\t Carleton equivalent: " + closest_ca.name

		else:
			print "No equivalents exist of " + comp_class.name + " at Carleton or Concordia."

	else:
		print "No description found for " + comp_class.name + "."
