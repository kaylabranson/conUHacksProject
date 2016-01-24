import urllib2
import string
from bs4 import BeautifulSoup

class School:
	def __init__(self, name, url):
		self.name = name
		self.url = url #url listing courses

class Course:
	def __init__(self, name):
		self.name = name

def extractCourseCatalog(School):
	url = urllib2.urlopen(School.url)
	html = url.read()
	txt_content = BeautifulSoup(html, 'html.parser').get_text()
	txt_name = School.name + '_content.txt'
	txt_file = open(txt_name, 'w')
	txt_file.write(html)
	txt_file.close()


McGill = School('McGill', 'https://www.cs.mcgill.ca/academic/courses/all_courses')
Concordia = School('Concordia', 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#b71.70.10')

print McGill.name
extractCourseCatalog(McGill)

print Concordia.name
extractCourseCatalog(Concordia)