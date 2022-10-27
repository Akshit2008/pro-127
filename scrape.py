from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/kulka/Desktop/pro 127/chromedriver")
header=["name", "Distance","Mass","Radius"]
star_data=[]
temp_list = []

def scrape():
    browser.get(START_URL)
    time.sleep(10)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    for th_tag in soup.find_all("th"): 
         tr_tag = th_tag.find_all("tr")
    
    for index, tr_tag in enumerate(tr_tag):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")

star_data.append(temp_list)
browser.find_element_by_xpath('//*[@id="mw-hidden-catlinks"]/ul/li[1]/a').click()

with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(star_data)
scrape()
