# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:20:43 2022

@author: wajee
"""

#scraping a live website

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
ycr = response.text

soup = BeautifulSoup(ycr , "html.parser")

headings = soup.find(class_="titlelink")
answer = headings.getText()

print(answer)

article_link = soup.find(name="a",class_ = "titlelink")
href_link = article_link.get("href")
print(href_link)

article_upvotes = soup.find(class_="score",id="score_31797336")
only_upvotes = article_upvotes.getText()
print(only_upvotes)