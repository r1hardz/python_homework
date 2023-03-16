import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.imdb.com/title/tt6084202/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

class1 = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"
director = soup.find("a", class_=class1).text
writers = [writer.text for writer in soup.find_all("a", class_=class1)[1:3]]
stars = [star.text for star in soup.find_all("a", class_=class1)[3:6]]
awards = soup.find("span", class_="ipc-metadata-list-item__list-content-item").text
cast = [cast.text for cast in soup.find_all("div", class_="sc-bfec09a1-5 kUzsHJ")]
pattern = r'(?<=[a-z])(?=[A-Z])'

output_list = [re.split(pattern, s) for s in cast]

print("Director:",director)
print("Writers: " + ", ".join(writers))
print("Stars: " + ", ".join(stars))
print("Awards:",awards)
print("Cast list:")
for i, item in enumerate(output_list):
    print(f"{i+1}. " + ", ".join(item))
