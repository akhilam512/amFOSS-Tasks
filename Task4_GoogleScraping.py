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

    


driver.close()






