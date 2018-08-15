
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os



url = "https://scholar.google.com/citations?user=6F3Kj_8AAAAJ&hl=en"



chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(chrome_options=chrome_options)  

driver.implicitly_wait(30)
driver.get(url)

python_button = driver.find_element_by_xpath('//*[@id="gsc_bpf_more"]')
python_button.click() #click fhsu link

time.sleep(5)

#Selenium hands the page source to Beautiful Soup

page_content = BeautifulSoup(driver.page_source, "html.parser")
publications = page_content.find_all(class_='gsc_a_t')
citations = page_content.find_all(class_='gsc_a_ac')
years = page_content.find_all(class_='gsc_a_h gsc_a_hc gs_ibl')

titles = []
authors = []
cites = []
ye = []
where = []

for p in publications:
    if p.a != None and p.div!=None:
        titles.append(p.a.get_text())
        aandw = p.find_all('div', class_='gs_gray')
        authors.append(aandw[0].get_text())
        where.append(aandw[1].get_text())

for c in citations:
    if c != None:
        cites.append(c.get_text())

for y in years:
    if y != None:
        ye.append(y.get_text())

for i in range(len(titles)):
	print(titles[i])
	print(authors[i])
	print(where[i])
	print(cites[i])
	print(ye[i])
	print("\n")

print(len(titles), len(cites), len(ye))
driver.close()

'''



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os



url = "https://scholar.google.com/citations?user=7pdeQX4AAAAJ&hl=en"



chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(chrome_options=chrome_options)  

driver.implicitly_wait(30)
driver.get(url)

python_button = driver.find_element_by_id('gsc_bpf_more')
python_button.click() #click fhsu link

time.sleep(5)

#Selenium hands the page source to Beautiful Soup

page_content = BeautifulSoup(driver.page_source, "html.parser")
publications = driver.find_elements_by_class_name('gsc_a_at')

links = []
titles = []
authors = []
cites = []
ye = []

for link in publications:
	
	link.click()
	time.sleep(5)
	print("Clicked")

	page_content = BeautifulSoup(driver.page_source, "html.parser")
	field = page_content.find(class_='gsc_vcd_title_link')
	
	if links:
		links.append(field['href'])
	else:
		links.append('#')

	driver.execute_script("window.history.go(-1)") 

	time.sleep(5)

print(links)

driver.close()
'''