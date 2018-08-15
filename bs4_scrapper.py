from bs4 import BeautifulSoup
import requests

page_link = 'https://scholar.google.com/citations?user=tQT0OSAAAAAJ&hl=en'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
publications = page_content.find_all(class_='gsc_a_t')
citations = page_content.find_all(class_='gsc_a_ac')
years = page_content.find_all(class_='gsc_a_h gsc_a_hc gs_ibl')
titles = []
authors = []
for p in publications:
	if p.a!=None and p.div!=None:
		titles.append(p.a.get_text())
		authors.append(p.div.get_text())

print(len(titles), len(authors))

