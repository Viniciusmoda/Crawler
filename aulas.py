### Creditos : https://towardsdatascience.com/download-course-materials-with-a-simple-python-crawler-94e06d5f84b5

import os 
import requests
from lxml import etree
import wget


#### preparando 
download_directory= '/home/vinicius/Crawler/slides/'
url='http://inst.eecs.berkeley.edu/~cs61a/fa18/'
#requets

r=requests.get(url)
html=etree.HTML(r.text)

## links de extração
slide_links= html.xpath('//li/a[text()="8pp"]/@href')
slide_links=list(set(slide_links))# retirando links duplicados
print (len(slide_links))

#baixando os arquivos 
for slide in slide_links:
    print(slide)
    download_link= url+slide
    file_name= os.path.basename(slide)
    download_path = download_directory + file_name
    wget.download(download_link, download_path)
    print ("O arquivo {0} foi baixado".format(slide[17:-3]))
