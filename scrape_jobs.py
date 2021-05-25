from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome(r'Web scraping\Selenium\chromedriver.exe')
driver.get('https://indeed.com')

job=input("What career are you looking to apply to? ")
search=driver.find_element_by_id("text-input-what")
search.clear()
search.send_keys(job)
search.send_keys(Keys.RETURN)

jobs=driver.find_element_by_id("resultsCol")
job_lst=jobs.text.split("\n")

for index,item in enumerate(job_lst[4:len(job_lst)-3]):

    if "More" in item or "days ago" in item or "·Save job" in item or "Just posted" in item:
        print("")
    else:
        print(index,item)


