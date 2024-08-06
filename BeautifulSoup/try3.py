from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source=requests.get('https://www.freeimages.com/search/dog', headers  =headers).text
soup = BeautifulSoup(source,'lxml')

Images=[]
img_links=soup.select('img[src="https://www.freeimages.com"]')

for i in range(len(img_links)):
    Images.append(img_links[i]['src'])

for i in range(len(Images)):
    name="D:/python/DogImage/"+str(i)+".jpg"
    urllib.request.urlretrieve(Images[i], name)
