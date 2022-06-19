# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:41:57 2022

@author: wajee
"""

#scraping a live website

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
ycr = response.text

soup = BeautifulSoup(ycr , "html.parser")

article_text_list = []
article_links_list =[]
upvotes_list=[]

headings = soup.find_all(name= "a",class_="titlelink")

for article in headings:
    article_text = article.getText()
    article_text_list.append(article_text)



for link in headings:
    article_link = link.get("href")
    article_links_list.append(article_link)


article_upvotes = soup.find_all(name="span",class_="score")

for upvotes in article_upvotes:
    vote = upvotes.getText()
    value = vote.split(" ")
    points = int(value[0])
    upvotes_list.append(points)

print(upvotes_list)

largest_number = max(upvotes_list)
get_index = upvotes_list.index(largest_number)

print(largest_number)
print(get_index)


print(article_links_list[get_index])
print(article_text_list[get_index])