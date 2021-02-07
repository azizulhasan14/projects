from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#CCC variables
titleClass = "h1"
titleName = "_1GTSsh _2Q73m9"
ratingClass = "span"
ratingName = "XqYSS8 AtzNiv"
synopsisClass = "div"
synopsisName = "_3qsVvm _1wxob_"
storeFrontURL = "https://www.amazon.com/gp/video/storefront/"
vidDownloadURL = "/gp/video/detail"

videoLinks = []
titles = []
ratings = []
synopsis = []

def scrapeText(lst, classType, className):
    findCLass = soup.find_all(classType, class= className)
    if len(findCLass) == 0:
       lst.append(None)
    else:
        for n in findCLass:
            if className == ratingName:
                lst.append(float(n.text[-3:]))
            else:
                lst.append(n.text)
            

#Initialize browser to be controlled by Python
driver = webdriver.Chrome(executable_path=r"C:\Users\Azizul Hasan\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(storeFrontURL)

elems = driver.find_element_by_xpath("//a[@href]")
for elem in elems:
    if vidDownloadURL in elem.get_attribute("href"):
        videoLinks.append(elem.get_attribute("href"))

for i in range(0,10):
    driver.get(videoLinks[i])
    content = driver.page_source
    soup = BeautifulSoup(content)

    scrapeText(titles, titleClass, titleName)
    scrapeText(ratings, ratingClass, ratingName)
    scrapeText(synopsis, synopsisClass, synopsisName)

print(titles)