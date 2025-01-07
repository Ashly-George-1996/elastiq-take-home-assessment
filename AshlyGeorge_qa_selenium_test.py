#Import the Necessary Classes
from selenium import webdriver
from selenium.webdriver.common.keys. import Keys

#Create a WebDriver Instance
driver = Webdriver.Chrome('./Chromedriver')

#Load the Website
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
#Check the Page Title
print(driver.title)

#Interact with the Search Bar
#Finds the search bar element
search_bar = driver.find_element(By.XPATH, "//*[@id="example_filter"]/label/input")

#Clears any existing text
search_bar.clear()

#Types the query into the search bar
search_bar.send_keys("New York")

#Simulates pressing the Return (Enter) key
search_ bar.send_keys(Keys.RETURN)

# to identify the table rows
r = driver.find_elements_by_xpath ("//*[@id="example"]/tbody/tr")

# to get row count with len method
rc = len (r)

# to identify table columns
c = driver.find_elements_by_xpath ("//*[@id="example"]/tbody/tr[3]/td")

# to get column count with len method
cc = len (c)

# to traverse through the table rows excluding headers
for i in range (2, rc + 1) :

# to traverse through the table column 
for j in range (1, cc + 1) :

# to get all the cell data with text method
d = driver.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text

# to search for our required text
m = driver.find_elements_by_xpath ("//td[text() = 'New York']")

# to get the size of the list with len method
s = len (m)

# check if list size is 5
If (s == 5) :
print ("New York found 5 times")

#close the browser session to end the test
driver.close
