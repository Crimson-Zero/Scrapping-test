# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:54:46 2022

@author: wajee
"""

from bs4 import BeautifulSoup
website_path = "C:/Users/wajee/.spyder-py3/bs4-start/website.html"

with open(website_path , encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser") #understanding the contents parsing
#soup = BeautifulSoup(contents,"lxml")

#if i want the title tag
title_test = soup.title
print(title_test)

#if I want the name of the title
name_test = soup.title.name
print(name_test)

#if I want the string between the title tag
string_test = soup.title.string
print(string_test)

#to prettify

print(soup.prettify())
print(soup.a) #get first anchor tag
print(soup.p)

#get all paragraphs or all anchor tahs

get_a=soup.find_all(name="a") #all anchor tags
print(get_a)


get_p=soup.find_all(name="p") #all paragraphs
print(get_p)


#Only want the text in the anchor tags

for tag in get_a:
    
    anchor_text=tag.getText()
    print(anchor_text)


#get the aactuall href i.e link the tag goes through

for t in get_a:
   href = t.get("href")
   print(href)

heading = soup.find_all(name="h1",id="name") #will get attribute that has h1 heading and id of name
print(heading)

section = soup.find(name="h3",class_="heading") #will get attribute that has class name heading
print(section)
print(section.getText())

company_url = soup.select_one(selector="p a") #anchor tag that sits in p paragraph
print(company_url)

name_t = soup.select_one(selector ="#name")
print(name_t)

headings = soup.select(".heading")
print(headings)