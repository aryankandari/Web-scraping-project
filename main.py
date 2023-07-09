import requests
from bs4 import BeautifulSoup

# url = "https://www.imdb.com"
# url = "https://www.amazon.in/Nike-Court-Vision-NN-WHITE-BLACK-WHITE-SESAME-DH2987-107-10UK/dp/B0BX4F3XG4/ref=sr_1_9?crid=1VOJVZ1TZ1J5Q&keywords=nike&qid=1688883363&s=shoes&sprefix=nik%2Cshoes%2C216&sr=1-9&th=1&psc=1"
# url = "https://www.coinbase.com" 
url = "https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQ3YAQHoAQGIAgGoAgO4AqG4qaUGwAIB0gIkMmQ4MDMxYjItZjhhNC00N2Y2LThkMmUtMTdmM2M1ZTM2ZDM52AIF4AIB&sid=cf4d5e387feae62a76fa5bb70e7212cf&keep_landing=1&sb_price_type=total&"

# # Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal

title = soup.title

# #commonly used object
# print(type(title)) # 1. tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# getting the title of HTML page
# print(title)

# get all the paragraph from the page
# paras = soup.find_all('p')
# print(paras)

# get all anchor tags
anchors = soup.find_all('a')
# get all the links on the page:
# for link in anchors:
#     print(link.get('href'))

# all_links = set()
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = "https://www.booking.com" + link.get('href')
#         all_links.add(linkText)
#         print(linkText)
# print(anchors)

# get the first element in the html page
# print(soup.find('p'))
# print(soup.find('p')['class'])

# find all element with class lead
# print(soup.find('p',class_= "lead"))

# get text from tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text()) # all the text on the page

indexsearch = soup.find(id='indexsearch')
# print(indexsearch)
# print(indexsearch.children)
# print(indexsearch.contents)

# for elem in indexsearch.stripped_strings:
#     print(elem)


# for elem in indexsearch.contents:
#     print(elem)

# print(indexsearch.parent)
# for elem in indexsearch.parent:
#     print(elem)
#     print(elem.name)

# print(indexsearch.next_sibling)

# elem = soup.select('.loginModal')
elem = soup.select('.modal-footer')
print(elem)