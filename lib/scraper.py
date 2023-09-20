from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# returns a list of bs4.element.NavigableString objects
print(doc.select('.heading-primary')[0].contents)

# returns the text without extra space
print(doc.select('.heading-primary')[0].text.strip())

# returns a list of bs4.element.ResultSet, a lot like a list
# each one is a bs4.element.Tag object
courses = doc.select('.heading-25-extrabold.color-black')
for course in courses:
    # prints all the headings as text!
    print(course.contents[0].strip())
# print the name attribute, which is the HTML tag
# in this case, h3 tag
print(courses[0].name)