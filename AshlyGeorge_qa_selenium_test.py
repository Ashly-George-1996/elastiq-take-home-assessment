from selenium import webdriver
from selenium.webdriver.common.keys. import Keys

driver = Webdriver.Chrome('./Chromedriver')

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
print(driver.title)

search_bar = driver.find_element(By.XPATH, "//*[@id="example_filter"]/label/input")
search_bar.clear()
search_bar.send_keys("New York")
search_ bar.send_keys(Keys.RETURN)

r = driver.find_elements_by_xpath ("//*[@id="example"]/tbody/tr")
rc = len (r)

c = driver.find_elements_by_xpath ("//*[@id="example"]/tbody/tr[3]/td")
cc = len (c)

for i in range (2, rc + 1) :
for j in range (1, cc + 1) :
  
d = driver.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text

m = driver.find_elements_by_xpath ("//td[text() = 'New York']")
s = len (m)
If (s == 5) :
print ("New York found 5 times")

driver.close
