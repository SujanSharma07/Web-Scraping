# -*- coding: utf-8 -*-
"""Python App That Tracks AliBaba Prices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gD6YKxJ5M6pC5OkUFgwvvuDZFOHrcGQT

Step 0: Set Up environment
"""

pip install requests

pip install html5lib

pip install bs4

# Commented out IPython magic to ensure Python compatibility.
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import smtplib
import seaborn as sns
# %matplotlib inline

from bs4 import BeautifulSoup

url="https://www.alibaba.com/product-detail/Newest-Nepal-copper-beads-Tibetan-inlay_62035851052.html"

"""Step 1 : Get the HTML"""

r=requests.get(url)
htmlContent=r.content
print(htmlContent)

"""Step 2 : Parse the HTML"""

soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

"""Step 3: HTML Tree Traversal"""

title=soup.title
print(title)

print(soup.get_text())

soup.find_all('span','priceVal')#(tag having specified class)

a=soup.find('span','priceVal')
price=a.get_text() #/a.string
s1=price[1:10]
s1
#price 1(s1)

b= soup.find(title='$4.25')#find_all use garda .string use garna mildaina
priced=b.string
s2=priced[1:10]
s2
# price 2(s2)

def send_mail():
  server=smtplib.SMTP("smtp.gmail.com",587)# (host-address and port for gmail)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('example@gmail.com',"dhjkwdrta987654321")
  subject="Price of the Jewelery"
  body="check out the AliBaba product link https://www.alibaba.com/product-detail/Newest-Nepal-copper-beads-Tibetan-inlay_62035851052 for the jewelery"
  msg=f"Subject:{subject}\n \n {body}"
  server.sendmail(
      "dhakhwa@gmail.com",
      "a202@gmail.com",

      msg
      )
  print("mail sent")
  server.quit()

if (s1=='6.50'):# this program can be used to send email when the price goes down but since we cant control the price down so we are using this program to check if the first price is equal to 6.50 or not
  pass

if (s1=='6.50'):
  send_mail()
