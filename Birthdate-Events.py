# 18th September 2023
# CSC461 – Assignment1 – Web Scraping 
# H. M. Adil Javaid
# FA21-BSE-006
# In this task get the famous personalities born and historical events happened in birthdate


import requests
from bs4  import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

file = "Birth-Events.txt"
mode = 'w'

url1 = requests.get("https://www.timeanddate.com/on-this-day/october/25",headers=headers)
url2 = requests.get("https://www.britannica.com/more-on-this-day/October-25",headers=headers)

soup1 = BeautifulSoup(url1.content,"html.parser")
soup2 = BeautifulSoup(url2.content,"html.parser")
date_share = soup1.find("div",attrs={"class": "otd-life__block"}).text.strip()

elements = soup2.find_all("div",attrs={"class":"card-body"})
event_happened = "\n\n".join(element.text.strip() for element in elements)


with open(file, mode) as file:
    file.write(date_share + '\n\nEvents Happened in 25th October:\n\n' + event_happened)
