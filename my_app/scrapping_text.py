import requests as rq
from bs4 import BeautifulSoup as bs
import re
#from .import domain_to_ip

def scrapping_text(url):

    page=rq.get(url)
    page_content=bs(page.content,'html.parser')

    title=page_content.title.string

    page_text=(str(page_content).replace('\n',''))
    page_text =(str ( page_text ).replace ( '\t' , '' ))
    page_text=(str(page_text).replace('&amp','and'))
    page_text=page_text.replace('\xa0',' ')

    regex='(<script\s.*?>.*?</script>)|(<script>(.*?)</script>)|(<style\s.*>.*?</style>)|(<style>(.*?)</style>)|(<.*?>)'

    pattern_x=re.compile(regex)
    website_content=re.sub(pattern_x,' ',page_text)

    website_content=re.sub(' +',' ',website_content)
    website_content=re.sub('[^A-Za-z\s]+', '', website_content)



    website_text=[title,website_content]

    return website_text[1]