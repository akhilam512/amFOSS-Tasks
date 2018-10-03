from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://google.co.in")  

box = driver.find_element_by_xpath('//*[@id="lst-ib"]')    #selecting search text box

keyword = raw_input( "Enter keyword" )
box.send_keys(keyword)  # typing keyword in text box

box.submit()

res = driver.find_elements_by_xpath('//h3//*') #all search result links have h3 header

j=1
for i in res:
    href = i.get_attribute("href")  # extracting info from selenium object using get_attribute()
    print "%d.) %s" %(j,href)                      # prints 8 search results
    j+=1

page2=driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr/td[3]/a') #going to page 2
page2.click()

res = driver.find_elements_by_xpath('//h3//*')


for i in res:
    href = i.get_attribute("href")  
    print "%d.) %s" %(j,href) 

    j+=1
    if j>10:
        break

    
"""Google scrapping can be done in shorter way using bs4. The code is :


import requests ; from bs4 import BeautifulSoup
import sys

search_item=input("enter search parameter:")
base="http://www.google.co.in"
url="http://www.google.co.in/search?q="+ search_item

response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
c=0;
for item in soup.select(".r a"):
	print(item.text)
	c=c+1
	if c>10 :
		break;
if c < 10 :
	for next_page in soup.select(".fl"):
		res=requests.get(base + next_page.get('href'))
		soup= BeautifulSoup(res.text,"lxml")
		while c <10 :
			for item in soup.select(".r a"):
				print(item.text)
				c+=1
                


driver.close()"""






