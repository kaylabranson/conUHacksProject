import urllib2

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
	html_txt_name = School.name + '_html.txt'
	html_txt_file = open(html_txt_name, 'w')
	html_txt_file.write(html)
	html_txt_file.close()

McGill = School('McGill', 'https://www.cs.mcgill.ca/academic/courses/all_courses')
Concordia = School('Concordia', 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#b71.70.10')

print McGill.name
extractCourseCatalog(McGill)

print Concordia.name
extractCourseCatalog(Concordia)
